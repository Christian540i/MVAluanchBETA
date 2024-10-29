from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'insured', 'commercial_vehicle', 'fracture', 'rear_end', 'passenger', 'pedestrian'
        ]

        labels = {
            'insured': 'Were you insured?',
            'commercial_vehicle': 'Was it a commercial vehicle?',
            'fracture': 'Did you sustain a fracture?',
            'rear_end': 'Was it a rear-end collision?',
            'passenger': 'Were you a passenger?',
            'pedestrian': 'Were you a pedestrian?',
        }

        # Use RadioSelect widgets for Yes/No questions for better user experience
        widgets = {
            'insured': forms.RadioSelect(choices=[('Yes', 'Yes'), ('No', 'No')]),
            'commercial_vehicle': forms.RadioSelect(choices=[('Yes', 'Yes'), ('No', 'No')]),
            'fracture': forms.RadioSelect(choices=[('Yes', 'Yes'), ('No', 'No')]),
            'rear_end': forms.RadioSelect(choices=[('Yes', 'Yes'), ('No', 'No')]),
            'passenger': forms.RadioSelect(choices=[('Yes', 'Yes'), ('No', 'No')]),
            'pedestrian': forms.RadioSelect(choices=[('Yes', 'Yes'), ('No', 'No')]),
        }