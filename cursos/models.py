from django.db import models

# Create your models here.


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True  # nao vai aparecer no BD


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)  # cada url tem que ser unica

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']  # para ordernar a paginacao por id, tem que ter isso!! Pode ser -id para ter ordem descrescente

    def __str__(self) -> str:
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(
        Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(
        max_digits=2, decimal_places=1)  # permites notas como 4.8

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
        unique_together = ['email', 'curso']  # um email so pode avaliar apenas uma vez o curso e utiliza isso, eles devem ser unicos
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.nome} avaliou o curso {self.curso} com a nota {self.avaliacao}'
