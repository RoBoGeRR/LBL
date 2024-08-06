from django.urls import path
from .views import business_from_list_view, add_business_view, BusinessListCreate, BusinessRetrieveUpdateDestroy, MapView

urlpatterns = [
    path('business/', BusinessListCreate.as_view(), name='business-list-create'),
    path('business/<int:pk>/', BusinessRetrieveUpdateDestroy.as_view(), name='business-r-u-d'),
    path('map/', MapView.as_view(), name='map-view'),
    path('business/new/', add_business_view, name='business-new'),
    path('business/from_list/', business_from_list_view, name='business_from_list')
]