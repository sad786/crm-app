from django import forms
from .models import Customer, Interaction, Note

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['interaction_type', 'notes']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']