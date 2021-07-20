
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,req):
        if not req.user.is_anonymous:
            if not req.user.is_staff:
                profile = req.user.profileuser
                if not profile.picture or not profile.biography:
                    if req.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')
        response = self.get_response(req)
        return response