from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import TestCase
from ..serializers.test_case_serializer import TestCaseSerializer

class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user) 