from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.view_events, name='events'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
]