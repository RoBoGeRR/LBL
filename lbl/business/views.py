from unicodedata import category
from django.shortcuts import render

from rest_framework import generics
from .models import Business
from .serializers import BusinessSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.views import View
import json
from .filters import BusinessFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Business
from .serializers import BusinessSerializer
from .filters import BusinessFilter
import requests


def business_from_list_view(request):
    API_KEY = 'AIzaSyCUOy0BkAIqj8QmNdYpB9WQ8iskk3hfe98'
    LOCATION = '49.8397,24.0297'
    RADIUS = 50000
    TYPE = 'grocery_or_supermarket'

    def get_grocery_store(api_key, location, radius, place_type):
        url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={place_type}&key={api_key}'
        response = requests.get(url)
        print(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    results = get_grocery_store(API_KEY, LOCATION, RADIUS, TYPE)

    
    serializers = []
    if results:
        for place in results['results']:
            
            name = place.get('name')
            address = place.get('vicinity')
            coords = place.get('geometry')['location']
            business = Business(name=name, category='Supermarket/grocerystore', address=address, latitude=coords['lat'], longtitude=coords['lng'])
            bserializer = BusinessSerializer(business)
            print("Name: ", name)
            print("Address: ", address)
            print("Category: ", 'Supermarket/grocerystore')
            print('Longitude: ', coords['lng'])
            print('Latitude: ', coords['lat'])
            serializers.append(bserializer.data)
            # return render(request, 'business/add_business.html', {'serializer':bserializer.data})
    return render(request, 'business/add_business.html', {'serializers':serializers})
                    # print(f'Name: {name}, Address: {address},Latitude:{coords['lat']}, Longitude:{coords['lng']}')
    
    




class BusinessListCreate(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BusinessFilter
class BusinessRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

# def map_view(request):
#     return render(request, 'business/map.html')

class MapView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'business/map.html')
    
@csrf_exempt
def add_business_view(request):
    return render(request, 'business/add_business.html')


