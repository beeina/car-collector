from django.forms import ModelForm
from .models import Insurance

class InsuranceForm(ModelForm):
  class Meta:
    model = Insurance
    fields = ['policyNumber', 'provider', 'coverageAmount', 'startDate', 'endDate']

