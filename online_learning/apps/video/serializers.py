from rest_framework import serializers
from .models import Video

from user.serializers import Profile


class VideoSerializers(serializers.ModelSerializer):
    author = Profile()

    class Meta:
        model = Video
        fields = ['id','title', 'ctime', 'mtime','path', 'views', 'praise_num', 'author']