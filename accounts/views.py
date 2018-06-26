from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm

def logout(request):
	"""
	Logs the user out
	"""
	auth.logout(request)
	messages.success(request, "You have succesfully been logged out")
	return redirect(reverse('index'))

def login(request):
	"""
	return the login page
	"""
	if request.method == 'POST':
		login_form = UserLoginForm(request.POST)

		if login_form.is_valid():
			user= auth.authenticate(username = request.POST['username'],
									password = request.POST['password'])
			messages.success(request, "You have succesfully logged in")


			if user:
				auth.login(user=user, request=request)
			else:
				login_form.add_error(None, "The username or password is incorrect")
	else:
		login_form = UserLoginForm()
	return render(request, 'login.html', {'login_form' : login_form})