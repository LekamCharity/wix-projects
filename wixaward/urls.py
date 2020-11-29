from django.conf.urls import url,include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('users',views.UserViewSet)
router.register('posts',views.PostViewSet)
router.register('profile',views.ProfileViewSet)

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^api/',include(router.urls)),
    url(r'^(?P<username>\w+)/profile', views.user_profile, name='userprofile'),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^profile/(?P<username>\w+)/settings', views.edit_profile, name='edit'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^project/(?P<id>\d+)',views.project,name='project'),
    url(r'^search/$',views.search_project,name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
