from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
import uuid
from django.db import models
from django.utils import timezone
from django_mongoengine import Document, fields
import datetime

# class ChatInvite(models.Model):
#     CHOICES = (
#         ('pending', 'Pending'),
#         ('accepted', 'Accepted'),
#         ('rejected', 'Rejected'),
#         ('blocked', 'Blocked')
#     )
#     sender_id = models.IntegerField(verbose_name=_(u'Sender ID'), blank=False, null=False, default=0)
#     recipient_id = models.IntegerField(verbose_name=_(u'Recipient ID'), blank=False, null=False, default=0)
#     invite_id = models.UUIDField(verbose_name=_(u'Chat Invitation ID'), primary_key=True, blank=False, null=False,
#                                  default=uuid.uuid4, editable=False)
#     created_at = models.DateTimeField(verbose_name=_(u'Invited date'), auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name=_(u'Updated date'), auto_now_add=True)
#     status = models.CharField(default='pending', choices=CHOICES, max_length=10)


class ChatInvite(Document):
    CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('blocked', 'Blocked')
    )
    sender_id = fields.StringField(verbose_name=_(u'Sender ID'), blank=False, null=False, default=0)
    recipient_id = fields.StringField(verbose_name=_(u'Recipient ID'), blank=False, null=False, default=0)
    invite_id = fields.StringField(verbose_name=_(u'Chat Invitation ID'), primary_key=True, blank=False, null=False,
                                      default=uuid.uuid4, editable=False)
    created_at = fields.DateTimeField(verbose_name=_(u'Invited date'), default=datetime.datetime.now, required=True,
                                      editable=False,)

    updated_at = fields.DateTimeField(verbose_name=_(u'Updated date'), default=datetime.datetime.now, required=True,
                                      editable=False,)
    status = fields.StringField(default='pending', choices=CHOICES, max_length=10)

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

    def __unicode__(self):
        return self.label

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}