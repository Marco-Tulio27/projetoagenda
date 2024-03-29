from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone',)
    ordering = 'id',
    list_filter = ('created_date',)
    list_per_page = 10
    search_fields = ('id',)