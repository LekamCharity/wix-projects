from rest_framework  import serializers
from django.contrib.auth.models import User
from .models import Post,Profile


class ProfileSerializer(serializers.ModelSerializer):
    model = Profile
    fields = ['name','prof_picture','bio','location','contact']


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = ['id','title','description','technology','date','photo','user','url']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only = True)
    posts = PostSerializer(read_only = True,many=True)

    class Meta:
        model = User
        fields = ['id','url','username','profile','posts']
