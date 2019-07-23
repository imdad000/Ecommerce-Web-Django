from django.conf.urls import url
from . import views
app_name= 'imdad'
urlpatterns = [
    url(r'^home/$',views.home_page,name='home_page'),
    url(r'^email/$',views.login_and_signup,name='login_and_signup'),
    url(r'^login/$',views.check_otp,name='check_otp'),    
]