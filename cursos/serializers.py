from rest_framework import serializers
from .models import Avaliacao, Curso
from django.db.models import Avg  # average - media


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
        
    def validate_avaliacao(self, valor): # tem que ter o underline para validar, ex validate_email
        if valor in range(1,6):
            return valor
        raise serializers.ValidationError('A avaliacao PRECISA ser de 1 a 5!!!')


class CursoSerializers(serializers.ModelSerializer):

    # avaliacoes = AvaliacaoSerializers(
    #     many=True, read_only=True)  # Nested Relationship, vai colocar cada dados relacionado junto, mas com todas as infos
    
    #para melhorar o trafico de dados - recomendacao para API fast, so os necessarios e oferece para acesso
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')  # Hyperlinked Related Field/tem que ter o detail no nome

    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # para trazer mais performace, se tiver centenas de dados, utilize esse!
    
    media_avaliacoes = serializers.SerializerMethodField()  # e o valor dele gerado por uma funcao, comeca com get seguido com underline


    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes',
        )
        
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')  # dois underlines, se tiver muitos dados, melhor criar no models
        
        if media is None:
            return 0
        # return round(media *2)/2
        return round(media, 2)