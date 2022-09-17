from django.forms import ModelForm
from .models import Reason

class ReasonForm(ModelForm):
    class Meta:
        model = Reason
        fields = ['date', 'occasion'] 