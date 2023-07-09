# -*- coding: utf-8 -*-

import django
import os
import sys

from datetime import timedelta
from collections import Counter
from django.utils import timezone


sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meL_backend.settings")
django.setup()


from account.models import User


users = User.objects.all()

for user in users:
    # Clear the suggestion list
    user.people_you_may_know.clear()

    for friend in user.friends.all():
        for ff in friend.friends.all():
            if ff not in user.friends.all() and ff != user:
                user.people_you_may_know.add(ff)