from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('get_pair/', TokenObtainPairView.as_view(), name='get_token'),
    path('register/', views.RegistrationView.as_view(), name='register_acc'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('create_note/', views.CreationNoteView.as_view(), name='create_note'),
    path('get_notes/', views.GetNotesView.as_view(), name='get_notes'),
    path('update_note/<int:note_id>/', views.UpdateNoteView.as_view(), name='update_note'),
    path('delete_note/<int:note_id>/', views.DeleteNoteView.as_view(), name='delete_note')
]
