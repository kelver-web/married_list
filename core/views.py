from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import GuestLoginForm, GuestRegisterForm

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from core.forms import ContactForm
from project import settings
from .models import ContactMessage, Gift, Reservation

# Create your views here.


def home(request):
    return render(request, 'core/index.html')

def gift_list(request):
    list_gifts = Gift.objects.all()
    return render(request, 'core/gift_list.html', {'gifts': list_gifts})


def our_love_story(request):
    return render(request, 'core/our_love_story.html')

def gallery(request):
    return render(request, 'core/gallery_area.html')


@login_required(login_url='guest_login')
def contact(request):
    return render(request, 'core/contact_area.html')


@login_required(login_url='guest_login')
def reserve_gift(request, gift_id):
    gift = get_object_or_404(Gift, id=gift_id)
    

    if gift.is_reserved:
        messages.warning(request, "Esse presente já foi reservado por outro usuário.")
    else:
        # Marca o presente como reservado
        gift.is_reserved = True
        gift.reserved_by = request.user
        gift.save()

        # Cria a reserva
        Reservation.objects.create(user=request.user, gift=gift)

        # Envia e-mail para os noivos
        assunto = f"🎁 Novo presente reservado: {gift.name}"
        mensagem = (
            f"Olá!\n\n"
            f"O convidado {request.user if request.user.is_authenticated else 'Um convidado'} "
            f"acabou de reservar o presente: {gift.name}.\n\n"
            f"Confira na sua lista de presentes."
        )

        send_mail(
            assunto,
            mensagem,
            None,  # usa DEFAULT_FROM_EMAIL configurado no settings.py
            ["Joyciarllianne@gmail.com", "Leonardosilvaferreira21@gmail.com"],  # e-mail dos noivos
        )

        # Envia e-mail de confirmação para o convidado
        assunto_convidado = "🎁 Confirmação de reserva de presente"
        mensagem_convidado = (
            f"Olá {request.user.username}!\n\n"
            f"Você reservou com sucesso o presente: {gift.name}.\n\n"
            f"Obrigado por participar da nossa celebração!"
        )
        send_mail(
            assunto_convidado,
            mensagem_convidado,
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=False
        )

        messages.success(request, "Presente reservado com sucesso! Um e-mail de confirmação foi enviado para você.")

    return redirect('gift_list')



@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            try:
                send_mail(
                    f"Contato: {contact_msg.subject}",
                    f"Mensagem de {contact_msg.name} ({contact_msg.email}):\n\n{contact_msg.message}",
                    settings.DEFAULT_FROM_EMAIL,
                    ["Joyciarllianne@gmail.com", "Leonardosilvaferreira21@gmail.com"],
                    fail_silently=False,
                )
            except Exception as e:
                return JsonResponse({'status': 'error', 'msg': 'Erro ao enviar e-mail.'}, status=500)

            return JsonResponse({'status': 'success', 'msg': 'Mensagem enviada com sucesso!'})
        else:
            return JsonResponse({'status': 'error', 'msg': 'Por favor corrija os erros no formulário.', 'errors': form.errors}, status=400)

    # GET normal: renderiza template com form
    form = ContactForm()
    return render(request, 'core/contact_area.html', {'form': form})


def guest_register(request):
    if request.method == 'POST':
        form = GuestRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # cria o usuário
            messages.success(request, "Cadastro realizado com sucesso! Agora faça login para reservar um presente.")
            return redirect('guest_login')  # <- manda para login
    else:
        form = GuestRegisterForm()
    return render(request, 'core/register.html', {'form': form})


def guest_login(request):
    if request.user.is_authenticated:
        return redirect('gift_list')

    if request.method == 'POST':
        form = GuestLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('gift_list')
    else:
        form = GuestLoginForm()

    return render(request, 'core/login.html', {'form': form})


def guest_logout(request):
    logout(request)
    return redirect('/')
