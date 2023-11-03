from django.contrib import admin

from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id' ,'first_name', 'last_name', 'phone', 'email', 'created_date', 'description')
    #list_filter = ('created_date',)
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'description')
    ordering = ('created_date',)
    date_hierarchy = 'created_date'
    #list_editable = ('phone', 'email',)
    # fieldsets = (
    #     ('Informações', {
    #         'fields': ('first_name', 'last_name', 'phone', 'email')
    #     }),
    #     ('Descrição', {
    #         'fields': ('description',)
    #     }),
    # )
    
    

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = '-id',
