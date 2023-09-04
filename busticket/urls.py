from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('booking/', views.booking_page, name='booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
    path('offer/', views.offer_page, name='offer'),
    path('ticket_cancel/', views.ticket_cancel, name='ticket_cancel'),
    path('bus_seat/', views.bus_seat, name='bus_seat'),
    path('payment/', views.payment_page, name='payment'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('user_list/', views.user_list, name='user_list'),
]
