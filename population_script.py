import os, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad_team_B_project.settings')

import django
django.setup()

from glover.choices import *
from glover.models import *
from django.contrib.auth.models import User
from glover import utils

def populate():

    add_societies()
    add_interests()
    add_courses()
    
    if User.objects.filter(username='ilona').exists():
        User.objects.all().delete()

    user1 = User.objects.create_user(username='tomas', password='1234', is_superuser=True, is_staff=True, email="tomas@student.gla.ac.uk", first_name="Tomas")
    user2 = User.objects.create_user(username='ilona', password='1234', is_superuser=True, is_staff=True, email="ilona@student.gla.ac.uk", first_name="Ilona")
    user3 = User.objects.create_user(username='vrinda', password='1234', is_superuser=True, is_staff=True, email="vrinda@student.gla.ac.uk", first_name="Vrinda")
    user4 = User.objects.create_user(username='fraser', password='1234', is_superuser=True, is_staff=True, email="fraser@student.gla.ac.uk", first_name="Fraser")
    user5 = User.objects.create_user(username='barbara', password='1234', is_superuser=True, is_staff=True, email="barbara@student.gla.ac.uk", first_name="Barbara")
    
    user6 = User.objects.create_user(username='bob', password='1234', email="bob@student.gla.ac.uk", first_name="Bob")
    user7 = User.objects.create_user(username='linda', password='1234', email="linda@student.gla.ac.uk", first_name="Linda")
    user8 = User.objects.create_user(username='jack', password='1234', email="jack@student.gla.ac.uk", first_name="Jack")
    user9 = User.objects.create_user(username='peter', password='1234', email="peter@student.gla.ac.uk", first_name="Peter")
    user10 = User.objects.create_user(username='melinda', password='1234', email="melinda@student.gla.ac.uk", first_name="Melinda")
    user11 = User.objects.create_user(username='john', password='1234', email="john@student.gla.ac.uk", first_name="John")
    user12 = User.objects.create_user(username='ken', password='1234', email="ken@student.gla.ac.uk", first_name="Ken")
    user13 = User.objects.create_user(username='jessica', password='1234', email="jessica@student.gla.ac.uk", first_name="Jessica")
    user14 = User.objects.create_user(username='greta', password='1234', email="greta@student.gla.ac.uk", first_name="Greta")
    user15 = User.objects.create_user(username='lea', password='1234', email="lea@student.gla.ac.uk", first_name="Lea")
    user16 = User.objects.create_user(username='amanda', password='1234', email="amanda@student.gla.ac.uk", first_name="Amanda")
    user17 = User.objects.create_user(username='jess', password='1234', email="jess@student.gla.ac.uk", first_name="Jess")
    user18 = User.objects.create_user(username='hugo', password='1234', email="hugo@student.gla.ac.uk", first_name="Hugo")
    user19 = User.objects.create_user(username='marina', password='1234', email="marina@student.gla.ac.uk", first_name="Marina")
    user20 = User.objects.create_user(username='lizzy', password='1234', email="lizzy@student.gla.ac.uk", first_name="Lizzy")
    user21 = User.objects.create_user(username='kyle', password='1234', email="kyle@student.gla.ac.uk", first_name="Kyle")
    user22 = User.objects.create_user(username='kim', password='1234', email="kim@student.gla.ac.uk", first_name="Kim")
    user23 = User.objects.create_user(username='joey', password='1234', email="joey@student.gla.ac.uk", first_name="Joey")
    user24 = User.objects.create_user(username='chris', password='1234', email="chris@student.gla.ac.uk", first_name="Chris")
    user25 = User.objects.create_user(username='david', password='1234', email="david@student.gla.ac.uk", first_name="David")
    user26 = User.objects.create_user(username='kylie', password='1234', email="kylie@student.gla.ac.uk", first_name="Kylie")
    user27 = User.objects.create_user(username='sabrina', password='1234', email="sabrina@student.gla.ac.uk", first_name="Sabrina")
    user28 = User.objects.create_user(username='matthew', password='1234', email="matthew@student.gla.ac.uk", first_name="Matthew")
    user29 = User.objects.create_user(username='laura', password='1234', email="laura@student.gla.ac.uk", first_name="Laura")
    user30 = User.objects.create_user(username='rosie', password='1234', email="rosie@student.gla.ac.uk", first_name="Rosie")
    user31 = User.objects.create_user(username='tim', password='1234', email="tim@student.gla.ac.uk", first_name="Tim")
    user32 = User.objects.create_user(username='love', password='1234', email="love@student.gla.ac.uk", first_name="Love")
    user33 = User.objects.create_user(username='anna', password='1234', email="anna@student.gla.ac.uk", first_name="Anna")
    user34 = User.objects.create_user(username='bill', password='1234', email="bill@student.gla.ac.uk", first_name="Bill")
    user35 = User.objects.create_user(username='tom', password='1234', email="tom@student.gla.ac.uk", first_name="Tom")
    user36 = User.objects.create_user(username='caroline', password='1234', email="caroline@student.gla.ac.uk", first_name="Caroline")
    user37 = User.objects.create_user(username='tamara', password='1234', email="tamara@student.gla.ac.uk", first_name="Tamara")
    user38 = User.objects.create_user(username='hannah', password='1234', email="hannah@student.gla.ac.uk", first_name="Hannah")
    user39 = User.objects.create_user(username='rick', password='1234', email="rick@student.gla.ac.uk", first_name="Rick")
    user40 = User.objects.create_user(username='saul', password='1234', email="saul@student.gla.ac.uk", first_name="Saul")
    user41 = User.objects.create_user(username='mike', password='1234', email="mike@student.gla.ac.uk", first_name="Mike")
    user42 = User.objects.create_user(username='amy', password='1234', email="amy@student.gla.ac.uk", first_name="Amy")
    user43 = User.objects.create_user(username='irina', password='1234', email="irina@student.gla.ac.uk", first_name="Irina")
    user44 = User.objects.create_user(username='dexter', password='1234', email="dexter@student.gla.ac.uk", first_name="Dexter")
    user45 = User.objects.create_user(username='rita', password='1234', email="rita@student.gla.ac.uk", first_name="Rita")
    user46 = User.objects.create_user(username='sarah', password='1234', email="sarah@student.gla.ac.uk", first_name="Sarah")
    user47 = User.objects.create_user(username='josh', password='1234', email="josh@student.gla.ac.uk", first_name="Josh")
    user48 = User.objects.create_user(username='cher', password='1234', email="cher@student.gla.ac.uk", first_name="Cher")
    user49 = User.objects.create_user(username='emma', password='1234', email="emma@student.gla.ac.uk", first_name="Emma")
    user50 = User.objects.create_user(username='robert', password='1234', email="robert@student.gla.ac.uk", first_name="Robert")
    user51 = User.objects.create_user(username='emily', password='1234', email="emily@student.gla.ac.uk", first_name="Emily")
    user52 = User.objects.create_user(username='olivia', password='1234', email="olivia@student.gla.ac.uk", first_name="Olivia")
    user53 = User.objects.create_user(username='amelia', password='1234', email="amelia@student.gla.ac.uk", first_name="Amelia")
    user54 = User.objects.create_user(username='omar', password='1234', email="omar@student.gla.ac.uk", first_name="Omar")
    user55 = User.objects.create_user(username='vivian', password='1234', email="vivian@student.gla.ac.uk", first_name="Vivian")
    user56 = User.objects.create_user(username='edward', password='1234', email="edward@student.gla.ac.uk", first_name="Edward")
    user57 = User.objects.create_user(username='ollie', password='1234', email="ollie@student.gla.ac.uk", first_name="Ollie")
    user58 = User.objects.create_user(username='henry', password='1234', email="henry@student.gla.ac.uk", first_name="Henry")
    user59 = User.objects.create_user(username='noah', password='1234', email="noah@student.gla.ac.uk", first_name="Noah")
    user60 = User.objects.create_user(username='evelyn', password='1234', email="evelyn@student.gla.ac.uk", first_name="Evelyn")


    profiles = [
        {'user': user1, 'dob': '1996-02-19', 'gender': "M", 'bio': "sup it's Tomas", 'year_in': "2nd Year", 'location': 'Glasgow', 'library_floor': "Level 3", 'looking_for': "F", 'course_id': 10},
        {'user': user2, 'dob': '1996-05-16', 'gender': "F", 'bio': "sup it's Ilona", 'year_in': "2nd Year", 'location': 'Glasgow', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 10},
        {'user': user3, 'dob': '1998-01-10', 'gender': "F", 'bio': "sup it's Vrinda", 'year_in': "2nd Year", 'location': 'Glasgow', 'library_floor': "Level 5", 'looking_for': "M", 'course_id': 10},            
        {'user': user4, 'dob': '1999-07-23', 'gender': "M", 'bio': "sup it's Fraser", 'year_in': "2nd Year", 'location': 'Glasgow', 'library_floor': "Level 6", 'looking_for': "F", 'course_id': 10},
        {'user': user5, 'dob': '1996-07-16', 'gender': "F", 'bio': "sup it's Barbara", 'year_in': "2nd Year", 'location': 'Glasgow', 'library_floor': "Level 7", 'looking_for': "M", 'course_id': 10},   
        
        {'user': user6, 'dob': '1990-03-16', 'gender': "N", 'bio': "Love is like a roller coaster, once you have completed the ride, you want to go again.", 'year_in': "3rd Year", 'location': 'Airdrie', 'library_floor': "Level 3", 'looking_for': "N", 'course_id': 26},
        {'user': user7, 'dob': '1990-01-16', 'gender': "N", 'bio': "I can drive you crazy without a drivers license!", 'year_in': "3rd Year", 'location': 'Airdrie', 'library_floor': "Level 6", 'looking_for': "N", 'course_id': 24},
        {'user': user8, 'dob': '1996-08-16', 'gender': "N", 'bio': "Great things we want to rush, but love simply happens on its own. Don't rush. God took the time to make you for me.", 'year_in': "3rd Year", 'location': 'Airdrie', 'library_floor': "Level 6", 'looking_for': "N", 'course_id': 2},            
        {'user': user9, 'dob': '1995-05-15', 'gender': "M", 'bio': "7 Billion people on this earth and my mind and heart is stuck on you...", 'year_in': "3rd Year", 'location': 'Airdrie', 'library_floor': "Level 8", 'looking_for': "M", 'course_id': 32},
        {'user': user10, 'dob': '1993-03-16', 'gender': "F", 'bio': "Save your heart for someone who leaves you breathless!", 'year_in': "1st Year", 'location': 'Paisley', 'library_floor': "Level 1", 'looking_for': "F", 'course_id': 26},   
        {'user': user11, 'dob': '1998-08-16', 'gender': "M", 'bio': "Your smile is like a sunrise, it sets the clouds on fire. But just being with you, is what I always admire.", 'year_in': "1st Year", 'location': 'Paisley', 'library_floor': "Level 2", 'looking_for': "M", 'course_id': 13},
        {'user': user12, 'dob': '1991-01-16', 'gender': "M", 'bio': "Let me tie your shoes, because I don't want you falling for anyone else.", 'year_in': "1st Year", 'location': 'Paisley', 'library_floor': "Level 2", 'looking_for': "M", 'course_id': 1},
        {'user': user13, 'dob': '1986-03-16', 'gender': "F", 'bio': "I don't have a library card, but do you mind if I check you out?", 'year_in': "1st Year", 'location': 'Paisley', 'library_floor': "Level 2", 'looking_for': "F", 'course_id': 19},            
        {'user': user14, 'dob': '1976-05-16', 'gender': "F", 'bio': "We go together like copy and paste.", 'year_in': "4th Year", 'location': 'Paisley', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 11},
        {'user': user15, 'dob': '1997-09-16', 'gender': "F", 'bio': "Roses are red, violets are blue, I'm counting the days until I can finally see you...", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 3", 'looking_for': "M", 'course_id': 17},   
        {'user': user16, 'dob': '1997-04-16', 'gender': "F", 'bio': "My heart and I agree... You're the only one for me.", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 26},
        {'user': user17, 'dob': '1994-08-22', 'gender': "F", 'bio': "I wanna be your girlfriend more than an electron wants to attach to a proton.", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 26},
        {'user': user18, 'dob': '1981-06-26', 'gender': "M", 'bio': "Now I understand why we can't be together. Because God does not want us to have the perfect life.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 8", 'looking_for': "F", 'course_id': 2},            
        {'user': user19, 'dob': '1988-05-26', 'gender': "N", 'bio': "There are many fish in the sea but you will always be my Nemo.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 9", 'looking_for': "N", 'course_id': 4},
        {'user': user20, 'dob': '1990-09-19', 'gender': "N", 'bio': "Being in love is like living in a cheesy little love song...", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 9", 'looking_for': "N", 'course_id': 25},
        {'user': user21, 'dob': '1994-01-09', 'gender': "N", 'bio': "If kisses were snowflakes, I'd send you a blizzard", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 18},
        {'user': user22, 'dob': '1993-09-19', 'gender': "N", 'bio': "If I can be with you in my dreams, I would sleep forever..", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 5", 'looking_for': "F", 'course_id': 15},
        {'user': user23, 'dob': '1992-07-09', 'gender': "M", 'bio': "It takes more than a million people to complete the world, but it only takes you to complete mine.", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 5", 'looking_for': "N", 'course_id': 15},
        {'user': user24, 'dob': '1991-06-19', 'gender': "F", 'bio': "I love you with all my butt, I would say heart, but my butt is bigger.", 'year_in': "MPhil", 'location': 'Glasgow', 'library_floor': "Level 5", 'looking_for': "N", 'course_id': 24},
        {'user': user25, 'dob': '1990-09-19', 'gender': "M", 'bio': "I'm not a photographer, but I can picture us together.", 'year_in': "MPhil", 'location': 'Glasgow', 'library_floor': "Level 9", 'looking_for': "F", 'course_id': 20},          
        {'user': user26, 'dob': '1997-04-16', 'gender': "F", 'bio': "Nobody has ever measured, even poets, how much a heart can hold.", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 2},
        {'user': user27, 'dob': '1994-08-22', 'gender': "F", 'bio': "Love is the joy of the good, the wonder of the wise, the amazement of the gods.", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 7},
        {'user': user28, 'dob': '1981-06-26', 'gender': "M", 'bio': "The best thing to hold onto in life is each other.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 8", 'looking_for': "F", 'course_id': 2},            
        {'user': user29, 'dob': '1988-05-26', 'gender': "N", 'bio': "When you trip over love, it is easy to get up. But when you fall in love, it is impossible to stand again.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 9", 'looking_for': "N", 'course_id': 9},
        {'user': user30, 'dob': '1990-09-19', 'gender': "N", 'bio': "Love is too strong a word to say it too early, but it has too beautiful a meaning to say it too late.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 9", 'looking_for': "N", 'course_id': 25},
        {'user': user31, 'dob': '1994-01-09', 'gender': "N", 'bio': "I would rather share one lifetime with you than face all the ages of this world alone.", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 28},
        {'user': user32, 'dob': '1993-09-19', 'gender': "N", 'bio': "Your smile is like a sunrise, it sets the clouds on fire. But just being with you, is what I always admire.", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 5", 'looking_for': "F", 'course_id': 15},
        {'user': user33, 'dob': '1992-07-09', 'gender': "M", 'bio': "Love is the triumph of imagination over intelligence.", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 5", 'looking_for': "N", 'course_id': 18},
        {'user': user34, 'dob': '1991-06-19', 'gender': "F", 'bio': "I love you with all my butt, I would say heart, but my butt is bigger.", 'year_in': "MPhil", 'location': 'Glasgow', 'library_floor': "Level 5", 'looking_for': "N", 'course_id': 21},
        {'user': user35, 'dob': '1990-09-19', 'gender': "M", 'bio': "I'm not a photographer, but I can picture us together.", 'year_in': "MPhil", 'location': 'Glasgow', 'library_floor': "Level 9", 'looking_for': "F", 'course_id': 20},
        {'user': user36, 'dob': '1990-09-19', 'gender': "N", 'bio': "Being in love is like living in a cheesy little love song...", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 9", 'looking_for': "N", 'course_id': 25},
        {'user': user37, 'dob': '1994-01-09', 'gender': "N", 'bio': "If kisses were snowflakes, I'd send you a blizzard", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 18},
        {'user': user38, 'dob': '1993-09-19', 'gender': "N", 'bio': "If I can be with you in my dreams, I would sleep forever..", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 5", 'looking_for': "F", 'course_id': 15},
        {'user': user39, 'dob': '1992-07-09', 'gender': "M", 'bio': "It takes more than a million people to complete the world, but it only takes you to complete mine.", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 5", 'looking_for': "N", 'course_id': 15},
        {'user': user40, 'dob': '1991-06-19', 'gender': "F", 'bio': "I love you with all my butt, I would say heart, but my butt is bigger.", 'year_in': "MPhil", 'location': 'Glasgow', 'library_floor': "Level 5", 'looking_for': "N", 'course_id': 24},
        {'user': user41, 'dob': '1990-09-19', 'gender': "M", 'bio': "I'm not a photographer, but I can picture us together.", 'year_in': "MPhil", 'location': 'Glasgow', 'library_floor': "Level 9", 'looking_for': "F", 'course_id': 20},          
        {'user': user42, 'dob': '1997-04-16', 'gender': "F", 'bio': "Nobody has ever measured, even poets, how much a heart can hold.", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 2},
        {'user': user43, 'dob': '1994-08-22', 'gender': "F", 'bio': "Love is the joy of the good, the wonder of the wise, the amazement of the gods.", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 7},
        {'user': user44, 'dob': '1981-06-26', 'gender': "M", 'bio': "The best thing to hold onto in life is each other.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 8", 'looking_for': "F", 'course_id': 2},            
        {'user': user45, 'dob': '1988-05-26', 'gender': "N", 'bio': "When you trip over love, it is easy to get up. But when you fall in love, it is impossible to stand again.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 9", 'looking_for': "N", 'course_id': 9},
        {'user': user46, 'dob': '1990-09-19', 'gender': "N", 'bio': "Love is too strong a word to say it too early, but it has too beautiful a meaning to say it too late.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 9", 'looking_for': "N", 'course_id': 25},
        {'user': user47, 'dob': '1994-01-09', 'gender': "N", 'bio': "I would rather share one lifetime with you than face all the ages of this world alone.", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 28},
        {'user': user48, 'dob': '1993-09-19', 'gender': "N", 'bio': "Your smile is like a sunrise, it sets the clouds on fire. But just being with you, is what I always admire.", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 5", 'looking_for': "F", 'course_id': 15},
        {'user': user49, 'dob': '1992-07-09', 'gender': "M", 'bio': "Love is the triumph of imagination over intelligence.", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 5", 'looking_for': "N", 'course_id': 18},
        {'user': user50, 'dob': '1991-06-19', 'gender': "F", 'bio': "I love you with all my butt, I would say heart, but my butt is bigger.", 'year_in': "MPhil", 'location': 'Glasgow', 'library_floor': "Level 5", 'looking_for': "N", 'course_id': 21},
        {'user': user51, 'dob': '1986-03-16', 'gender': "F", 'bio': "I don't have a library card, but do you mind if I check you out?", 'year_in': "1st Year", 'location': 'Paisley', 'library_floor': "Level 2", 'looking_for': "N", 'course_id': 19},            
        {'user': user52, 'dob': '1976-05-16', 'gender': "F", 'bio': "We go together like copy and paste.", 'year_in': "4th Year", 'location': 'Paisley', 'library_floor': "Level 3", 'looking_for': "N", 'course_id': 11},
        {'user': user53, 'dob': '1997-09-16', 'gender': "F", 'bio': "Roses are red, violets are blue, I'm counting the days until I can finally see you...", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 3", 'looking_for': "N", 'course_id': 17},   
        {'user': user54, 'dob': '1997-04-16', 'gender': "N", 'bio': "My heart and I agree... You're the only one for me.", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 4", 'looking_for': "F", 'course_id': 26},
        {'user': user55, 'dob': '1994-08-22', 'gender': "N", 'bio': "I wanna be your girlfriend more than an electron wants to attach to a proton.", 'year_in': "4th Year", 'location': 'East Kilbride', 'library_floor': "Level 4", 'looking_for': "F", 'course_id': 26},
        {'user': user56, 'dob': '1981-06-26', 'gender': "M", 'bio': "Now I understand why we can't be together. Because God does not want us to have the perfect life.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 8", 'looking_for': "N", 'course_id': 2},            
        {'user': user57, 'dob': '1988-05-26', 'gender': "M", 'bio': "There are many fish in the sea but you will always be my Nemo.", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 9", 'looking_for': "N", 'course_id': 4},
        {'user': user58, 'dob': '1990-09-19', 'gender': "M", 'bio': "Being in love is like living in a cheesy little love song...", 'year_in': "Masters", 'location': 'Stepps', 'library_floor': "Level 9", 'looking_for': "N", 'course_id': 25},
        {'user': user59, 'dob': '1994-01-09', 'gender': "N", 'bio': "If kisses were snowflakes, I'd send you a blizzard", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 4", 'looking_for': "M", 'course_id': 18},
        {'user': user60, 'dob': '1993-09-19', 'gender': "N", 'bio': "If I can be with you in my dreams, I would sleep forever..", 'year_in': "PHD", 'location': 'Milngavie', 'library_floor': "Level 5", 'looking_for': "M", 'course_id': 15},
    ]

    societies = Society.objects.all()
    interests = Interest.objects.all()

    for profile_data in profiles:
        p = add_profile(profile_data['user'], profile_data['dob'], profile_data['gender'], profile_data['bio'], profile_data['year_in'],
            profile_data['location'], profile_data['library_floor'], profile_data['looking_for'], profile_data['course_id'])
        
        p.societies.clear() # remove all existing societies from the user's profile
        p.interests.clear() # remove all existing interests from the user's profile
        
        # add profile's societies
        socs = []
        while len(socs) < 5:
            choice = random.choice(societies) 
            if choice not in socs:
                socs.append(choice)
        p.societies.add(*socs)

        # add profile's interests
        intrs = []
        while len(intrs) < 5:
            choice = random.choice(interests)
            if choice not in intrs:
                intrs.append(choice)
        p.interests.add(*intrs)

    profiles = Profile.objects.all()

    for profile in profiles:
        possible_matches = utils.get_discover_profiles(profile)
        for user_liked in possible_matches:
            if profile != user_liked:
                add_like(profile, user_liked)

    matches = Match.objects.all()

    for match in matches:
        add_message(match.profile1, match.profile2)

def add_like(profile, profile_liked):
    choice = random.randint(0, 3)   # 0: like, 1-3: no like object is created
    if choice == 0:
        like = Like.objects.get_or_create(profile=profile, profile_liked=profile_liked, is_liked=True)[0]
    
def add_profile(user, dob, gender, bio, year_in, location, library_floor, looking_for, course_id):
    profile = Profile.objects.get_or_create(user=user, dob=dob, gender=gender, bio=bio, year_in=year_in, 
            location=location, library_floor=library_floor, looking_for=looking_for, course_id=course_id)[0]
    return profile

def add_message(profile1, profile2):
    kafka = "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a \
            horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown \
            belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it \
            and seemed ready to slide off any moment. His many legs, pitifully thin compared with the size of the \
            rest of him, waved about helplessly as he looked. It wasn't a dream. His room, a proper human room although \
            a little too small, lay peacefully between its four familiar walls. A collection of textile samples lay spread \
            out on the table - Samsa was a travelling salesman - and above it there hung a picture that he had recently cut \
            out of an illustrated magazine and housed in a nice, gilded frame. It showed a lady fitted out with a fur hat and \
            fur boa who sat upright, raising a heavy fur muff that covered the whole of her lower arm towards the viewer. \
            Gregor then turned to look out the window at the dull weather. Drops of rain could be heard hitting the pane, \
            which made him feel quite sad. 'How about if I sleep a little bit longer and forget all this nonsense', he thought, \
            but that was something he was unable to do because he was used to sleeping on his right, and in his present state \
            couldn't get into that position. However hard he threw himself onto his right, he always rolled back to where he \
            was. He must have tried it a hundred times, shut his eyes so that he wouldn't have to look at the floundering legs, \
            and only stopped when he began to feel a mild, dull pain there that he had never felt before. 'Oh, God', he thought."
    kafka_tokens = kafka.split()

    for i in range(5):
        msg1, msg2 = '', ''
        while len(msg1) == 0 or len(msg2) == 0 or len(msg1) > 300 or len(msg2) > 300:
            start = random.randint(0, len(kafka_tokens)-5)
            middle = random.randint(start, len(kafka_tokens))
            end = random.randint(middle, len(kafka_tokens))
            msg1 = ' '.join(kafka_tokens[start:middle])
            msg2 = ' '.join(kafka_tokens[middle:end])

        Message.objects.create(sender=profile1, receiver=profile2, message=msg1)
        Message.objects.create(sender=profile2, receiver=profile1, message=msg2)

def add_societies():
    for society in SocietyChoices.ALL_CHOICES:
        Society.objects.get_or_create(society=society)

def add_interests():
    for interest in InterestChoices.ALL_CHOICES:
        Interest.objects.get_or_create(interest=interest)

def add_courses():
    for course in CourseChoices.ALL_CHOICES:
        Course.objects.get_or_create(course=course)


if __name__ == '__main__':
    print('Starting GLover population script...', end="")
    populate()
    print('DONE')