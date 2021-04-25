from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from rest_framework import status
from django.http import QueryDict

class APIAuthView(APIView):
    authentication_classes = [
            authentication.SessionAuthentication,
            # authentication.BasicAuthentication
        ]
    permission_classes = [permissions.IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        return super(__class__, self).dispatch(request, *args,**kwargs)


class NoteView(APIAuthView):
    def get(self, request, note_id=None, *args, **kwargs):
        if note_id:
            note = Note.objects.get(id=note_id, user=request.user)
            res =  NoteSerializer(note).data
            return Response(res)
        else:
            notes = Note.objects.filter(user=request.user)
            res = NoteSerializer(notes, many=True).data
            return Response(res)

    def post(self, request, *args, **kwargs):
        request_body = request.data
        Note.objects.create(user=request.user, content=request_body['content'])
        return Response({})

    def patch(self, request, note_id, *args, **kwargs):
        request_body = request.data
        note = Note.objects.get(id=note_id, user=request.user)
        note.content = request_body['content']
        note.save()
        return Response({})

    def delete(self, request, note_id, *args, **kwargs):
        note = Note.objects.get(id=note_id, user=request.user)
        note.delete()
        return Response({})      

    
