from django.contrib import admin
from videos.models import Video, VideoRelation

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Video, VideoAdmin)
admin.site.register(VideoRelation)

