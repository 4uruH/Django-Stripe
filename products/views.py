import stripe
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings
from .models import Item
from django.views.decorators.csrf import csrf_protect

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


class IndexPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name="test1")
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "https://127.0.0.1:8000"
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': '{{price_123}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
