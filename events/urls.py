from django.urls import path
from events import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('events/', views.event_list, name="event_list"),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:event_id>/update/', views.update_event,
         name='update_event'),
    path('events/<int:event_id>/delete/',
         views.delete_event, name='delete_event'),
    path('events/<int:event_id>/book/', views.book_event, name="book_event"),
    path('events/<int:event_id>/booking_success/',
         views.booking_success, name="booking_success"),
    # Management views
    path('bookings/', views.booking_list, name="booking_list"),
    path('bookings/<int:booking_id>/',
         views.booking_detail, name='booking_detail'),
    path('bookings/<int:booking_id>/update/',
         views.update_booking, name='update_booking'),
    path('bookings/<int:booking_id>/delete/',
         views.delete_booking, name='delete_booking'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)