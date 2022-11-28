import stripe
from config import settings
from django.views.generic import ListView, DetailView, View
from django.http import JsonResponse
from item.models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemListView(ListView):
    model = Item
    queryset = Item.objects.all()
    template_name = 'item_list.html'
    
    
class ItemDetailView(DetailView):
    model = Item
    
    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY       
            })
        return context


class CreateCheckoutView(View):
    def post(self, request, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs['pk'])
        session = stripe.checkout.Session.create(
            line_items = [{
                "price_data":{
                    "currency": "usd",
                    "product_data": {"name": item.name},
                    "unit_amount": item.price,
                    },
                "quantity": 1,
            }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/',
        )
        return JsonResponse({"id": session.id})
        
