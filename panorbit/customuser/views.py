from django.shortcuts import render,redirect
import requests
from django.core.mail import send_mail
from django.conf import settings
import random 
from .models import Myuser,Otp
context={
	all:"Welcome Page"
}
def home_page(request):
	return render(request,"index.html",context)

def login_and_signup(request):
	if request.method == 'POST':
		try:
			email=request.POST['email']
			get_email = Myuser.objects.get(email=email)
			get_all = Myuser.objects.all()
			number = random.randrange(1000, 9999)
			subject = 'Your OTP (PANORBIT)'
			message = ' Your otp is '+str(number)
			Otp.objects.create(otp=number)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [email]
			send_mail( subject, message, email_from, recipient_list )
			return render(request,'signin.html')
		except Myuser.DoesNotExist:
			if len(request.POST.dict())>2:
				login_data = request.POST.dict()
				first_name = login_data.get('first_name')
				last_name = login_data.get('last_name')
				fathers_name = login_data.get('fathers_name')
				gender = login_data.get('gender')
				phone_number = login_data.get('phone_number')
				spouse_name = login_data.get('spouse_name')
				email = login_data.get('email')
				Myuser.objects.create(first_name=first_name,last_name=last_name,fathers_name=fathers_name,gender=gender,phone_number=phone_number,spouse_name=spouse_name,email=email)
				number = random.randrange(1000, 9999)
				subject = 'Your OTP (PANORBIT)'
				message = ' Your otp is '+str(number)
				Otp.objects.create(otp=number)
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [email]
				send_mail( subject, message, email_from, recipient_list )
				return render(request,'signin.html')
			else:
				return render(request,'edit.html')

def check_otp(request):
	if request.method == 'POST':
		get_otp = Otp.objects.all()
		otps = []
		for i in range(0,len(get_otp)):
			otps.append(get_otp[i].otp)
		otp = request.POST['otp']
		if int(otp) in otps:
			Otp.objects.get(otp=otp).delete()
			return render(request,'welcome.html')
		else:
			return render(request,'index.html')



