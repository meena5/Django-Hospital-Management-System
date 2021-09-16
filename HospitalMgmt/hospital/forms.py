from django.forms import ModelForm
from hospital.models import *
class Addoctorform(ModelForm):
    class Meta:
        model=Doctor
        fields=['name','mobile_no','specialization']
