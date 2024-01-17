from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from user_app.models import blog as BlogModels
# Create your views here.



def signup(request):
    if request.user.is_authenticated == False:
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
    else:
        return redirect('/')
def signin(request):
    if request.user.is_authenticated == False:
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
    else:
        return redirect('/')
    

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')
    
def aboutus(request):
    return render(request,'aboutus.html')

def blog(request):
    blog = BlogModels.objects.filter(active = True)
    context = dict(
        blog = blog
    )
    return render(request,'blog.html',context)
def blogDetail(request,id):
    blog = BlogModels.objects.filter(id = id,active = True).first()
    blogall = BlogModels.objects.filter(active = True)
    context = dict(
        blog = blog,
        blogall= blogall,
    )
    return render(request,'blogdetail.html',context)

def donate(request):
    return render(request,'donate.html')
def involved(request):
    return render(request,'involved.html')
def ourwork(request):
    return render(request,'ourwork.html')
def whyoralhealt(request):
    return render(request,'whyoralhealt.html')
