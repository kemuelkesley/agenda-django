from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    # CRUD
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/delete/', views.contact, name='contact'),
]
