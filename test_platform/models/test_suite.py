from django.db import models
from django.contrib.auth.models import User
from .test_case import TestCase

class TestSuite(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    test_cases = models.ManyToManyField(TestCase)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name 