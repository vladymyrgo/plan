from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Dream, Plan, Task, Idea


admin.site.unregister(Group)
admin.site.register(Dream)
admin.site.register(Plan)
admin.site.register(Task)
admin.site.register(Idea)
