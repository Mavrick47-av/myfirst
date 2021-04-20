from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from flipapp.models import product
class home(ListView):
    model=product
    template_name = 'home.html'
    context_object_name = 'k'
class detail(DetailView):
    model=product
    template_name = 'detail.html'
    context_object_name = 'i'
class update(UpdateView):
    model=product
    template_name = 'update.html'
    context_object_name = 'i'
    fields=('name','item_id','price')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

# class update(UpdateView):
#     model=product
#     template='update.html'
#     context_object_name = 'k'
#     fields = ['name','item_id','price']
#     def get_success_url(self):
#         return reverse_lazy('listview.')

# def home(request):
#     o=product.objects.all()
#     return render(request,'home.html',{'k': o})
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        price = request.POST.get('price')
        image = request.FILES['image']
        p=product(item_id=id,name=name,price=price,image=image)
        p.save()
        return redirect('/')

    return render(request,'add.html')