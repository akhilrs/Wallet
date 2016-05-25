import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
import haikunator
from .models import Room
from .models import ChatInvite
from rest_framework.views import APIView
from rest_framework import status
from wallet.core.http import HttpHandler as http


class ChatInviteView(APIView):
    def post(self, request):
        try:
            invite = ChatInvite.objects.create(
                sender_id=request.data['sender'],
                recipient_id=request.data['recipient'],
            )
            invite.save()
            return http.json_response_wrapper([], 'Success', status.HTTP_200_OK)
        except Exception as e:
            return http.json_response_wrapper([], e.message, status.HTTP_200_OK)
