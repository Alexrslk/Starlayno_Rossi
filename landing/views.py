from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, Review, WorkExample, SiteSettings
from .forms import ContactRequestForm
from django.core.management import call_command

def index(request):
    call_command('migrate', interactive=False)  # миграция


def index(request):
    # Настройки сайта — берём первую запись (создаём пустую, если нет)
    settings_obj = SiteSettings.objects.first()
    if settings_obj is None:
        settings_obj = SiteSettings.objects.create()

    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('landing:index')
        else:
            messages.error(request, 'Проверьте правильность заполнения формы.')
    else:
        form = ContactRequestForm()

    context = {
        'settings': settings_obj,
        'services': Service.objects.filter(is_active=True),
        'reviews': Review.objects.filter(is_published=True),
        'works': WorkExample.objects.filter(is_active=True),
        'form': form,
    }
    return render(request, 'landing/index.html', context)