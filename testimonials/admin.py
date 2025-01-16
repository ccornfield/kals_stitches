from django.contrib import admin

from .models import Testimonies

class TestimoniesAdmin(admin.ModelAdmin):
    readonly_fields = ('creator','name','date','description','rating',)

    fields = ('creator','name','date','description','rating',)

    list_display = ('creator','name','date','description','rating',)

    ordering = ('-date',)

admin.site.register(Testimonies, TestimoniesAdmin)


