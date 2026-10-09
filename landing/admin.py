from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Review, WorkExample, ContactRequest, SiteSettings


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('preview', 'title', 'price', 'order', 'is_active')
    list_editable = ('price', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'price')
        }),
        ('Иконка', {
            'fields': ('image', 'icon'),
            'description': 'Загрузите картинку. Emoji — запасной вариант, '
                           'если картинки нет.'
        }),
        ('Настройки вывода', {
            'fields': ('order', 'is_active')
        }),
    )

    @admin.display(description='Превью')
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:40px;width:40px;'
                'object-fit:contain;background:#f3f3f3;border-radius:6px;padding:3px;">',
                obj.image.url
            )
        return format_html('<span style="font-size:24px;">{}</span>', obj.icon)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'rating', 'created_at', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('rating', 'is_published')
    search_fields = ('name', 'text')


@admin.register(WorkExample)
class WorkExampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at', 'is_processed')
    list_editable = ('is_processed',)
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'phone', 'message')
    readonly_fields = ('name', 'phone', 'message', 'created_at')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass