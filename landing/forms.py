import re

from django import forms
from django.core.exceptions import ValidationError

from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    """Форма заявки с лендинга."""

    class Meta:
        model = ContactRequest
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (___) ___-__-__',
                'required': True,
                'data-phone-mask': 'true',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Какая у вас машина и что хотите установить?',
                'rows': 3,
            }),
        }
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'message': 'Комментарий',
        }

    def clean_name(self):
        """Убираем лишние пробелы и проверяем, что имя не из одних пробелов."""
        name = self.cleaned_data['name'].strip()
        if len(name) < 2:
            raise ValidationError('Имя слишком короткое')
        return name

    def clean_phone(self):
        """
        Приводим телефон к единому виду +7XXXXXXXXXX.
        Принимаем любые записи: +7 (999) 123-45-67, 89991234567, 9991234567.
        """
        phone = self.cleaned_data['phone']
        digits = re.sub(r'\D', '', phone)

        # 8XXXXXXXXXX → 7XXXXXXXXXX
        if digits.startswith('8'):
            digits = '7' + digits[1:]

        # Если не начинается с 7 — добавляем
        if not digits.startswith('7'):
            digits = '7' + digits

        if len(digits) != 11:
            raise ValidationError('Введите корректный номер телефона')

        return f'+{digits}'