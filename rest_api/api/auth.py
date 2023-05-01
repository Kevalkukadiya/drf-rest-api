from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BasicAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            raise AuthenticationFailed('Please provide username')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such User')
        return(user, None)


