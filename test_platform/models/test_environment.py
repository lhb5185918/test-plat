from django.db import models

class TestEnvironment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    base_url = models.URLField()
    variables = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name 