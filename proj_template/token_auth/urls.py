from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from token_auth.views import UserViewSet, GroupViewSet, schema_view

admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^dot/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url('^swagger/', schema_view),

    url(r'^', include(router.urls)),
]
