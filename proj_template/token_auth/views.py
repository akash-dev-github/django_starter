from django.contrib.auth.models import User, Group
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from token_auth.serializers import UserSerializer, GroupSerializer
from rest_framework import permissions, viewsets, schemas, response


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [OpenAPIRenderer, SwaggerUIRenderer]


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Example APIs')
    return response.Response(generator.get_schema(request=request))
