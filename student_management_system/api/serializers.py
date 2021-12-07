from rest_framework import serializers
from api.models import User

class api_serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email_id', 'contact_number', 'permanent_address',
                  'education_qualification', 'active_status')