
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    return  render(request,"index.html",{'result':obj})
def demo(request):
    sub=team.objects.all()
    return  render(request,"index.html",{'result':sub})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     addi=x+y
#     subt=x-y
#     divi=x/y
#     multi=x*y
#     return render(request,"result.html",{'addit':addi,'subtr':subt,'divis':divi,'multip':multi})
