from django.contrib import admin
from .models import TestCase, TestSuite, TestReport, TestEnvironment

admin.site.register(TestCase)
admin.site.register(TestSuite)
admin.site.register(TestReport)
admin.site.register(TestEnvironment) 