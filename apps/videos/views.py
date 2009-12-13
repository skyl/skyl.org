from random import choice

from django.views.generic.list_detail import object_detail, object_list
from django.views.generic.create_update import create_object, update_object
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from videos.models import Video
from videos.forms import VideoForm, VideoFormPriv




def list(request):
    ''' Display the list of videos

    http://docs.djangoproject.com/en/dev/ref/generic-views/#notes-on-pagination
    In addition to the videos_list and whatever we add to locals, the view will
    paginated videos by 5.  The page can be by GET variable.
    In the template we can then do something like::

        {% if is_paginated %}
            {% if page_obj.has_previous %}
                <a href="{% url videos_list %}">FIRST</a>
                <a href="
                    {% url videos_list %}?page={{page_obj.previous_page_number}}">
                    PREVIOUS
                </a>
            {% endif %}
            {% if page_obj.has_next %}
                <a href="
                    {% url videos_list %}?page={{page_obj.next_page_number}}">
                    NEXT
                </a>
                <a href="{% url videos_list %}?page=last">LAST</a>
            {% endif %}
        {% endif %}
    '''
    return object_list(request,
            queryset = Video.objects.all(),
            paginate_by = 5,
            template_object_name = "video", # so render {{video_list}}
            extra_context = locals()
    )

def detail(request, slug):
    ''' Display the video and allow the user to interact with it '''

    video = get_object_or_404( Video, slug=slug )

    return object_detail(request,
            queryset = Video.objects.all(),
            object_id = video.id,
            #slug = slug,
            #slug_field = 'slug',
            template_object_name = 'video', # {{video.attr}}
            extra_context = locals(),
    )

@login_required
def add(request):
    ''' Allows the logged-in user to add videos to the site '''

    perm = request.user.has_module_perms('videos')

    if request.method == 'POST':
        if perm:
            form = VideoFormPriv(request.POST, request.FILES)
        else:
            form = VideoForm(request.POST)

        if form.is_valid():
            v = form.save( commit=False )
            v.owner = request.user

            # stupid hack to get a unique slug
            if not Video.objects.filter( slug=slugify(v.title) ):
                v.slug = slugify(v.title)
            else:
                v.slug = slugify(v.title) + '-' +\
                        ''.join([choice('skyl-org') for i in range(8)])

            v.save()
            return HttpResponseRedirect( reverse('videos_list') )

    return create_object(request,
        form_class = VideoFormPriv if perm else VideoForm,
        extra_context = locals()
    )

@login_required
def update(request, slug):
    ''' Allow the user to update videos that they own '''

    v = get_object_or_404( Video, slug=slug )

    if not v.owner == request.user:
        return HttpResponseRedirect( reverse('videos_list') )

    perm = request.user.has_module_perms('videos')

    return update_object(request,
        form_class = VideoFormPriv if perm else VideoForm,
        slug_field = 'slug',
        slug = slug,
        #post_save_redirect = reverse( 'videos_list' ),
        extra_context = locals()
    )

