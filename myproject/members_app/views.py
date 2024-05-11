from django.http import HttpRequest
from django.shortcuts import render
from django.utils import timezone

from .models import Member, MemberData


# Create your views here.
def input_view(request: HttpRequest):
    if request.method == 'POST':
        # Отримання даних з POST-запиту
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        text = request.POST.get('text', '')

        # Перевірка, чи існує вже член з таким ім'ям та електронною поштою
        member, created = Member.objects.get_or_create(name=name, email=email)

        # Створення нового об'єкта MemberData і збереження його в базі даних
        MemberData.objects.create(member=member, text=text, pub_date=timezone.now())

    return render(request, 'input.html')


def display_view(request):
    if request.method == 'GET':
        members = Member.objects.all()
        membersdata = MemberData.objects.all()

        # message = f'Name: {name}, Email: {email}, Text: {text}'
        message = f'{members}, {membersdata}'
    else:
        message = 'No data submitted.'

    return render(request, 'display.html', {'members': members, 'member_data': membersdata})


def session_view(request):
    # breakpoint()
    if request.session:
        data = request.session.TEST_COOKIE_NAME, request.session.TEST_COOKIE_VALUE, dir(request.session)
    else:
        data = 'No session data.'

    return render(request, 'session.html', {'data': data})
