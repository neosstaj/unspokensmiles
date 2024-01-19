from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


class User_Settings_Form(ModelForm):
   class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        help_texts = {
            'username': '',
        }
   def __init__(self, *args, **kwargs):
        super(User_Settings_Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-3'



class Password_Change_Form(PasswordChangeForm):
   class Meta:
        model = User
        fields = 'password'
   def __init__(self, *args, **kwargs):
        super(Password_Change_Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-3'    
