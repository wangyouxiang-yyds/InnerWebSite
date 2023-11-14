from django.shortcuts import render
from django.core.mail import EmailMessage
from django.urls import reverse
from .models import *


# Create your views here.


def contactView(request):
    if "name" in request.POST:
        name = request.POST['name']
        department = request.POST['department']
        serial_number = request.POST['serial-number']
        message = request.POST['message']
        email = request.POST['email']
        obj = ContactModels.objects.create(
            name=name,
            email=email,
            department=department,
            serial_number=serial_number,
            message=message
        )
        obj.save()
        mail_body = u'''
        名字:{}
        部門:{}
        工號:{}
        電子信箱:{}
        反應意見:{}
        '''.format(name, department, serial_number, email, message)
        send_mail = EmailMessage('來自' + department + name + '的意見', mail_body, email, ['it@agit-global.com'])

        send_mail.send()

    current_url = request.path_info
    contact_url = reverse('contact')

    return render(request, 'contact.html', locals())
