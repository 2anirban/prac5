from django.forms import ModelForm
from django import forms


class blogform1(ModelForm):
    class Meta:
        fields=["author1","title1","body1","image1"]

class commentform1(ModelForm):
    class Meta:
        field=["comment1","comment_name1"]


