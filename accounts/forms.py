from django import forms
from .models import CustomUser, Region, District, Profile

from django.utils import timezone
from datetime import timedelta


class SimpleLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    # add class to email field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Email Address"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        # check password length
        if len(password) < 8:
            self.add_error("password", "Password must be at least 8 characters long")
        # check if email is valid
        if not email.endswith("@gmail.com"):
            self.add_error("email", "Email must be gmail")

        return cleaned_data


class RegistarForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter First Name"}
        )
        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter Last Name"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Email Address"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Retry Password"}
        )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        # check password length
        if len(password1) < 8:
            self.add_error("password1", "Password must be at least 8 characters long")
        # check passwords
        if password1 != password2:
            self.add_error("password2", "Password is incorrect")
        # check if email already exists
        user = CustomUser.objects.filter(email=email)
        if user:
            self.add_error("email", "Email is already taken")
        # check if email is valid
        if not email.endswith("@gmail.com"):
            self.add_error("email", "Email must be gmail")

        return cleaned_data
    

    def save(self):
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        email = self.cleaned_data["email"]
        password1 = self.cleaned_data["password1"]

        user_obj = CustomUser.objects.create_user(
            email=email,
            password=password1,
            username=email,
            first_name=first_name,
            last_name=last_name,
        )
        return user_obj
    

class UpdateProfileFormModel(forms.ModelForm):
    region = forms.ModelChoiceField(
        queryset=Region.objects.filter(is_active=True),
        empty_label="Select region",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    district = forms.ModelChoiceField(
        queryset=District.objects.filter(is_active=True),
        empty_label="Select district",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    address = forms.CharField(max_length=40, initial="1234")
    birth_date = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
                               attrs={'type': 'date',
                                      'min': str((timezone.now() - timedelta(days=365)).date()),
                                      'max': str(timezone.now().date())
                                      }
                                ),
        input_formats=["%d/%m/%Y", "%Y-%m-%d"],
    )

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
        return profile

    class Meta:
        model = Profile
        fields = ("image", "region", "district", "address", "birth_date")
        labels = {
            "image": "Profile Image",
            "region": "Region",
            "district": "District",
            "address": "Address",
            "birth_date": "Tug'ligan sana",
        }
        widgets = {
            "region": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your region"}
            ),
            "district": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your district"}
                ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your address"}
                ),
            "birth_date": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter your birth_date"}
                ),
        }
        error_css_class = "danger"
