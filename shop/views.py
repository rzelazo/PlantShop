from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from shop.models import Plant


class HomeView(ListView):
    template_name = 'shop/index.html'
    model = Plant
    context_object_name = 'plants'

    def get_queryset(self):
        return self.model.objects.order_by('?')[:8]


class PlantView(DetailView):
    template_name = 'shop/plant_detail.html'
    model = Plant
    context_object_name = 'plant'


def buy_now(request, pk):
    if request.method == 'POST':
        plant = get_object_or_404(Plant, pk=pk)
        plant.in_stock -= 1
        plant.save()
        return redirect(to='shop:thank_you')


class ThankYouView(TemplateView):
    template_name = 'shop/thank_you.html'


class AboutProjectView(TemplateView):
    template_name = 'shop/about.html'


class ContactView(TemplateView):
    template_name = 'shop/contact.html'
