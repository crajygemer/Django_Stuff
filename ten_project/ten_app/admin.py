from django.contrib import admin
from ten_project.ten_app.models import Topic, Webpage, AccessRecord, Categories
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Categories)
