from django.contrib import admin

from glover.models import Like, Match, Profile, Course, Interest, Society, Message


# Register your models here.
class LikeAdmin(admin.ModelAdmin):
    list_display = ('profile', 'profile_liked', 'is_liked')

class MatchAdmin(admin.ModelAdmin):
    list_display = ('profile1', 'profile2', 'time_matched')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'gender', 'looking_for', 'course', 'year_in', 'library_floor', 'location',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course',)

class InterestAdmin(admin.ModelAdmin):
    list_display = ('interest',)

class SocietyAdmin(admin.ModelAdmin):
    list_display = ('society',)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'message',)

admin.site.register(Like, LikeAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Society, SocietyAdmin)
admin.site.register(Message, MessageAdmin)
