from rest_framework import serializers
from ..models import TestCase

class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at') 