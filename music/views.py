from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

def index(request):
	print(request.method)
	return render(request,'index.html', {
	    'form': ContactForm,
	})

def contact(request):
    form_class = ContactForm
    print("Hit contact request")
    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['danieldjangotutorial@gmail.com'],
                headers = {'Reply-To': contact_email }
            )

	    print(email)
            email.send()
            return redirect('contact')

    return render(request, 'index.html', {
        'form': form_class,
    })
