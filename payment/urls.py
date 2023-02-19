from django.urls import path
from .views import (
    CreateCheckoutSessionView,
    ItemLandingPageView,
    SuccessView,
    CancelView,
)

app_name = 'payment'

urlpatterns = [
    path('item/<int:pk>/', ItemLandingPageView.as_view(), name='landing-page'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),

]
