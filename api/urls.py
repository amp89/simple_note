from django.urls import path
from django.urls import include
from api import views

urlpatterns = [
    path("note/<int:note_id>", views.NoteView.as_view(), name='note'),
    path("note/", views.NoteView.as_view(), name='note'),
    
]
