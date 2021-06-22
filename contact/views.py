from contact.models import Contact
from django.shortcuts import render
# from .models import Contact
from django.http import HttpResponseRedirect
from django.contrib import messages


def contact(request):
    contact = Contact()

    if request.method == "POST":
        contact.Name = request.POST['name']
        contact.Email_address = request.POST['email']
        contact.Message = request.POST['comment']

        contact.save()
        messages.success(request, 'your message has been sent successfully.')

    return render(request, 'contact.html')
