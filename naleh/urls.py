from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('buy/<int:product_id>/', views.buy, name='buy_product'),
    path('about/',views.about,name='about'),
    path('shop/',views.shop,name='shop'),
    path("search/", views.search, name="search"),
    path("information/",views.information,name="information"),
    path("contact/", views.contact_view, name="contact"),
    path('upcoming_products',views.upcoming_products,name='upcoming_products'),
]
