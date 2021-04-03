from CVcontact.forms import ContactMeForm
from django.http.request import HttpRequest
from CVcontact.models import ContactMe
from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.

def ss(s):
    print('#'*50)
    print(s)
    print('#'*50)


def contactMe(request:HttpRequest):

    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        form = ContactMeForm(request.POST, initial={'messege' : request.POST.get('messegee')})

        if form.is_valid():
            form.save()
            return JsonResponse({'result' : 'Messege Sent'})
        else:
            form.add_error('messege', 'operation failed')
            return JsonResponse({'result' : 'Please try againg'})

    else : form = ContactMeForm()

    context = {
        'form' : form
    }
    return render(request, "contact.html", context)