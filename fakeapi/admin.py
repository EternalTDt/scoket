from django.contrib import admin
from .models import FirstLevelCategory, SecondLevelCategory, ThirdLevelCategory

admin.site.register(FirstLevelCategory)
admin.site.register(SecondLevelCategory)
admin.site.register(ThirdLevelCategory)
