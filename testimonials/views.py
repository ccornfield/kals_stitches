from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Testimonies
from .forms import TestimonyForm

def testimonials(request):
    """ A view to return the testimony page and view created testimonies"""

    testimonies = Testimonies.objects.all()

    template = 'testimonials/testimonials.html'

    context = {
        'testimonies' : testimonies,
    }
    
    return render(request, template, context)

@login_required
def add_testimonials(request):
    """ A view to let users create testimonies"""

    if request.method == "POST":
        form_data = {
            'name': request.POST['name'],
            'rating': request.POST['rating'],
            'description': request.POST['description'],
        }
        testimony_form = TestimonyForm(form_data)
        if testimony_form.is_valid:
            testimony_form.instance.creator = request.user
            testimony_form.save()
            messages.success(request, 'Successfully created Testimony!')
            return redirect(reverse('testimonials')) # Keeps user on same page.
        else:
            messages.error(request, 'Failed to create testimony. Please ensure the form is valid.')
    else:
        testimony_form = TestimonyForm()
    
    template = 'testimonials/add_testimony.html'
    
    context = {
        'testimony_form': testimony_form,
    }

    return render(request, template, context)

@login_required
def edit_testimonials(request, testimonies_id): # Testimonies_id is not a valid integer.
    """ A view to let users create testimonies"""

    testimonies = get_object_or_404(Testimonies, pk=testimonies_id)

    testimony_form = TestimonyForm(initial={
    'creator': testimonies.creator,
    'name': testimonies.name,
    'date': testimonies.date,
    'description': testimonies.description,
    'rating': testimonies.rating,
    })

    if request.user == testimonies.creator:
        if request.method == "POST":
            testimony_form = TestimonyForm(request.POST, instance=testimonies)
            if testimony_form.is_valid:
                testimony_form.save()
                messages.success(request, 'Successfully updated Testimony!')
                return redirect(reverse('testimonials'))
            else:
                messages.error(request, 'Failed to update testimony. Please ensure the form is valid.')
        else:
            testimony_form = TestimonyForm(instance=testimonies)
    else:
        messages.error(request, 'Sorry, only the original author can do that')
        return redirect(reverse('testimonials'))
    
    template = 'testimonials/edit_testimony.html'
    
    context = {
        'form': testimony_form,
        'testimonies': testimonies
    }

    return render(request, template, context)

@login_required
def delete_testimonials(request, testimonies_id):

    testimonies = get_object_or_404(Testimonies, pk=testimonies_id)

    if request.user == testimonies.creator:
        testimonies.delete()
        messages.success(request, 'Successfully deleted testimony!')
    else:
        messages.error(request, 'Sorry, only the original author can do that')
        return redirect(reverse('testimonials'))

    return redirect(reverse('testimonials'))


