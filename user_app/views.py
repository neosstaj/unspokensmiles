from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def test(request):
    user = request.user
    test = User.objects.filter(username = user.username)
    test2 = User.objects.filter(username = user.username).first()
    print(test)
    print(test2)
    return redirect('/')
def signup(request):
    if request.method == 'POST':
        POST = request.POST
        isim = POST.get('isim')
        soyisim = POST.get('soyisim')
        email =POST.get('email')
        password = POST.get('password')
        if isim and soyisim and email and password:
            usernametrue = User.objects.filter(username = isim).first()
            emailtrue = User.objects.filter(email = email).first()
            if usernametrue:
                messages.add_message(request,messages.ERROR,'Bu Kullanıcı adına sahip bir kullanıcı var',extra_tags='signup-error')
                return redirect('signup')
            if emailtrue:
                messages.add_message(request,messages.ERROR,'Bu Emaile sahip bir kullanıcı var',extra_tags='signup-error')
                return redirect('signup')
            
            User.objects.create_user(username=isim,first_name = isim,last_name = soyisim,email= email, password=password)
            messages.add_message(request,messages.ERROR,'Kayıt Olduğunuz İçin Teşekkürler Giriş yapın',extra_tags='signin')
            return redirect('signup')
            
        else:
            messages.add_message(request,messages.ERROR,'Lütfen Tüm Alanları Doldurunuz',extra_tags='signup-error')
            return redirect('signup')
    else:
        return render(request,'register.html')
def signin(request):
    if request.method == 'POST':
        POST = request.POST
        email =POST.get('email')
        password = POST.get('password')
        if email and password:
            emailtrue = User.objects.filter(email = email).first()
            if emailtrue:
                username = emailtrue.username
                user = authenticate(request,username = username,password = password)
                if user:
                    login(request,user)
                    messages.add_message(request,messages.ERROR,'Giriş başarılı',extra_tags='signin')
                    return redirect('/')
                else:
                    messages.add_message(request,messages.ERROR,'E postanız veya şifreniz yanlış',extra_tags='signin-error')
                    return redirect('signup')
            else:
                messages.add_message(request,messages.ERROR,'E postanız veya şifreniz yanlış',extra_tags='signin-error')
                return redirect('signup')
        else:
            messages.add_message(request,messages.ERROR,'Lütfen Tüm Alanları Doldurunuz',extra_tags='signin-error')
            return redirect('signup')
    else:
        return render(request,'register.html')