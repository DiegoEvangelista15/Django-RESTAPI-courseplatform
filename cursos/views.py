from rest_framework.generics import get_object_or_404
from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializers, AvaliacaoSerializers

from rest_framework import viewsets
# alterar acoes dentro do nosso model view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions

from .permissions import IsSuperUser


"""
API V1
"""

# so isso substitui todo o conteudo, pega todos os dados para ler criar


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers


# esse para atualizar e deletar mas precisa ser um portanto precisa do IP
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))

        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,  # se ele atender a requisicao, ele vai para o proximo
         permissions.DjangoModelPermissions,)  # tem que ter a virgula porque eh uma tupla
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers

    # coloca o decorator para criar uma nova rota, e ai traz todas as avaliacoes do curso, true a rota
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size=1  # ai ele vai paginar em uma pagina a parte de cada avaliacao de cada curso
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)
        
        if page is not None:
            serialiazer = AvaliacaoSerializers(page, many=True)
            return self.get_paginated_response(serialiazer.data)  # para pegar se exsite e passando para paginazao
        
        
        # curso = self.get_object()
        # pegando do models, e pgando todas as avalicoes desse curso
        serialiazer = AvaliacaoSerializers(avaliacoes, many=True)
        return Response(serialiazer.data)

# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializers


class AvaliacaoViewSet(mixins.CreateModelMixin,  # isso eh exatamente o de cima, desta forma podemos ver para personalizar, mesma coisa que ModelViewset
                       mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializers
