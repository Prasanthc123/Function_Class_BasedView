from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.
def fbv_string(request):
    return HttpResponse('hey ur using function base view ')

class cbv_string(View):
    def get(self,request):
        return HttpResponse('hey ur using class base view nd displaying string as reponse')



def fbv_html(request):
    return render(request,'fbv_html.html')

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')


def insert_school_fbv(request):
    SFO=Schoolform()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data submitted successfully')
    return render(request,'insert_school_fbv.html',d)


class insert_school_cbv(View):
    def get(self,request):
        SFO=Schoolform()
        d={'SFO':SFO}
        return render(request,'insert_school_cbv.html',d)
    
    def post(self,request):
        SFDO=Schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Insert_School_Cbv is done')


class Template_cbv(TemplateView):
    template_name='Template_cbv.html'
