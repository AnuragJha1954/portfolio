from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

def terminal(request):
    return render(request, 'terminal.html')


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # text = request.POST.get('text')
        # from_email= settings.EMAIL_HOST_USER
        # message = f"Name: {name}\nEmail: {email}\nMessage: {text}"
        # recipient_email = 'office.anuragjha@gmail.com'
        
        return JsonResponse({'success': True, 'message': 'Email Sent Successfully'})
    else:
        return render(request, 'contact.html')
