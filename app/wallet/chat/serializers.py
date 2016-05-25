from .models import ChatInvite
from wallet.core.serializers import ExModelSerializer
# from rest_framework import serializers


class ChatInviteSerializer(ExModelSerializer):

    class Meta:
        model = ChatInvite