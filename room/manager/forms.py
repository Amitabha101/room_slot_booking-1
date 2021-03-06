from django.forms import ModelForm
from .models import add
from django import forms

# addform 
class AddForm(ModelForm):
  class Meta:
    model = add
    # fields='__all__'
    fields=['room_no','days','check_in_time','check_out_time']
    widgets={
      # room_no 
      'room_no':forms.NumberInput(
        attrs={'class':'form-control','placeholder':"room no"}
        ),

        # days
      'days':forms.NumberInput(
        attrs={'class':'form-control input','placeholder':"days"}
        ),


          # check_in_time
      'check_in_time':forms.TimeInput(
        attrs={
          'class':'form-control picker_time',
          'placeholder':"hour:min",
          },
          format="%H:%M"),

          # check_out_time
        'check_out_time':forms.TimeInput(
        attrs={
          'class':'form-control picker_time',
          'placeholder':"hour:min",
          },
          format="%H:%M"),
    }

# update form 
class UpdateForm(ModelForm):
  class Meta:
    model = add
    fields='__all__'
    widgets={
      # room_no 
      'room_no':forms.NumberInput(
        attrs={'class':'form-control','placeholder':"room no",'readonly': 'readonly'}
        ),

        # days
      'days':forms.NumberInput(
        attrs={'class':'form-control input','placeholder':"days"}
        ),


          # check_in_time
      'check_in_time':forms.TimeInput(
        attrs={
          'class':'form-control picker_time',
          'placeholder':"hour:min",
          },
          format="%H:%M"),


          # check_out_time
        'check_out_time':forms.TimeInput(
        attrs={
          'class':'form-control picker_time',
          'placeholder':"hour:min",
          },
          format="%H:%M"),
    }