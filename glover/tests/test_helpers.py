import random
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad_team_B_project.settings')

# import django
# django.setup()

from glover.choices import *
from glover.models import *
from django.contrib.auth.models import User

def populate():
    
    add_societies()
    add_interests()
    add_courses()
    
    if User.objects.filter(username='bob').exists():
        User.objects.all().delete()
    
    user6 = User.objects.create_user(username='bob', password='1234', email="bob@student.gla.ac.uk", first_name="Bob")
    user7 = User.objects.create_user(username='linda', password='1234', email="linda@student.gla.ac.uk", first_name="Linda")
    user8 = User.objects.create_user(username='jack', password='1234', email="jack@student.gla.ac.uk", first_name="Jack")
    user9 = User.objects.create_user(username='peter', password='1234', email="peter@student.gla.ac.uk", first_name="Peter")
    user10 = User.objects.create_user(username='melinda', password='1234', email="melinda@student.gla.ac.uk", first_name="Melinda")
    
    user11 = User.objects.create_user(username='john', password='1234', email="john@student.gla.ac.uk", first_name="John")
    user12 = User.objects.create_user(username='jack2', password='1234', email="jack@student.gla.ac.uk", first_name="Jack")
    user13 = User.objects.create_user(username='jessica', password='1234', email="jessica@student.gla.ac.uk", first_name="Jessica")
    user14 = User.objects.create_user(username='greta', password='1234', email="greta@student.gla.ac.uk", first_name="Greta")
    user15 = User.objects.create_user(username='lea', password='1234', email="lea@student.gla.ac.uk", first_name="Lea")

    profiles = [
        {'user': user6, 'dob': '1996-05-16', 'gender': "N", 'bio': "sup it's Bob", 'year_in': "1st Year", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "N", 'course_id': 26},
        {'user': user7, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Linda", 'year_in': "4th Year", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 26},
        {'user': user8, 'dob': '1996-05-16', 'gender': "M", 'bio': "sup it's Jack", 'year_in': "2nd Year", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "F", 'course_id': 2},            
        {'user': user9, 'dob': '1996-05-16', 'gender': "M", 'bio': "sup it's Peter", 'year_in': "PHD", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "F", 'course_id': 32},
        {'user': user10, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Melinda", 'year_in': "Masters", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "F", 'course_id': 26},   
        {'user': user11, 'dob': '1996-05-16', 'gender': "M", 'bio': "sup it's John", 'year_in': "MPhil", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "F", 'course_id': 10},
        {'user': user12, 'dob': '1996-05-16', 'gender': "N", 'bio': "sup it's Jack", 'year_in': "3rd Year", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "N", 'course_id': 10},
        {'user': user13, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Jessica", 'year_in': "2nd Year", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 10},            
        {'user': user14, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Greta", 'year_in': "1st Year", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 10},
        {'user': user15, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Lea", 'year_in': "4th Year", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "N", 'course_id': 10}
    ]

    for profile_data in profiles:
        p = add_profile(profile_data['user'], profile_data['dob'], profile_data['gender'], profile_data['bio'], profile_data['year_in'],
            profile_data['location'], profile_data['library_floor'], profile_data['looking_for'], profile_data['course_id'])
        


def add_like(profile, profile_liked):
    like = Like.objects.get_or_create(profile=profile, profile_liked=profile_liked, is_liked=True)[0]
    
def add_profile(user, dob, gender, bio, year_in, location, library_floor, looking_for, course_id):
    profile = Profile.objects.get_or_create(user=user, dob=dob, gender=gender, bio=bio, year_in=year_in, 
            location=location, library_floor=library_floor, looking_for=looking_for, course_id=course_id)[0]
    return profile

def add_societies():
    for society in SocietyChoices.ALL_CHOICES:
        Society.objects.get_or_create(society=society)

def add_interests():
    for interest in InterestChoices.ALL_CHOICES:
        Interest.objects.get_or_create(interest=interest)

def add_courses():
    for course in CourseChoices.ALL_CHOICES:
        Course.objects.get_or_create(course=course)