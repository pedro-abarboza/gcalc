import json

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

from oauth2_provider.models import get_access_token_model
from oauth2_provider.views import TokenView as OAuth2TokenView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



class TokenView(OAuth2TokenView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_request(self):
        my_request = self.request.POST.copy()
        my_request['client_id'] = self.param.api_client_id
        my_request['client_secret'] = self.param.api_client_secret
        return my_request

    def post(self, request, *args, **kwargs):
        request.POST = self.set_request()
        response = super().post(request, *args, **kwargs)
        body = json.loads(response.content)

        access_token = body.get("access_token")
        if not access_token:
            response.status_code = 404
            return response

        token = get_access_token_model().objects.get(token=access_token)

        body["id_user"] = token.user.username
        body["color_primary"] = self.param.theme_color
        body["color_primary_rgb"] = self.param.theme_color_rgb
        body["color_secondary"] = self.param.theme_color_light
        body["color_secondary_rgb"] = self.param.theme_color_light_rgb
        response.content = json.dumps(body)
        return response