from django.shortcuts import render
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


from .forms import ContactForm
from .models import Contact


def contact(request):
    """ Display the user's profile. """

    if request.method == 'POST':
        form_data = {
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'body': request.POST['body'],
        }
        contact_form = ContactForm(form_data)

        if contact_form.is_valid():
            contact = contact_form.save()
            cust_email = contact.email
            subject = render_to_string(
                'contact/inquiry_emails/inquiry_email_subject.txt',
                {'contact': contact})
            body = render_to_string(
                'contact/inquiry_emails/inquiry_email_body.txt',
                {'contact': contact})
            
            messages.success(request, 'Contact email sent successfully')
        
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            ) 
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
                
    contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
