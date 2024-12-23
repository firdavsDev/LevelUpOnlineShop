from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from common.models import District, Region

from ..models import Profile
from ..forms import UpdateProfileFormModel

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
    initial = {
        'region': profile.region.id,
        'district': profile.district.id,
        'address': profile.address,
        'birth_date': profile.birth_date
    }

    profile_form = UpdateProfileFormModel(instance=profile, initial=initial)
    
    if request.method == "POST":
        profile_form = UpdateProfileFormModel(data=request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()

    context = {
        "profile_form": profile_form,
    }
    
    return render(request, "accounts/profile.html", context)



@login_required
def get_districts_by_region(request, region_id):
    districts = District.objects.filter(region_id=region_id).values("id", "name")
    return JsonResponse({"districts": list(districts)})