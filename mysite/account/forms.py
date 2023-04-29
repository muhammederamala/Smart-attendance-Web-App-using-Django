from django import forms
from .models import add_class_model


# add class form references the add_class model

class add_class_form(forms.ModelForm):
    class Meta:
        model = add_class_model
        fields = ('subject','new_class','no_of_students')