from django.test import TestCase

from glover.models import *
from glover.utils import get_discover_profiles, get_matches
from .test_helpers import populate


class ProfileTests(TestCase):
    
    def setUp(self):
        # create users/profiles
        populate()

    def test_get_discover_profiles(self):
        """ Tests the utils.get_discover_profiles method returns correct profiles """
        jessica = Profile.objects.get(user__username='jessica')
        discovery_profiles = get_discover_profiles(jessica) # call the function
        self.assertEqual(len(discovery_profiles), 3)

        # create a new like and a new dislike to ensure the profiles are removed from the discovery list
        Like.objects.create(profile=jessica, profile_liked=discovery_profiles[0], is_liked=True)
        self.assertEqual(len(get_discover_profiles(jessica)), 2)
        Like.objects.create(profile=jessica, profile_liked=discovery_profiles[1], is_liked=False)
        self.assertEqual(len(get_discover_profiles(jessica)), 1)

        # change existing user's gender and preference to ensure function updates correctly
        greta = Profile.objects.get(user__username='greta')
        greta.gender = 'M'
        greta.looking_for = 'F'
        greta.save()
        self.assertEqual(len(get_discover_profiles(jessica)), 2)

        # test another user
        bob = Profile.objects.get(user__username='bob')
        discovery_profiles = get_discover_profiles(bob)
        self.assertEqual(len(discovery_profiles), 1)

        # change gender of match to ensure it is removed
        discovery_profiles[0].gender = 'F'
        discovery_profiles[0].save()
        discovery_profiles = get_discover_profiles(bob)
        self.assertEqual(len(discovery_profiles), 0)

    def test_get_matches(self):
        NUM_MATCHES_EXPECTED = 3
        jessica = Profile.objects.get(user__username="jessica")
        profiles = Profile.objects.exclude(user__username="jessica")[:NUM_MATCHES_EXPECTED]

        for profile in profiles:
            Like.objects.create(profile=jessica, profile_liked=profile, is_liked=True)
            Like.objects.create(profile=profile, profile_liked=jessica, is_liked=True)

        matches = get_matches(jessica)
        self.assertEqual(len(matches), NUM_MATCHES_EXPECTED)

    def test_two_likes_create_match(self):
        jessica = Profile.objects.get(user__username="jessica")
        jack = Profile.objects.get(user__username="jack")

        self.assertEqual(Match.objects.count(), 0)

        Like.objects.create(profile=jessica, profile_liked=jack, is_liked=True)
        Like.objects.create(profile=jack, profile_liked=jessica, is_liked=True)

        self.assertEqual(Match.objects.count(), 1)

    def test_two_dislikes_dont_create_match(self):
        jessica = Profile.objects.get(user__username="jessica")
        jack = Profile.objects.get(user__username="jack")

        self.assertEqual(Match.objects.count(), 0)

        Like.objects.create(profile=jessica, profile_liked=jack, is_liked=False)
        Like.objects.create(profile=jack, profile_liked=jessica, is_liked=False)

        self.assertFalse(Match.objects.count(), 1)

    def test_delete_user_cascades(self):
        jessica = Profile.objects.get(user__username="jessica")
        jack = Profile.objects.get(user__username="jack")

        # create likes (and match) between users
        Like.objects.create(profile=jessica, profile_liked=jack, is_liked=True)
        Like.objects.create(profile=jack, profile_liked=jessica, is_liked=True)

        Message.objects.create(sender=jessica, receiver=jack, message="hi I've just matched you")
        Message.objects.create(sender=jack, receiver=jessica, message="hi")
        Message.objects.create(sender=jessica, receiver=jack, message="hi")

        msgs = Message.objects.filter(Q(sender=jessica) | Q(receiver=jessica))
        self.assertEquals(msgs.count(), 3)

        likes = Like.objects.filter(Q(profile=jessica) | Q(profile_liked=jessica)).count()
        matches = get_matches(jessica)
        self.assertEquals(len(matches), 1)

        # now delete user and check that likes, matches and messages cascade
        jack.delete()
        msgs = Message.objects.filter(Q(sender=jessica) | Q(receiver=jessica))
        self.assertEquals(msgs.count(), 0)

        likes_after_delete = Like.objects.filter(Q(profile=jessica) | Q(profile_liked=jessica)).count()
        self.assertEquals(likes_after_delete, likes-2)

        matches = get_matches(jessica)
        self.assertEquals(len(matches), 0)