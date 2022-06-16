from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from django.utils import timezone


class MyBackend(ModelBackend):
    print('This is something')

    def get_user(self, user_id):

        try:
            user = get_user_model().objects.get(pk=user_id)
            user.last_online = timezone.now()
            print('This is something', user.last_online)
            user.save(update_fields=['last_online'])
            return user
        except get_user_model().DoesNotExist:
            return None
