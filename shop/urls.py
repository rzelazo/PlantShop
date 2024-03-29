from django.urls import path
from shop.views import HomeView, PlantView, buy_now, ThankYouView, AboutProjectView, ContactView

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutProjectView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('detail/<int:pk>/', PlantView.as_view(), name='detail'),
    path('detail/<int:pk>/buy-now', buy_now, name='buy_now'),
    path('thank-you/', ThankYouView.as_view(), name='thank_you'),
]
