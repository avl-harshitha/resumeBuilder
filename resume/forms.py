from django import forms
from .models import ResDetails,UserLogin
from django.forms import ModelForm, Textarea

genderop = 'MALE','FEMALE','OTHERS'

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResDetails
        fields = '__all__'
        widgets = {
            'Summary': Textarea(attrs={'width':"100%", 'cols' : "70", 'rows': "10", }),
            'WorkSummary': Textarea(attrs={'width':"100%", 'cols' : "70", 'rows': "10", }),
            'SkillSummary' : Textarea(attrs={'width':"100%", 'cols' : "70", 'rows': "10", }),
            'HobbiesSummary' : Textarea(attrs={'width':"100%", 'cols' : "70", 'rows': "10", }),
            'EducationSummary' : Textarea(attrs={'width':"100%", 'cols' : "70", 'rows': "10", }),
        }
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = '__all__'
    

    