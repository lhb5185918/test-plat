from django.apps import AppConfig

class TestPlatformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_platform'
    verbose_name = '测试平台' 