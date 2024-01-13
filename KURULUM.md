- [x] pip install virtualenv
- [x] virtualenv env
- [x] env\Scripts\activate (Çalışmazsa) source env/Scripts/activate
- [x] pip install -r requirements.txt
- [x] python manage.py createsuperuser (Hiç bir yer boş kalmıyacak first_name ve last_name)
Eklenmezse Donate kısmı çalışmaz
- [x] Admin panelden Donation Types kısmına ilk (Tek Seferlik) sonra (Aylık) ekliyoruz Eklenmezse Donate kısmı çalışmaz
- [x] python manage.py migrate --run-syncdb

HATA KODLARI
- [x] (Geçersiz imza) Sebebi kullanıcının first_name & Last_name alanlarının boş bırakılması
- [x] (502) Sebebi kullanıcının 6. maddenin yapılmaması
