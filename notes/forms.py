from django.forms import ModelForm
from .models import Note


class NoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(size='79')
        self.fields['body'].widget.attrs.update(rows='19', cols='79')

    class Meta:
        model = Note
        fields = ['title', 'body']
        labels = {'title': '', 'body': ''}
        
 
