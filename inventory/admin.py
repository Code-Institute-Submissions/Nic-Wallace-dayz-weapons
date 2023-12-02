from django.contrib import admin
from .models import Weapon, Ammunition, Attachment, Category

admin.site.register(Ammunition)
admin.site.register(Attachment)
admin.site.register(Category)


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = (
        "name", "slug", "ammunition", "attachment", "category", "size", "weight",
        "damage", "is_public"
    )
    list_filter = (
        "ammunition__name", "attachment__name", "category__name", "damage", "is_public"
    )
    prepopulated_fields = {'slug': ('name',)}
