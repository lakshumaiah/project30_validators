from django import forms

def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('name shuld not start with a ')


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a])
    age=forms.IntegerField()