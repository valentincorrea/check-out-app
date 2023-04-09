from django import forms
from django.forms import ModelForm
from .models import Request

# Create a request form
# TODO: Fix the class to take all student's information
class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('student_first_name', 
                  'student_last_name', 
                  'student_email', 
                  'teacher_first_name', 
                  'teacher_last_name', 
                  'teacher_email', 
                  'computer_sn',
                  'os',
                  'computer_classification',
                  )
        labels = {
            'student_first_name': '', 
            'student_last_name': '', 
            'student_email':'', 
            'teacher_first_name': '', 
            'teacher_last_name': '', 
            'teacher_email':'', 
            'computer_sn':'If the serial number is 3, enter the number 3 in the field below',
            'os':'',
            'computer_classification':'',
        }

        widgets = {
            'student_first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Student's First Name"}), 
            'student_last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Student's Last Name"}), 
            'student_email': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Student's Email"}), 
            'teacher_first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Teacher's First Name"}), 
            'teacher_last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Teacher's Last Name"}), 
            'teacher_email': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Teacher's Email"}),
            'computer_sn': forms.TextInput(attrs={'class':'form-control', 'placeholder': "3"}),
            'os': forms.Select(attrs={'class':'form-select'}),
            'computer_classification': forms.Select(attrs={'class':'form-select', 'placeholder': "Computer ID"}),
        }

# Approved form
class ApproveForm(ModelForm):
    class Meta: 
        model = Request
        exclude = (
            'student_first_name', 
                  'student_last_name', 
                  'student_email', 
                  'teacher_first_name', 
                  'teacher_last_name', 
                  'teacher_email', 
                  'computer_sn',
                  'os',
                  'computer_classification',
        )
        fields = (
            'approved', 
            'comment',)
        labels = {
        'approved': 'Check the box to approve the request ', 
        'comment': 'Comments', 
        }
        widgets = {
            'approved': forms.CheckboxInput(attrs={'class':'form-check-input', 'placeholder': ''}), 
            'comment': forms.Textarea(attrs={'class':'form-control', 'rows':'3', 'placeholder': ''}), 
        }
        # fields = "__all__"
    # fields = (
    #     'approved', 
    #     'comment', 
    #     )
    

    # test form
    class TestForm(forms.Form):
        name = forms.CharField(max_length=255)
        email = forms.EmailField()
        message = forms.Textarea()
