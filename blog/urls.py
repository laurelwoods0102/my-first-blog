from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Post', views.blogImage)

urlpatterns = [
    url('^$', views.post_list, name='post_list'),
    url(r'^api_root/', include(router.urls)),
]