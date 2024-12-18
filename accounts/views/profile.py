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


def update_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    regions = Region.objects.all()
    districts = District.objects.all()

    if request.method == "POST":
        region_id = request.POST.get("region")
        district_id = request.POST.get("district")
        address = request.POST.get("address")
        birth_date = request.POST.get("birth_date")
        print(region_id)

        region_obj = regions.get(id=region_id)
        district_obj = districts.get(id=district_id)
        profile.region = region_obj
        profile.district = district_obj
        profile.address = address
        profile.birth_date = birth_date
        profile.save()

    context = {
        "profile": profile,
        "regions": regions,
        "districts": districts,
    }
    return render(request, "accounts/profile.html", context)
