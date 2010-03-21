'''
Modeling single screencasts,
or other Video,
each with it's owner,
title, slug, description,
the file itself,
publish date and last updated datetime.
Tagging is supported if installed.
The models are GIS ready.
get_absolute_url with permalink is a must!
'''
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from django.conf import settings
if 'tagging' in settings.INSTALLED_APPS:
    from tagging.fields import TagField
else:
    TagField = None

class Video(models.Model):
    ''' A single video and metadata '''

    owner = models.ForeignKey('auth.User')

    title = models.CharField( max_length=255 )
    slug = models.SlugField( max_length=255, unique=True )
    description = models.TextField( blank=True )

    flash = models.FileField( upload_to='videos/flash', blank=True )
    lossless = models.FileField( upload_to='videos/lossless', blank=True )
    url = models.URLField( max_length=255, blank=True )

    published = models.DateTimeField( auto_now_add=True )
    updated = models.DateTimeField( auto_now=True )

    if TagField:
        tags = TagField()
    #objects = models.GeoManager()

    @models.permalink
    def get_absolute_url(self):
        return ('videos.views.detail', (), { 'slug': self.slug } )

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ( '-published', )

class VideoRelation(models.Model):
    ''' Generic M2M between Videos and other objects '''

    video = models.ForeignKey(Video)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    #objects = models.GeoManager()

    def __unicode__(self):
        return '%s <--> %s' % ( self.video, self.content_object )

def get_videos_for_object(obj):
    ''' takes an object and returns qs of related Videos.

    '''
    ct = ContentType.objects.get_for_model(obj)
    id = obj.id
    vs = VideoRelation.objects.filter( content_type=ct, object_id=id )

    return [ v.video for v in vs ]
