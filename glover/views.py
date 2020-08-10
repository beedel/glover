import os

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.messages import success, info, warning
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from glover.forms import UserRegistrationForm, LoginForm, EditProfileForm
from glover.models import Profile, Match, Like, Message
from glover import utils


def index(request):
    return render(request, 'glover/index.html')


def about(request):
    return render(request, 'glover/about.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            dob = user_form.cleaned_data['dob']
            gender = user_form.cleaned_data['gender']
            profile = Profile.objects.create(user=user, dob=dob, gender=gender)

            login(request, user)
            success(request, f"Congratulations, {user.first_name}! You've registered successfully!")
            return redirect(reverse('glover:discover'))
        else:
            print(user_form.errors)
    else:
        user_form = UserRegistrationForm()

    context = {
        'registration_form': user_form,
    }
    return render(request, 'glover/register.html', context)


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            # get number of new matches since last login
            num_new_matches = utils.num_recent_matches(user.profile)
            num_new_messages = utils.num_recent_messages(user.profile)
            login(request, user)

            if num_new_matches == 1:
                info(request, f"You've got {num_new_matches} new match! Don't be shy to slide into their DMs!")
            if num_new_matches > 1:
                info(request, f"You've got {num_new_matches} new matches! Don't be shy to slide into their DMs!")

            if num_new_messages == 1:
                info(request, f"You've got {num_new_messages} new message!")
            if num_new_messages > 1:
                info(request, f"You've got {num_new_messages} new messages!")

            return redirect(reverse('glover:discover'))

    return render(request, 'glover/login.html', {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('glover:index'))


@login_required
def discover(request):
    qfilter = request.GET.get("filter", None)
    profile = request.user.profile

    if qfilter is None:
        profile_list = utils.get_discover_profiles(profile)
    elif qfilter == 'course':
        profile_list = utils.get_discover_profiles_by_course(profile)
    elif qfilter == 'year-in':
        profile_list = utils.get_discover_profiles_by_year_in(profile)
    elif qfilter == 'society':
        profile_list = utils.get_discover_profiles_by_societies(profile)   
    elif qfilter == 'interest':
        profile_list = utils.get_discover_profiles_by_interests(profile)
    elif qfilter == 'age':
        profile_list = utils.get_discover_profiles_by_age_ascending(profile)
    elif qfilter == 'age-reverse':
        profile_list = utils.get_discover_profiles_by_age_descending(profile)

    context_dict = {'profiles': profile_list}

    return render(request, 'glover/discover.html', context_dict)


@login_required
def discover_profile(request, username):
    context_dict = {}

    try:
        user = User.objects.get(username=username)
        profile = user.profile

        d_profiles = utils.get_discover_profiles(request.user.profile)
        if profile not in d_profiles:
            warning(request, 'That user cannot be viewed.')
            return redirect('glover:discover')
            
        context_dict['profile'] = profile

    except Profile.DoesNotExist:
        context_dict['profile'] = None

    return render(request, 'glover/discover-profile.html', context=context_dict)


@login_required
def match_profile(request, username):
    context_dict = {}
    profile = request.user.profile

    try:
        user = User.objects.get(username=username)
        matches = utils.get_matches(profile)
        if user.profile not in matches:
            warning(request, 'You have not been matched with that user.')
            return redirect('glover:matches')
        context_dict['profile'] = user.profile

    except Profile.DoesNotExist:
        context_dict['profile'] = None

    return render(request, 'glover/match-profile.html', context=context_dict)


########
# Profile Views

@login_required
def profile(request):
    profile = request.user.profile

    return render(request, 'glover/profile.html', {"profile": profile})


@login_required
def edit_profile(request):
    form = EditProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            success(request, f"Profile updated successfully!")
            return redirect(reverse('glover:profile'))

    return render(request, 'glover/edit-profile.html', {"form": form})

@login_required
def delete_account(request):
    request.user.delete()
    success(request, f"Your account has been successfully deleted. Sorry to see you go!")
    return redirect(reverse('glover:index'))

@login_required
def edit_photos(request):
    if request.method == 'POST':
        profile = request.user.profile
        picture_fields = [profile.image1, profile.image2, profile.image3, profile.image4, profile.image5]
        updatable_pics = [i for i in picture_fields if not bool(i)]
        update_field = ([bool(i) for i in picture_fields]).index(
            False) + 1  # get the number of the image-field to be updated

        if len(updatable_pics) > 0:
            img_file = request.FILES['file']
            updatable_pics[0].save(img_file.name, img_file, save=True)
            return JsonResponse({"imgnum": update_field, "imgpath": updatable_pics[0].url})
    return render(request, 'glover/edit-photos.html')


@login_required
def matches(request):
    context_dict = {}
    qfilter = request.GET.get("filter", None)
    profile = request.user.profile

    if qfilter is None:
        matches = utils.get_matches(profile)
    elif qfilter == 'name-a':
        matches = utils.get_matches_by_name_ascending(profile)
    elif qfilter == 'name-d':
        matches = utils.get_matches_by_name_descending(profile)
    elif qfilter == 'messaged':
        matches = utils.user_chat_profiles(profile)
    elif qfilter == 'not-messaged':
        matches = utils.get_matches_not_messaged(profile)

    context_dict = {'profiles': matches}

    return render(request, 'glover/matches.html', context=context_dict)


@login_required
def like(request, profile2):
    profile1 = request.user.profile
    profile2 = User.objects.get(username=profile2).profile

    if "like" in request.POST:
        like = Like.objects.get_or_create(profile=profile1, profile_liked=profile2, is_liked=True)[0]

        if Like.objects.filter(profile=profile2, profile_liked=profile1, is_liked=True).exists():
            success(request, f"It's a match! You can now chat with {profile2.user.first_name}!")
        else:
            info(request, f"Happy to see you liked {profile2.user.first_name}!")

    elif "dislike" in request.POST:
        like = Like.objects.get_or_create(profile=profile1, profile_liked=profile2, is_liked=False)[0]

    return redirect(reverse('glover:discover'))


@login_required
def unmatch(request, profile2):
    profile1 = request.user.profile
    profile2 = User.objects.get(username=profile2).profile

    if "unmatch" in request.POST:
        like = Like.objects.filter(profile=profile1, profile_liked=profile2)
        like.delete()

        msgs = Message.objects.filter(Q(sender=profile1, receiver=profile2) | Q(sender=profile2, receiver=profile1))
        msgs.delete()

        dislike = Like.objects.get_or_create(profile=profile1, profile_liked=profile2, is_liked=False)[0]

        Match.objects.filter(Q(profile1=profile1, profile2=profile2) | Q(profile1=profile2, profile2=profile1)).delete()
        info(request, f"You've successfully unmatched {profile2.user.first_name}.")

    return redirect(reverse('glover:matches'))


@login_required
def block(request, profile2):
    profile1 = request.user.profile
    profile2 = User.objects.get(username=profile2).profile

    if "block" in request.POST:
        likes = Like.objects.filter(Q(profile=profile1, profile_liked=profile2) | Q(profile=profile2, profile_liked=profile1))
        likes.delete()

        msgs = Message.objects.filter(Q(sender=profile1, receiver=profile2) | Q(sender=profile2, receiver=profile1))
        msgs.delete()

        dislike1 = Like.objects.get_or_create(profile=profile1, profile_liked=profile2, is_liked=False)[0]
        dislike2 = Like.objects.get_or_create(profile=profile2, profile_liked=profile1, is_liked=False)[0]

        Match.objects.filter(Q(profile1=profile1, profile2=profile2) | Q(profile1=profile2, profile2=profile1)).delete()
        info(request, f"Blocked! {profile2.user.first_name} won't bother you anymore.")

    return redirect(reverse('glover:matches'))


#### AJAX VIEWS
@login_required
def delete_photo(request):
    """ Deletes user picture specified by query parameter """
    picture = request.GET.get('img', None)  # get the picture from the query parameter

    photo_profile_map = {
        "img1": request.user.profile.image1,
        "img2": request.user.profile.image2,
        "img3": request.user.profile.image3,
        "img4": request.user.profile.image4,
        "img5": request.user.profile.image5
    }

    if picture is None or picture not in photo_profile_map.keys():
        return redirect(reverse('glover:edit-photos'))

    photo_profile_map[picture].delete()

    picture_fields = list(photo_profile_map.values())

    if not bool(picture_fields[0]):
        for field in picture_fields[1:]:
            if bool(field):
                picture_fields[0].save(field.name, field)
                field.delete()
                request.user.profile.save()
                break

    return JsonResponse({"url": reverse('glover:edit-photos')})


@login_required
def messages(request):
    context_dict = {}
    context_dict['users_messaged'] = utils.user_chat_profiles(request.user.profile)
    return render(request, 'glover/dms.html', context=context_dict)

@login_required
def user_messages(request, username):
    profile = Profile.objects.get(user__username=username)
    matches = utils.get_matches(request.user.profile)
    if profile not in matches:
        warning(request, 'You cannot message this user.')
        return redirect('glover:messages')

    if request.method == "POST":
        msg = request.POST.get('message-content')
        Message.objects.create(sender=request.user.profile, receiver=profile, message=msg)
    
    context_dict = {}
    q1 = Q(sender=request.user.profile, receiver=profile)
    q2 = Q(sender=profile, receiver=request.user.profile)
    chat = Message.objects.filter(q1|q2).order_by('time_sent')
    context_dict['chat'] = chat
    context_dict['profile'] = profile
    context_dict['users_messaged'] = utils.user_chat_profiles(request.user.profile)
    return render(request, 'glover/messages.html', context=context_dict)
