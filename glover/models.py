from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

from .choices import CourseChoices, SocietyChoices, InterestChoices, GenderChoices, LibraryFloorChoices, YearInChoices


class Profile(models.Model):
    # get username, email, first_name, password from the User model when needed
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GenderChoices.get_choices())
    bio = models.TextField(max_length=300, default="")
    year_in = models.CharField(max_length=20, choices=YearInChoices.get_choices(), null=True)
    location = models.CharField(max_length=30, default="")
    library_floor = models.CharField(max_length=20, choices=LibraryFloorChoices.get_choices())
    looking_for = models.CharField(max_length=1, choices=GenderChoices.get_choices())  # Allow to pick one, not multiple

    image1 = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    image2 = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    image3 = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    image4 = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    image5 = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True)
    interests = models.ManyToManyField("Interest", blank=True)
    societies = models.ManyToManyField("Society", blank=True)

    def get_age(self):
        """ Gets the age of the user """
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def get_num_societies(self):
        """ Gets the number of societies the user is in """
        return self.societies.count()

    def get_num_interests(self):
        """ Gets the number of interests the user has listed """
        return self.interests.count()

    def get_societies(self):
        """ Gets all societies the user is in """
        return self.societies.all()

    def get_interests(self):
        """ Gets all the user's interests """
        return self.interests.all()

    def __str__(self):
        return self.user.username


class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="likes")
    profile_liked = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="liked")
    is_liked = models.BooleanField()  # if false - represents a dislike, if true - like

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['profile', 'profile_liked'], name='unique_likes')
        ]

    def save(self, *args, **kwargs):
        """ Override the model's save method to automatically create a match on two likes """
        super().save(*args, **kwargs)
        if self.is_liked:
            if Like.objects.filter(profile=self.profile_liked, profile_liked=self.profile, is_liked=True).exists():
                match = Match.objects.get_or_create(profile1=self.profile, profile2=self.profile_liked)

    def __str__(self):
        if self.is_liked:
            return f"{self.profile.user.username} liked {self.profile_liked.user.username}"
        elif not self.is_liked:
            return f"{self.profile.user.username} disliked {self.profile_liked.user.username}"


class Match(models.Model):
    profile1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="matches")
    profile2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="matched")
    time_matched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile1.user.username} + {self.profile2.user.username}"

    class Meta:
        verbose_name_plural = "Matches"
        constraints = [
            models.UniqueConstraint(fields=['profile1', 'profile2'], name='unique_matches')
        ]


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    message = models.TextField(max_length=500)
    time_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Society(models.Model):
    society = models.CharField(max_length=50, choices=SocietyChoices.get_choices(), unique=True)

    def __str__(self):
        return self.society

    class Meta:
        ordering = ['society']
        verbose_name_plural = 'Societies'


class Course(models.Model):
    course = models.CharField(max_length=50, choices=CourseChoices.get_choices(), unique=True)

    def __str__(self):
        return self.course


class Interest(models.Model):
    interest = models.CharField(max_length=30, choices=InterestChoices.get_choices(), unique=True)

    def __str__(self):
        return self.interest

    class Meta:
        ordering = ['interest']
