from django.db import models
import uuid
from clientes.models import Cliente
from django.core.validators import MinValueValidator

# Create your models here.
class Ingresso(models.Model):
    class TipoIngresso(models.TextChoices):
        JOGO = 'JOGO', 'Jogo'
        SHOW = 'SHOW', 'Show'
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    tipo = models.CharField(max_length=5, choices=TipoIngresso.choices, default=TipoIngresso.JOGO)
    thumbnail = models.ImageField(blank=True, null=True)
    titulo = models.CharField(max_length=120, verbose_name='Título')
    local = models.CharField(max_length=120, verbose_name='Local do ingresso')
    descricao = models.CharField(max_length=255, verbose_name='Descrição do Ingresso')
    data_horario = models.DateTimeField()
    preco = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    estoque_disponivel = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.titulo

class HistoricoCompra(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    ingresso = models.ForeignKey(Ingresso, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=120, verbose_name='Título')
    local = models.CharField(max_length=120)
    data_compra = models.DateTimeField(auto_now_add=True)
    valor_pago = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.cliente.first_name}/{self.ingresso.titulo}'