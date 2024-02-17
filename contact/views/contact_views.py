from django.http import Http404
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact

from django.core.paginator import Paginator



def index(request):

    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')


    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    #Ler uma consulta do banco de dados
    #print(contacts.query)

    context = {
        'page_obj': page_obj,
        'site_title' : 'Contacts - ',
    }

    return render(request, 'contact/index.html', context)



def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    

    if single_contact is None:
        raise Http404('Contact not found')

    context = {
        'contact': single_contact,
    }


    return render(
        request,
        'contact/contact.html',
        context
    )




def search(request):
    
   search_value = request.GET.get('q', '').strip()
   
   
   if search_value == '':
       return redirect('contact:index')

   contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value) 
        )\
        .order_by('-id')#[10:20]


   paginator = Paginator(contacts, 10)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   #print(contacts.query)
   context = {
       'page_obj': page_obj,
       'site_title' : 'Search - ',
       
       #Para mostrar o valor pesquisado no campo de busca
       'search_value': search_value,
   }

   return render(request, 'contact/index.html', context)
