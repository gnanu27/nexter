from django.shortcuts import render, get_object_or_404
from realtor.models import Realtor
from listing.models import Listing
from listing.choices import bedroom_choices, state_choices, price_choices
# Create your views here.
def home(req):

    listing = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    context = {
    'state_choices' : state_choices,
    'price_choices' : price_choices,
    'bedroom_choices' : bedroom_choices,
    'listings': listing,
    'values' : req.GET
    }
    return render(req, 'pages/home.html', context)



def about(req):
    realtor = Realtor.objects.order_by('hire_date')
    context = {
        'realtors': realtor
    }


    return render(req, 'pages/about.html', context)