from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from common.models import District, Region

from ..models import Profile

# from ..forms import ProfileForm


# allow ony authenticated users to access this view
@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    regions = Region.objects.all()
    districts = District.objects.all()
    context = {
        "profile": profile,
        "regions": regions,
        "districts": districts,
    }
    return render(request, "accounts/profile.html", context)


# TODO update profile view
