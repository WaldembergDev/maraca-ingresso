from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Cliente
from .tasks import enviar_email_confirmacao_cadastro

@receiver(post_save, sender=Cliente)
def meu_receptor(sender, instance, created, **kwargs):
    if created:
        enviar_email_confirmacao_cadastro(instance.usuario.email, instance.usuario.first_name)