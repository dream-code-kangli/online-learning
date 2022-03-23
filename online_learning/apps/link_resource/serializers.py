from rest_framework import serializers
from .models import LinkResource, Tag


class LinkResourceRelatedField(serializers.RelatedField):

    def to_representation(self, value):
        return {'name', value.name}


class TagSerializer(serializers.ModelSerializer):

    # link_resources = LinkResourceRelatedField(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'


class LinkResourceSerializer(serializers.ModelSerializer):

    tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LinkResource
        fields = '__all__'
