from django.contrib.auth import get_user_model
from django.utils.timezone import now


class SetLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Update last activity after request finished processing
            get_user_model().objects.filter(pk=request.user.pk).update(last_activity=now())

        response = self.get_response(request)

        return response
