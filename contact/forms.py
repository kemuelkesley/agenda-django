from contact.models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )
    
    

    # Quando eu quero validar varios campos
    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = forms.ValidationError('O primeiro nome não pode ser igual ao segundo', code='invalid')

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        #print(cleaned_data)
        return super().clean()


    # Quando eu quero validar apenas um campo
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        print(first_name)

        if first_name == 'ABC':
            #raise forms.ValidationError('Não digite ABC nesse campo')
            self.add_error(
            'first_name',
            forms.ValidationError(
                'Veio do ADD errors',
                code='invalid'
            )
        )


        return first_name