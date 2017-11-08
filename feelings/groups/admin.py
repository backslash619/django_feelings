from django.contrib import admin

from .models import Company, Family

# Register your models here.
# class GroupAdmin(admin.ModelAdmin):
#     readonly_fields = ("name",)
#

# admin.site.register(Group, GroupAdmin)
admin.site.register(Family)
admin.site.register(Company)
