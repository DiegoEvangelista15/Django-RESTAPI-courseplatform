

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializers, AvaliacaoSerializers


class CursoAPIView(APIView):
    """
    API de Cursos da Geek
    """

    def get(self, request):
        cursos = Curso.objects.all()
        # para passar todos os cursos, um so passa o parametro
        serializer = CursoSerializers(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):  # pegando os dados para criar as novas coisas
        # com isso a gente envia os dados, por isso o data
        serializers = CursoSerializers(data=request.data)
        # Para verificar se os dados sao validos, caso nao ele ja para ali e manda o erro
        serializers.is_valid(raise_exception=True)
        serializers.save()
        # depois de salvar ele manda a resposta
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """ 
    API de Avaliacoes da Geek
    """

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializers = AvaliacaoSerializers(avaliacoes, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = AvaliacaoSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
