from django.shortcuts import render,redirect
import iyzipay
import json
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse
from user_app.models import Donations,DonationType
from user_app.models import blog as BlogModels
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

API_KEY = 'sandbox-ybJixj0TVm9yQcaLZKYjN5hiAwUzFMcI'
SECRET_KEY = 'sandbox-nW30QdMCvJ5HKsBoQXGH288DcJ4ZoaIV'
BASE_URL = 'sandbox-api.iyzipay.com'

options = {
    'api_key': API_KEY,
    'secret_key': SECRET_KEY,
    'base_url': BASE_URL,
}
sozlukToken = list()


def index(request):
    context = dict(
        donate = Donations.objects.all(),
        blog = BlogModels.objects.filter(active = True)
    )
    
    return render(request,'index.html',context)


# @login_required(login_url='/signup') 
def payment(request):
    price = request.POST.get('price')
    if price:   
        print('fiytayyy',price)
        context = dict()
        OneTime = request.POST.get('oneTime')
        Monthly = request.POST.get('monthly')
        print('onetime',OneTime)
        print('Monthly',Monthly)
        print('Monthly',len(OneTime))
        print('Monthly',len(Monthly))
        print('Monthly',len(Monthly)>0)
        print('Monthly',len(OneTime)>0)
        

        if len(OneTime) > 0 or len(Monthly) > 0:        
            
            if OneTime == '1':
                DonationType = 1
            else:
                DonationType = 2
        else:
            messages.add_message(request,messages.ERROR,'Lütfen Bağış Tipi seçin',extra_tags='payment-error')
            return redirect('/')
        
        print('onetime',OneTime)
        print('onetime',DonationType)
        print('Monthly',Monthly)
        user = request.user
        print(user)

        print(type(user))
        buyer={
            'id': 'BY789222',
            'name': user.username,
            'surname': user.last_name,
            'gsmNumber': '+905350000000',
            'email': user.email,
            'identityNumber': '74300864791',
            'lastLoginDate': '2015-10-05 12:43:35',
            'registrationDate': '2013-04-21 15:12:09',
            'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
            'ip': '85.34.78.112',
            'city': 'Istanbul',
            'country': 'Turkey',
            'zipCode': '34732'
        }

        address={
            'contactName': user.username,
            'city': 'Istanbul',
            'country': 'Turkey',
            'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
            'zipCode': '34732'
        }
        basket_items=[
            {
                'id': 'BI101',
                'name': user.username,
                'category1': 'Collectibles',
                'category2': 'Accessories',
                'itemType': 'PHYSICAL',
                'price': '0.3'
            }
        ]
        print(price)
        request_iyzico = {
            'locale': 'tr',
            'conversationId': '123456789',
            'price': '0.3',
            'paidPrice': price,
            'currency': 'TRY',
            'basketId': 'B67832',
            'paymentGroup': 'PRODUCT',
            "callbackUrl": "http://127.0.0.1:8000/result/",
            "enabledInstallments": ['2', '3', '6', '9'],
            'buyer': buyer,
            'shippingAddress': address,
            'billingAddress': address,
            'basketItems': basket_items,
            # 'debitCardAllowed': True
        }

        print(type(user))
        print(user)
        checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(request_iyzico,options)
        page = checkout_form_initialize

        print('iyzico-sayfa')
        print(page)
        print('*'*50)

        content = checkout_form_initialize.read().decode('utf-8')
        
        print(content)
        content_yazdir = json.loads(content)

       


        errorCode = content_yazdir.get('errorCode')
        errorMessage = content_yazdir.get('errorMessage')
        print('hata kodu ',errorCode,'TİPİ',type(errorCode))
        print('hata Mesajı ',errorMessage,'TİPİ',type(errorMessage))

        if content_yazdir.get('errorCode') or content_yazdir.get('errorMessage'):
            messages.error(request, f'Hata Kodu: {errorCode}, Hata Mesajı: {errorMessage}', extra_tags='payment-error')
            return redirect('/')
        

        print(type(content))
        print('*0'*50)
        json_content = json.loads(content)
        print('*0'*50)
        print('*0'*50)
        print('*0'*50)
        print(json_content)
        print('*0'*50)
        print('*0'*50)
        print('*0'*50)
        print('*0'*50)
        print('checklouttttttt ',json_content['checkoutFormContent'])
        print('*0'*50)
        print(json_content["token"])
        print('*0'*50)


        sozlukToken.append(json_content['token'])



        response = HttpResponse(json_content['checkoutFormContent'])
        response.set_cookie('donationtype',DonationType)
        response.set_cookie('para',price)
        return response
        
    else:
        messages.add_message(request,messages.ERROR,'Lütfen Miktar giriniz',extra_tags='payment-error')
        return redirect('/')
@require_http_methods(['POST'])
@csrf_exempt

# @login_required(login_url='/signup') 
def result(request):
    context = dict()
    print('*'*50)
    print(request.user)
    print('*'*50)
    url = request.META.get('index')
    user = User
    request_iyzico = {
        'locale':'tr',
        'conversationId':'123456789',
        'token':sozlukToken[0]
    }
    checkout_form_result= iyzipay.CheckoutForm().retrieve(request_iyzico,options)
    print('*0'*50)
    print('Sonuç')
    print(type(checkout_form_result))
    result = checkout_form_result.read().decode('utf-8')
    print('*0'*50)
    print(sozlukToken[0],'sonuc herhaldeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    print('*0'*50)
    sonuc = json.loads(result,object_pairs_hook=list)

    print('sonuc')
    print('sonucddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
    print(sonuc)
    print(sonuc[0][1])
    print(sonuc[5][1])
    print(sonuc[6])
    user = request.user
    print('KULANICIIIssssI',user)
    for i in sonuc:
        print('sonuclar',i,'tipi',type(i))

    print('*0'*50)
    print('sözlük token')
    print(sozlukToken)
    print('*0'*50)



    if sonuc[0][1] == 'success':
        # quantity = sonuc[5][1]
        print('*'*50)
        print('sonucsdasdasdasdasdas',sonuc[5][1])
        donation_type =  request.COOKIES.get('donationtype')
        quantity =  request.COOKIES.get('para')
        print('fiyat cookie',quantity)
        print('fiyat cookie',type(quantity))
        print('donate tipiğ',donation_type)
        user =  request.user
        print('KULANICIIII',user)
        # AYLIK ÜYELİK TİPİ İD 2 TEK SEFERLİK 1
        if donation_type == '1':
            donation_type = DonationType.objects.filter(title = 'Tek Seferlik').first()
        else:
            donation_type = DonationType.objects.filter(title = 'Aylık').first()      
        Donations.objects.create(
                user =user,
                donation_type = donation_type,
                quantity = quantity
            )
        return redirect('success')
    
    elif sonuc[0][1] == 'failure':
        return redirect('fail')

    return HttpResponse(url)


def success(request):
    messages.add_message(request, messages.INFO, "Bağışınız İçin Teşekkür Ederiz",extra_tags='py-success')
    return redirect('/')
    

def fail(request):
    messages.add_message(request, messages.INFO, "Ödeme Aşamasında sıkıntı çıktı",extra_tags='payment-error')
    return redirect('/')


