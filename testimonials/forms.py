from django import forms
from .models import Testimonies


RATINGS_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimonies
        fields = ('name', 'rating', 'description',)
        
    rating = forms.ChoiceField(choices=RATINGS_CHOICES)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'rating': "N/A",
            'description': 'Description',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False