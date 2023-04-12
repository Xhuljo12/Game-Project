from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('newsDetails/<id>', views.newsDetails, name='newsDetails'),
    path('news/', views.news, name='news'),
    path('product/<id>', views.product, name='product'),
    path('products/', views.products, name='products'),
    path('productBase', views.productBase, name='productBase'),
    path('productBases/<id>', views.productBases, name='productBases'),
    path('newsBase', views.newsBase, name='newsBase'),
    path('newsBases/<id>', views.newsBases, name='newsBases'),
    path('undermaintenance/', views.undermaintenance, name='undermaintenance'),
    path('search/', views.search, name='search'),
]