from django.contrib import admin
from . import models
# Register your models here.

class ItemInLine(admin.TabularInline):
    model = models.Listitem
    extra = 2

class TemplateAdmin(admin.ModelAdmin):
    inlines = [ItemInLine]

admin.site.register(models.Template,TemplateAdmin)
admin.site.register(models.Copy)
admin.site.register(models.Listitemcopy)
