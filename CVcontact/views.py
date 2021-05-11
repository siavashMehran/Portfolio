from CVabout.models import ContactInfo
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

        # the initial passing is nessissary because
        #the name of input and the name of model attrebiute
        #differ from each other and this is my lazy way around it
        form = ContactMeForm(request.POST, initial={'messege' : request.POST.get('messegee')})

        if form.is_valid():
            form.save()
            form = ContactMeForm(request.POST)
            return JsonResponse({'result' : 'Messege Sent'}, status=200)

        else:
            form.add_error('messege', 'operation failed')
            return JsonResponse({'result' : 'invalid operation, Please try againg'}, status=400)

    else : form = ContactMeForm()

    contactInfo = ContactInfo.objects.earliest('pk')
    
    context = {
        'form' : form,
        'info' : contactInfo
    }
    return render(request, "contact.html", context)