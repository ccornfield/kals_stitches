from django.shortcuts import render

from .models import Testimonies
from .form import TestimonyForm

def testimonials(request):
    """ A view to return the index page """

    testimonies = Testimonies.objects.all()

    template = 'testimonials/testimonials.html'

    context = {
        'testimonies' : testimonies,
    }
    
    return render(request, template, context)
