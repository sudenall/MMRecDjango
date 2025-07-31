from django import forms
from .models import CustomDataset

class CustomDatasetForm(forms.ModelForm):
    class Meta:
        model = CustomDataset
        fields = ['file']


    def clean_file(self):
        uploaded_file = self.cleaned_data.get('file')
        if not uploaded_file.name.endswith('.csv'):
            raise forms.ValidationError("❌ Please upload only files with a .csv extension.")
        return uploaded_file