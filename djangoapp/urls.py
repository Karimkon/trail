"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import login,gameparks_pdf,index_view,indexx_view,sign_up_view,blog_list_view,add_gamepark_view,add_visitor_view,add_payment_view,add_warden_view,add_wildlife_view,delete_wildlife_view,edit_wildlife_view,edit_gamepark_view,delete_gamepark_view,edit_visitor_view,delete_visitor_view,edit_payment_view,delete_payment_view,edit_warden_view,delete_warden_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login,name="login_page"),
    path('gamepark_pdf/', gameparks_pdf, name="gamepark_pdf_page"),
    path('index_page/', index_view,name="index_page"),
    path('indexx/', indexx_view,name="indexx_page"),
    path('sign_up/', sign_up_view, name="sign_up"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('blog_list', blog_list_view,name="blog_list_page" ),
    path('add_gamepark/',add_gamepark_view,name="add_gamepark_page"),
    path('add_visitor/',add_visitor_view,name= "add_visitor_page"),
    path('add_payment/',add_payment_view,name= "add_payment_page"),
    path('add_warden/',add_warden_view,name= "add_warden_page"),
    path('wildlife_animal/',add_wildlife_view,name="add_wildlife_animal_page"),
    
    path('edit_gamepark/<int:gamepark_id>/',edit_gamepark_view, name="edit_gamepark_page"),
    path('delete_gamepark/<int:gamepark_id>/',delete_gamepark_view, name="delete_gamepark_page"), 
    
    path('edit_visitor/<int:visitor_id>/',edit_visitor_view, name="edit_visitor_page"),
    path('delete_visitor/<int:visitor_id>/',delete_visitor_view, name="delete_visitor_page"),
    
    path('edit_payment/<int:payment_id>/',edit_payment_view, name="edit_payment_page"),
    path('delete_payment/<int:payment_id>/',delete_payment_view, name="delete_payment_page"),
    
    path('edit_warden/<int:warden_id>/',edit_warden_view, name="edit_warden_page"),
    path('delete_warden/<int:warden_id>/',delete_warden_view, name="delete_warden_page"),
    
    path('edit_wildlife/<int:wildlife_id>/',edit_wildlife_view, name="edit_wildlife_page"),
    path('delete_wildlife/<int:wildlife_id>/',delete_wildlife_view, name="delete_wildlife_page"),
]
