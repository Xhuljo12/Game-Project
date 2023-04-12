from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from .models import *
from django.db.models import Q 

# Create your views here.

def homepage(request):
    products = Product.objects.all()
    news = News.objects.all()
    productBase = ProductBase.objects.all()
    newsBase = NewsBase.objects.all()
    context = {"products":products, "news":news, "productBase":productBase, "newsBase":newsBase}
    return render(request, 'homepage.html', context)

def search (request):
    if request.method == "POST":
        searched = request.POST.get('search')
        if searched:
            searching= Product.objects.filter(product_name__contains=searched)
            if searching:
                context={'searched':searched,'searching': searching}
                return render(request,'search.html',context)
            else:
                messages.info(request, ' ')
        else:
            return HttpResponseRedirect('/search/')
    context={'searching':searching}
    return render(request,'search.html', context)

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):

    if request.method == "POST":
        name_contact = request.POST['firstName']
        surname_contact = request.POST['lastName']
        email_contact = request.POST['email']
        comment_contact = request.POST['comment']

        Contact(contact_name=name_contact, contact_surname=surname_contact, 
        contact_email=email_contact, contact_message=comment_contact).save()

        return render(request, 'thankyou.html')
    return render(request, 'contact.html')

def undermaintenance(request):
    return render(request, 'undermaintenance.html')

def newsDetails(request, id):
    newsDetailsDetail = News.objects.get(news_id=id)
    context = {"newsDetailsDetail":newsDetailsDetail}
    return render(request, 'newsDetails.html', context)

def news(request):
    news = News.objects.all()
    context = {"news":news}
    return render(request, 'news.html', context)

def product(request, id):
    productDetail = Product.objects.get(product_id=id)
    context = {"productDetail":productDetail}
    return render(request, 'product.html', context)

def products(request):
    products = Product.objects.all()
    p = Paginator(products, 6)
    print('NUMBER OF PAGES')
    print(p.num_pages)
    page_num = request.GET.get("page", 1)
    try: 
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    context = {"products":page}
    return render(request, 'products.html', context) 

def productBases(request, id):
    productBasesDetail = ProductBase.objects.get(productBase_id=id)
    context = {"productBasesDetail":productBasesDetail}
    return render(request, 'productBases.html', context)    

def productBase(request):
    productBase = ProductBase.all()
    context = {"productBase":productBase}
    return render(request, 'productBase.html', context)

def newsBases(request, id):
    newsBasesDetail = NewsBase.objects.get(newsBase_id=id)
    context = {"newsBasesDetail":newsBasesDetail}
    return render(request, 'newsBases.html', context)
    
def newsBase(request):
    newsBase = NewsBase.all()
    context = {"newsBase":newsBase}
    return render(request, 'newsBase.html', context)
