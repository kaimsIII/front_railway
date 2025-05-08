from django.http import HttpResponse
from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

# Create your views here.

# Vista para la raíz
def bienvenida(request):
    return HttpResponse("¡Bienvenido a la API de Usuarios!")

# Crear un usuario
class CrearUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Obtener usuario por ID
class ObtenerUsuarioView(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'id_usuario'