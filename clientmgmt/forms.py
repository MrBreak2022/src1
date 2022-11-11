from django import forms
from .models import Client

class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'category', 'contact_number'
     ]

    def clean_client_name(self):
         client_name = self.cleaned_data.get('client_name')
         if not client_name:
             raise forms.ValidationError('This field is required')

         for instance in Client.objects.all():
             if instance.client_name == client_name:
                 raise forms.ValidationError(str(client_name) + ' is already created')
         return client_name