from django.contrib.auth.models import User
from django.db.models import Q

from .models import Profile, Like, Match, Message

 
def get_discover_profiles(profile: Profile):
    """ When given a profile, this function returns all to-be-discovered profiles that match both the 
        given profile's "looking for" choice, as well as reverse matching the "looking for" field for
        potential matches to ensure they match the given profile's gender 
    """
    likes = Like.objects.filter(profile=profile)
    looking_for = profile.looking_for
    gender = profile.gender
    already_liked = [l.profile_liked for l in likes]
    users = User.objects.exclude(Q(profile__in=already_liked) | Q(profile=profile)).select_related('profile')
    users = users.filter(profile__gender=looking_for).order_by('-date_joined')

    # remove users who are not looking for the given user's gender
    users = [user.profile for user in users if user.profile.looking_for == gender]
    return users

def get_matches(profile: Profile):
    """ Gets all matches for the user """
    matches = Match.objects.filter(Q(profile1=profile) | Q(profile2=profile)).order_by('-time_matched')
    profiles = []
    for match in matches:
        if match.profile1.pk != profile.pk:
            profiles.append(match.profile1)
        else:
            profiles.append(match.profile2)
    return profiles

def num_recent_matches(profile: Profile):
    """ Gets the number of new matches for a user since they last logged in """
    last_login = profile.user.last_login 

    if last_login is not None:
        matches =  Match.objects.filter(Q(profile1=profile) | Q(profile2=profile)) \
                                .filter(time_matched__gt=last_login)
        return matches.count()
    return 0

def user_chat_profiles(profile: Profile):
    """ Gets all profiles the user has shared messages with """
    msgs = Message.objects.filter(Q(sender=profile) | Q(receiver=profile))
    profiles = set()
    if msgs.exists():
        for msg in msgs:
            profiles.add(msg.receiver)
            profiles.add(msg.sender)
        # remove the profile user from the set
        profiles.remove(profile)
    return profiles

def num_recent_messages(profile: Profile):
    """ Gets the number of new matches for a user since they last logged in """
    last_login = profile.user.last_login 

    if last_login is not None:
        msgs = Message.objects.filter(receiver=profile).filter(time_sent__gt=last_login)
        return msgs.count()
    return 0

def get_discover_profiles_by_course(profile: Profile):
    """ Gets discover profiles that are in the same course """
    profiles = get_discover_profiles(profile)
    profiles_by_course = []
    
    for p in profiles:
        if p.course == profile.course:
            profiles_by_course.append(p)

    return profiles_by_course

def get_discover_profiles_by_year_in(profile: Profile):
    """ Gets discover profiles that are in the same year of study """
    profiles = get_discover_profiles(profile)
    profiles_by_year_in = []
    
    for p in profiles:
        if p.year_in == profile.year_in:
            profiles_by_year_in.append(p)

    return profiles_by_year_in

def get_discover_profiles_by_societies(profile: Profile):
    """ Gets discover profiles that share at least one society """
    profiles = get_discover_profiles(profile)
    profiles_by_societies = []
    user_societies = profile.get_societies()

    for p in profiles:
        for society in p.get_societies():
            if society in user_societies:
                profiles_by_societies.append(p)
                break

    return profiles_by_societies

def get_discover_profiles_by_interests(profile: Profile):
    """ Gets discover profiles that share at least one interest """
    profiles = get_discover_profiles(profile)
    profiles_by_interests = []
    user_interests = profile.get_interests()

    for p in profiles:
        for interest in p.get_interests():
            if interest in user_interests:
                profiles_by_interests.append(p)
                break

    return profiles_by_interests

def get_discover_profiles_by_age_ascending(profile: Profile):
    """ Gets discover profiles from youngest to oldest """
    profiles = get_discover_profiles(profile)
    profiles.sort(key=lambda u: u.dob, reverse=True)

    return profiles

def get_discover_profiles_by_age_descending(profile: Profile):
    """ Gets discover profiles from oldest to youngest """
    profiles = get_discover_profiles(profile)
    profiles.sort(key=lambda u: u.dob)

    return profiles

def get_matches_by_name_ascending(profile: Profile):
    """ Gets all matches for the user ordered by name (ascending order) """
    matches = get_matches(profile)
    matches.sort(key=lambda m: m.user.first_name)

    return matches

def get_matches_by_name_descending(profile: Profile):
    """ Gets all matches for the user ordered by name (descending order) """
    matches = get_matches(profile)
    matches.sort(key=lambda m: m.user.first_name, reverse=True)

    return matches

def get_matches_not_messaged(profile: Profile):
    """ Gets all matches that have not been messaged yet """
    matches = get_matches(profile)
    messaged_matches = user_chat_profiles(profile)
    not_messaged_matches = []
    
    for match in matches:
        if match not in messaged_matches:
            not_messaged_matches.append(match)
    
    return not_messaged_matches