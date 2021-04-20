from.models import product
from django import forms

class f(forms.ModelForm):
    class meta :
        model=product
        fields = ['name','item_id','price']
