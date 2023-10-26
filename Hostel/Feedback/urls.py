from django.urls import path
from . import views

urlpatterns=[
    # endpoint for all hostels and posting a new hostel
    path('hostels/', views.hostels, name='feedback'),  
    # endpoint for feedback of a given hostel
    path('feeds/<str:pk>', views.Feedback, name="feeds"),
    # endpoint for getting info for a gicen hostel
    path('hostel/<str:pk>', views.hostelInfo, name="hostelInfo"),
    path('hrooms/<str:pk>', views.hostelRooms, name="hostelRooms"),
    path('room/<str:pk>', views.roomInfo, name="room"),
]