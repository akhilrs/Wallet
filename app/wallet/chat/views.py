import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
import haikunator
from .models import Room
from rest_framework.views import APIView


class ChatInviteView(APIView):
    def post(self, request):
        try:
            pass
        except Exception as e:
            return e.message
