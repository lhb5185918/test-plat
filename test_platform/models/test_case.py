from django.db import models
from django.contrib.auth.models import User

class TestCase(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    test_script = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', '草稿'),
            ('active', '激活'),
            ('deprecated', '废弃')
        ],
        default='draft'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name 