from django.conf import settings
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render,redirect
# Create your views here.
from .forms import ContactForm
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def post(request):
    return render(request,"post.html")

# def contact(request):
#     return render(request,"contact.html")



def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_email]
                #to_email = [from_email, form_email]
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)

		try:
			send_mail(subject,contact_message, from_email, to_email)
		except BadHeaderError:
			return HttpResponse('Invalid header found.')
		return redirect('success')
            
	context = {
		"form": form,
	}
		
	return render(request, "contact.html", context)
	

def success(request):
    return render(request,'success.html') 