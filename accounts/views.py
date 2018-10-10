from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm

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
				return (redirect(reverse('index')))
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
                
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
        
def account_view(request):
	_user = request.user
	prof = _user.profile
	data = {'user': prof.user, 'full_name': prof.full_name, 'phone_number': prof.phone_number, 'country': prof.country, 'postcode': prof.postcode, 'town_or_city': prof.town_or_city, 'street_address1': prof.street_address1, 'street_address2': prof.street_address2, 'county': prof.county }

	if request.method == "POST":
		method_form = ProfileForm(request.POST, instance=request.user.profile)
		if method_form.is_valid():
			prof = method_form.save()
			
			return redirect(reverse('accounts:your_account'))
	else:
		method_form = ProfileForm(initial=data)
	return render(request, 'account_view.html', { 'user': _user, 'method_form': method_form })