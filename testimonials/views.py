from django.shortcuts import render

def testimonials(request):
    """ A view to return the index page """
    
    return render(request, 'testimonials/testimonials.html')
