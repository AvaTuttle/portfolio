from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "year", "image", "repository", "skill"]

        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Project Name", "class": "form-control"}),
            "description": forms.Textarea(attrs={"placeholder": "Description", "class": "form-control", "rows": 4}),
            "year": forms.NumberInput(attrs={"placeholder": "YYYY", "class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "repository": forms.URLInput(attrs={"placeholder": "GitHub Repository URL"}),
            "skill": forms.CheckboxSelectMultiple(),
        }
