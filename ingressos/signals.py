from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import HistoricoCompra
from .tasks import enviar_notificacao
from datetime import datetime
from django.conf import settings

@receiver(post_save, sender=HistoricoCompra)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        numero = settings.NUMERO_NOTIFICACAO
        evento = instance.titulo
        data_evento = datetime.strftime(instance.data_horario_evento, "%d/%m/%Y %H:%M")
        enviar_notificacao.delay(numero, evento, data_evento)