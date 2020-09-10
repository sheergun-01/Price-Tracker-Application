from django import forms

class AddNewItemForm(forms.Form):
    url = forms.CharField(max_length=600)
    budget_price = forms.IntegerField()
    # email = forms.EmailField()