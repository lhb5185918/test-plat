from django.db import models
from django.contrib.auth.models import User
from .test_suite import TestSuite
from .test_case import TestCase

class TestReport(models.Model):
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE, null=True, blank=True)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE, null=True, blank=True)
    executed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    executed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pass', '通过'),
            ('fail', '失败'),
            ('error', '错误'),
            ('skip', '跳过')
        ]
    )
    result_data = models.JSONField()
    execution_time = models.FloatField()  # 执行时间（秒）
    
    class Meta:
        ordering = ['-executed_at']

    def __str__(self):
        return f"Report {self.id} - {self.status}" 