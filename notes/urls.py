from django.urls import path

from simplenotes.notes import views

from django.contrib.auth.decorators import login_required


urlpatterns = [
	    path('', login_required(views.IndexView.as_view()), name='notes'),
	    path('<int:id>/edit', login_required(views.NoteFormEditView.as_view()), name='note_update'),
	    path('<int:id>', login_required(views.ThatNote.as_view()), name='note'),
        path('about/', views.about, name='about'),
        path('create/', login_required(views.NoteFormCreateView.as_view()), name='create_note'),
        path('<int:id>/delete', login_required(views.NoteFormDestroyView.as_view()), name='note_destroy') 
]

