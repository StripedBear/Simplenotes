from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import  get_object_or_404, redirect
from django.views import View
from .forms import NoteForm
from simplenotes.notes.models import Note


class IndexView(View):
    def get(self, request, *args, **kwargs):
        notes = Note.objects.filter(user=request.user)
        return render(request, 'notes/index.html', context={
                'notes': notes,})


class NoteFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = NoteForm(initial={'title': 'Title 1', 'body': 'Your note...'})
        notes = Note.objects.filter(user=request.user)
        return render(request, 'notes/create.html', {'form': form, 'notes': notes})
    
    def post(self, request, *args, **kwargs):
        form = NoteForm(request.POST)
        user_id = self.request.user.id
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.user_id = user_id
            newpost.save()
            return redirect('notes')
        return render(request, 'notes/create.html', {'form': form})
        
        
class ThatNote(View):
    def get(self, request, *args, **kwargs):
        user_id = self.request.user.id
        notes = Note.objects.filter(user_id=user_id)
        note = get_object_or_404(Note, id=kwargs['id'], user_id=user_id)
        return render(request, 'notes/show.html', context={'note': note, 'notes': notes})


class NoteFormEditView(View):

    def get(self, request, *args, **kwargs):
        user_id = self.request.user.id
        note_id = kwargs.get('id')
        note =  get_object_or_404(Note, id=kwargs['id'], user_id=user_id)
        form = NoteForm(instance=note)
        notes = Note.objects.filter(user=request.user)
        return render(request, 'notes/update.html', {'form': form, 'note_id': note_id, 'notes': notes})
        
    def post(self, request, *args, **kwargs):
        user_id = self.request.user.id
        note_id = kwargs.get('id')
        note = get_object_or_404(Note, id=kwargs['id'], user_id=user_id)
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')

        return render(request, 'notes/update.html', {'form': form, 'note_id': note_id})



class NoteFormDestroyView(View):
    
    def post(self, request, *args, **kwargs):
        user_id = self.request.user.id
        note_id = kwargs.get('id')
        note = get_object_or_404(Note, id=kwargs['id'], user_id=user_id)
        if note:
            note.delete()
        return redirect('notes')


def about(request):
    return render(request, 'home/about.html')

