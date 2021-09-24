from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name="home"),
    path('addContact',views.addContact,name="add"),
    path('displayContact',views.displayContact,name="display"),
    path('deleteContact',views.deleteContact,name="delete"),
    path('updateContact',views.updateContact,name="update"),
    path('addpage',views.addpage,name="addpage"),
    path('displaypage',views.displaypage,name="displaypage"),
    path('updatepage',views.updatepage,name="updatepage"),
    path('deletepage',views.deletepage,name="deletepage")
]+static(settings.STATIC_URL)