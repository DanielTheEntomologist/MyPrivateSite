from django.contrib import admin

from website import models

# Register your models here.

admin.site.register(models.Author)
admin.site.register(models.CurriculumVitae)

from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "view_posts_link")

    def view_posts_link(self, obj):
        count = obj.post_set.count()

        url = (
            reverse("admin:website_post_changelist")
            + f"?category__id__exact="
            + f"{obj.id}"
        )
        return format_html('<a href="{}">{} Posts</a>', url, count)

    view_posts_link.short_description = "Posts"


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "view_category")
    list_filter = ["category"]

    def view_category(self, obj):
        category_name = obj.category.title

        # count = reverse("admin:core_category_changelist")
        url = (
            reverse("admin:website_category_changelist")
            + "?"
            + urlencode({"category__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, category_name)

    view_category.short_description = "Category"
