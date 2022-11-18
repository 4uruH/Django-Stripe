from django.contrib import admin
from django.urls import path
from products.views import CreateCheckoutSessionView, IndexPageView, SuccessView, CancelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('cancel/', CancelView.as_view, name='cancel'),
    path('success/', SuccessView.as_view, name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]
