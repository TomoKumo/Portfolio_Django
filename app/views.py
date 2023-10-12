from django.views.generic import View
from django.shortcuts import render
from .models import Profile, Technical


class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by("-id")[0]
            technical_data = Technical.objects.order_by("-id")
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'technical_data': technical_data
        })
