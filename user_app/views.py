from django.shortcuts import render,redirect
from django.core.mail import BadHeaderError, send_mail

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from user_app.models import blog as BlogModels,Donations
from django.contrib.auth.decorators import login_required
# Create your views here.
from user_app.forms import User_Settings_Form,Password_Change_Form
from django.contrib.auth import update_session_auth_hash
from config.settings import EMAIL_HOST_USER

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
                subject = "Unspokensmiles'a Hoşgeldiniz" 
                email_from = EMAIL_HOST_USER
                recipient_list = [email]
                message = f"Kayıt Olduğunuz İçin Teşekkürler {isim}"
                send_mail(
                    subject,
                    message,
                    email_from,
                    recipient_list,)
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
@login_required(login_url="/")
def donations(request):
    user = request.user
    Donates = Donations.objects.filter(user = user)
    context = dict(
        Donates = Donates,
    )
    return render(request,"profil.html",context)
@login_required(login_url="/")
def profil(request):
    if request.method == 'POST':
        u_r_f = User_Settings_Form(data=request.POST, instance=request.user)
        if u_r_f.is_bound:
            if u_r_f.is_valid():
                u_r_f.save()
                return redirect('profil')
            else:
                print('urf valid değil', u_r_f.errors)
        p_r_f = Password_Change_Form(user=request.user, data=request.POST)
        if p_r_f:
            if p_r_f.is_valid():
                p_r_f.save()
                update_session_auth_hash(request, p_r_f.user)
                messages.add_message(request, messages.SUCCESS, 'Şifreniz Başarıyla Değiştirildi')
                print(f'Şifreniz değiştirildi')
                return redirect('profil')
            else:
                messages.add_message(request, messages.SUCCESS, f'Şifreniz Değiştirilemedi {p_r_f.errors}', extra_tags='error-sifre')
                print(f'Şifreniz Değiştirilemedi{p_r_f.errors}')
                return redirect('profil')
        else:
            return redirect('profil')
        

        
    else:
        user = request.user
        user = User.objects.filter(username = user.username)
        
        context = dict(
            user_form = User_Settings_Form(instance=request.user),
            password_form = Password_Change_Form(request.user),
            user = user,
        )
        return render(request,"settings.html",context)


def userDelete(request):
    user = request.user
    user.delete()
    return redirect("signup")