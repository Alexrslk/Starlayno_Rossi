document.addEventListener('DOMContentLoaded', function () {
    // Ищем все поля, к которым нужно применить маску.
    // Можно навесить на любое поле с атрибутом data-phone-mask
    const inputs = document.querySelectorAll('input[data-phone-mask]');

    inputs.forEach(function (input) {
        input.setAttribute('type', 'tel');
        input.setAttribute('inputmode', 'tel');
        input.setAttribute('autocomplete', 'tel');
        input.setAttribute('maxlength', '18'); // +7 (999) 123-45-67 = 18 символов

        // При фокусе — если поле пустое, сразу подставляем +7 (
        input.addEventListener('focus', function () {
            if (!input.value) {
                input.value = '+7 (';
            }
        });

        // При потере фокуса — если пользователь ввёл только +7 ( — очищаем
        input.addEventListener('blur', function () {
            if (input.value === '+7 (' || input.value === '+7') {
                input.value = '';
            }
        });

        input.addEventListener('input', function (e) {
            // Оставляем только цифры
            let digits = e.target.value.replace(/\D/g, '');

            // Если начинается с 8 — заменяем на 7
            if (digits.startsWith('8')) {
                digits = '7' + digits.slice(1);
            }
            // Если начинается не с 7 — добавляем 7 в начало
            if (digits && !digits.startsWith('7')) {
                digits = '7' + digits;
            }
            // Ограничиваем 11 цифрами (7 + 10)
            digits = digits.slice(0, 11);

            // Собираем красивый формат
            let formatted = '';
            if (digits.length > 0) {
                formatted = '+7';
                if (digits.length > 1) {
                    formatted += ' (' + digits.slice(1, 4);
                }
                if (digits.length >= 5) {
                    formatted += ') ' + digits.slice(4, 7);
                }
                if (digits.length >= 8) {
                    formatted += '-' + digits.slice(7, 9);
                }
                if (digits.length >= 10) {
                    formatted += '-' + digits.slice(9, 11);
                }
            }

            e.target.value = formatted;
        });

        // Запрещаем вставку мусора (необязательно, но приятно)
        input.addEventListener('keydown', function (e) {
            // Разрешаем: backspace, delete, tab, escape, enter, стрелки, home/end
            const allowed = ['Backspace', 'Delete', 'Tab', 'Escape', 'Enter',
                             'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown',
                             'Home', 'End'];
            if (allowed.includes(e.key)) return;
            // Разрешаем Ctrl/Cmd + A/C/V/X
            if ((e.ctrlKey || e.metaKey) && ['a', 'c', 'v', 'x'].includes(e.key.toLowerCase())) return;
            // Блокируем всё, кроме цифр
            if (!/^\d$/.test(e.key)) {
                e.preventDefault();
            }
        });
    });
});