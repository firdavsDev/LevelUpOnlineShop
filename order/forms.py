from django import forms
from .models import Region, District
from order.models import Delivery


class CheckoutFormModel(forms.ModelForm):
    region = forms.ModelChoiceField(
        queryset=Region.objects.filter(is_active=True),
        empty_label="Select region",
        widget=forms.Select(attrs={"class": "form-select", "id": "id_region"})
    )

    district = forms.ModelChoiceField(
        queryset=District.objects.filter(is_active=True),
        empty_label="Select district",
        widget=forms.Select(attrs={"class": "form-select", "id": "id_district"})
    )
    street = forms.CharField(max_length=40)
    building = forms.CharField(max_length=3)
    house = forms.CharField(max_length=3)
    postal_code = forms.CharField(max_length=6)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()

    def save(self, order_obj):
        delivery_obj = Delivery.objects.create(
            order=order_obj,
            region = self.cleaned_data["region"],
            district = self.cleaned_data["district"],
            street = self.cleaned_data["street"],
            building = self.cleaned_data["building"],
            house = self.cleaned_data["house"],
            postal_code = self.cleaned_data["postal_code"],
            phone = self.cleaned_data["phone"],
            email = self.cleaned_data["email"]
            )
        
    class Meta:
        model = Delivery
        fields = ("region", "district", "street", "building", "house", "postal_code", "phone", "email")
        labels = {
            "region": "Region",
            "district": "District",
            "street": "Street",
            "building": "Building",
            "house": "House",
            "postal_code": "Postal Code",
            "phone": "Phone",
            "email": "Email"
        }
        widgets = {
            "region": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your region"}
            ),
            "district": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your district"}
                ),
            "street": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your street"}
                ),
            "building": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter your building"}
                ),
            "house": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter your house"}
                ),
            "postal_code": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter your postal_code"}
                ),
            "phone": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter your phone"}
                ),
            "email": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
                ),
        }
        error_css_class = "danger"