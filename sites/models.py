from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Atividade(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=100, verbose_name="Título da Atividade")
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='atividades/', blank=True, null=True)
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='rascunho')
    autor = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name='atividades'
    )

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
