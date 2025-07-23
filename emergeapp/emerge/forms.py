from django import forms
from .models import Project

class ProjectCreate(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['student_name', 'year', 'semester', 'student_photo', 'project_photo', 'short_paper', 'project_name']