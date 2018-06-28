from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm

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

			if user:
				auth.login(user=user, request=request)
				messages.success(request, "You have succesfully logged in")
			else:
				login_form.add_error(None, "The username or password is incorrect")
	else:
		login_form = UserLoginForm()
	return render(request, 'login.html', {'login_form' : login_form})
	
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})