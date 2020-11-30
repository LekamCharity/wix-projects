from django.urls import path

urlpatterns=[
    path('profile',views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
