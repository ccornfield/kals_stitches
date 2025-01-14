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
        form = TestimonyForm(request.POST)
        if form.is_valid:
            form.instance.creator = request.user
            form.save()
            messages.success(request, 'Successfully created Testimony!')
            redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to create testimony. Please ensure the form is valid.')
    else:
        form = TestimonyForm()
    
    template = 'testimonials/add_testimony.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_testimonials(request, testimonies_id):
    """ A view to let users create testimonies"""

    testimonies = get_object_or_404(Testimonies, pk=testimonies_id)

    if request.user == testimonies.creator:
        if request.method == "POST":
            form = TestimonyForm(request.POST, instance=testimonies)
            if form.is_valid:
                form.save()
                messages.success(request, 'Successfully updated Testimony!')
                redirect(reverse('testimonials', args=[testimonies_id]))
            else:
                messages.error(request, 'Failed to update testimony. Please ensure the form is valid.')
        else:
            form = TestimonyForm()
    else:
        messages.error(request, 'Sorry, only the original author can do that')
        return redirect(reverse('testimonials'))
    
    template = 'testimonials/edit_testimony.html'
    
    context = {
        'form': form,
        'testimonies': testimonies
    }

    return render(request, template, context)

@login_required
def delete_testimonials(request, testimonies_id):

    if request.user == testimonies.creator:
        testimonies = get_object_or_404(Testimonies, pk=testimonies_id)
        testimonies.delete()
        messages.success(request, 'Successfully deleted testimony!')
    else:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    return redirect(reverse('testimonials'))


