from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import JSONRenderer

from .serializers import NotesSerializer, RegisterUserSerializer
from .models import Notes


class RegistrationView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RegisterUserSerializer


#Notes
class CreationNoteView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = NotesSerializer

    def post(self, request):
        title = request.data.get('title', None)
        discription = request.data.get('discription', None)
        if not title:
            return Response({'status': 'Title is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        note = Notes(title=title, discription=discription, user=request.user)
        note.save()
        return Response({'status': 'success'})


class GetNotesView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        notes = Notes.objects.filter(user_id=request.user.pk)
        notes = [NotesSerializer(note).data for note in notes]
        notes = JSONRenderer().render(notes)
        return Response(notes)
    

class UpdateNoteView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = NotesSerializer

    def post(self, request, note_id):
        note = Notes.objects.get(pk=note_id)
        if note.user_id != request.user.pk:
            return Response({'status': 'This note doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not note:
            return Response({'status': 'Note doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        title = request.data.get('title', None)
        discription = request.data.get('discription', None)

        if not title:
            return Response({'status': 'There is no title'}, status=status.HTTP_400_BAD_REQUEST)
        
        note.title = title
        note.discription = discription
        note.save()
        return Response({'status': 'success'})
    

class DeleteNoteView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, note_id):
        note = Notes.objects.get(pk=note_id)
        if note.user_id != request.user.pk:
            return Response({'status': 'This note doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not note:
            return Response({'status': 'Note doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        note.delete()
        return Response({'status': 'success'})
    



    




