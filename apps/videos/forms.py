from django.forms import ModelForm

from videos.models import Video

class VideoForm(ModelForm):

    class Meta:
        exclude = ('owner', 'flash', 'lossless', 'slug' )
        model = Video

class VideoFormPriv(ModelForm):

    class Meta:
        exclude = ('owner', 'slug')
        model = Video


