from asyncore import read
from rest_framework import serializers
from .models import Avaliacao, Curso


class AvaliacaoSerializers(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',  # O email eh um campo sensivel, entao coloca como extra kwargs para solicitar apenas na criacao, de resto nao vai aparecer
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )


class CursoSerializers(serializers.ModelSerializer):

    # avaliacoes = AvaliacaoSerializers(
    #     many=True, read_only=True)  # Nested Relationship, vai colocar cada dados relacionado junto, mas com todas as infos
    
    #para melhorar o trafico de dados - recomendacao para API fast, so os necessarios e oferece para acesso
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')  # Hyperlinked Related Field/tem que ter o detail no nome

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # para trazer mais performace, se tiver centenas de dados, utilize esse!


    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
