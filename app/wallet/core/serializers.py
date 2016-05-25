"""
===========
Serializers
===========
"""

from rest_framework import serializers as rf_serializers
from django.db.models import ForeignKey


class ExSerializer(rf_serializers.Serializer):
    """
    Base serializer that adds a feature of dynamically allow selection fields in response.
    """

    def __init__(self, *args, **kwargs):
        _fields = kwargs.pop('fields', None)
        super(ExSerializer, self).__init__(*args, **kwargs)

        # Dynamically allow selection of fields
        try:
            fields = self.context.get('request').GET.get('fields')
        except AttributeError:
            fields = _fields
        if fields:
            if isinstance(fields, basestring):
                fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ExModelSerializer(rf_serializers.ModelSerializer, ExSerializer):
    """
    Base serializer for model
    """

    def __init__(self, *args, **kwargs):
        super(ExModelSerializer, self).__init__(*args, **kwargs)
        meta = getattr(self, 'Meta', None)

        # Update the error messages specified under the Meta class for each fields
        for field_name, err_msgs in getattr(meta, 'error_messages', {}).iteritems():
            self.fields[field_name].error_messages.update(**err_msgs)

    @property
    def validated_data(self):
        """
        Overridden method to inject logged in user object to validated_data dict
        """
        validated_data = super(ExModelSerializer, self).validated_data

        if getattr(self.Meta.model, 'user', None):
            validated_data['user'] = self.context['request'].user

        return validated_data

    def build_relational_field(self, field_name, relation_info):
        field_class, field_kwargs = super(ExModelSerializer, self).build_relational_field(
            field_name, relation_info
        )

        # To override the queryset returned by the serializer to support enum field
        model_field = relation_info.model_field
        limit_choices_to = model_field.get_limit_choices_to()
        if isinstance(model_field, ForeignKey) and limit_choices_to:
            qs = field_kwargs.get('queryset')
            if qs:
                qs = qs.filter(**limit_choices_to)
                field_kwargs['queryset'] = qs

        return field_class, field_kwargs
