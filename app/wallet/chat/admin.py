from django_mongoengine import mongo_admin as admin
from wallet.chat.models import ChatInvite


@admin.register(ChatInvite)
class ChatInviteAdmin(admin.DocumentAdmin):
    pass
