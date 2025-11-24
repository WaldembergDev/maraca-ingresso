from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def enviar_email_confirmacao_cadastro(destinatario_email, nome_usuario):
    # 1. Definir o contexto para o template
    context = {
        'nome_usuario': nome_usuario,
    }

    # 2. Renderizar o template HTML para uma string
    html_content = render_to_string('emails/meu_email.html', context)
    
    # 3. Gerar a versão em texto simples (opcional)
    text_content = strip_tags(html_content) 

    # 4. Criar a mensagem de e-mail usando EmailMultiAlternatives
    email = EmailMultiAlternatives(
        # Assunto
        'Confirmação de Cadastro',
        # Conteúdo em texto simples
        text_content,
        # Remetente 
        settings.EMAIL_HOST_USER,
        # Destinatários
        [destinatario_email],
    )

    # 5. Anexar a versão HTML
    email.attach_alternative(html_content, "text/html")

    # 6. Enviar o e-mail
    email.send()
