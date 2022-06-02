
from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'bio', 'description', 'qualification',
         'institute', 'skils', 'contact', 'featured_image')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class':'input'}
        )
