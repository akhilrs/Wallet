# from django_mongoengine import mongo_admin as admin
from wallet.chat.models import ChatInvite
from django.contrib import admin

# @admin.register(ChatInvite)
# class ChatInviteAdmin(admin.DocumentAdmin):
#     pass

@admin.register(ChatInvite)
class ChatInviteAdmin(admin.ModelAdmin):
    pass