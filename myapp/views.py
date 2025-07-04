from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

def superuser_required(view_func):
    return user_passes_test(lambda u: isinstance(u, User) and u.is_superuser)(view_func)

