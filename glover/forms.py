from datetime import date

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from glover.choices import GenderChoices, InterestChoices, SocietyChoices
from glover.models import Profile, Society, Interest

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        user_name = self.cleaned_data['username']
        pw = self.cleaned_data['password']

        # check the user exists
        if not User.objects.filter(username=user_name).exists():
            raise forms.ValidationError("This user does not exist.")

        # check if user is active, return custom message if not
        if not User.objects.get(username=user_name).is_active:
            raise forms.ValidationError("This user's profile is disabled.")
        
        # check user's authentication details are correct
        if not authenticate(username=user_name, password=pw):
            raise forms.ValidationError("Invalid login details.")

        return self.cleaned_data



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    dob = forms.DateField(label="Date of Birth", input_formats=['%d/%m/%Y'], widget=forms.TextInput(attrs={'autocomplete':'off'}))
    gender = forms.ChoiceField(choices=GenderChoices.get_choices(), widget=forms.Select(), required=True)

    def clean_confirm_password(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['confirm_password']

        if not password1 == password2:
            raise forms.ValidationError("The passwords do not match.")
        return password2

    def clean_email(self):
        email = self.cleaned_data['email'].strip()

        if not email.endswith('@student.gla.ac.uk'):
            raise forms.ValidationError("Email must belong to a University of Glasgow account ( @student.gla.ac.uk ).")
        return email

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        today = date.today()
        if (dob.year + 16, dob.month, dob.day) > (today.year, today.month, today.day):
            raise forms.ValidationError("You must be over 16 to use GLover.")
        return dob

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'gender', 'dob', 'password', 'confirm_password')
        help_texts = {
            'username': None,  # don't show any help messages for the username
        }

    
class EditProfileForm(forms.ModelForm):
    empty_label = [('', '---------'),]
    _interestchoices = empty_label + InterestChoices.get_choices()
    _societychoices = empty_label  + SocietyChoices.get_choices()

    interest1 = forms.ChoiceField(choices=_interestchoices, widget=forms.Select(), required=False)
    interest2 = forms.ChoiceField(choices=_interestchoices, widget=forms.Select(), required=False)
    interest3 = forms.ChoiceField(choices=_interestchoices, widget=forms.Select(), required=False)
    interest4 = forms.ChoiceField(choices=_interestchoices, widget=forms.Select(), required=False)
    interest5 = forms.ChoiceField(choices=_interestchoices, widget=forms.Select(), required=False)

    society1 = forms.ChoiceField(choices=_societychoices, widget=forms.Select(), required=False)
    society2 = forms.ChoiceField(choices=_societychoices, widget=forms.Select(), required=False)
    society3 = forms.ChoiceField(choices=_societychoices, widget=forms.Select(), required=False)
    society4 = forms.ChoiceField(choices=_societychoices, widget=forms.Select(), required=False)
    society5 = forms.ChoiceField(choices=_societychoices, widget=forms.Select(), required=False)

    def __init__(self, *args, **kwargs):
        """ Override constructor to set individual ChoiceFields based on user's database entries """

        super().__init__(*args, **kwargs)
        societies = self.instance.get_societies()
        society_fields = [self.fields['society1'], self.fields['society2'], self.fields['society3'],
                          self.fields['society4'], self.fields['society5']]
        
        for soc, soc_field in zip(societies, society_fields):
            soc_field.initial = soc

        interests = self.instance.get_interests()
        interest_fields = [self.fields['interest1'], self.fields['interest2'], self.fields['interest3'],
                          self.fields['interest4'], self.fields['interest5']]
        
        for interest, interest_field in zip(interests, interest_fields):
            interest_field.initial = interest

    def save(self, commit=True):
        profile = super().save()
        data = self.cleaned_data

        # extract submitted data for the societies and add to the profile
        societies = data['society1'], data['society2'], data['society3'], data['society4'], data['society5']
        societies = [s for s in societies if s != self.empty_label] # filter out the empty labels
        societies = set(Society.objects.filter(society__in=societies))
        profile.societies.clear()
        profile.societies.add(*societies)

        # extract submitted data for the interests and add to the profile
        interests = data['interest1'], data['interest2'], data['interest3'], data['interest4'], data['interest5']
        interests = [i for i in interests if i != self.empty_label] # filter out the empty labels
        interests = set(Interest.objects.filter(interest__in=interests))
        profile.interests.clear()
        profile.interests.add(*interests)
        return profile


    class Meta:
        model = Profile

        fields = ('gender', 'bio', 'year_in', 'course', 'location', 'library_floor', 'looking_for', 'society1', 'society2', 'society3',
            'society4', 'society5', 'interest1', 'interest2', 'interest3', 'interest4', 'interest5')