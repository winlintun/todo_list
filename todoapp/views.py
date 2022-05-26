from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Mytodo
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#@login_required(login_url='/mytodo/login/')
def home(request):
	all_item = Mytodo.objects.all()
	return render(request, 'todoapp/home.html', {'all_item': all_item})


def add_item(request):
	title = request.POST['title']
	body = request.POST['body']

	new_item = Mytodo(title=title, body=body)
	new_item.save()
	messages.success(request, 'Successfully Added Item')
	return redirect('todoapp:home')


def delete_item(request, item_id):
	item = Mytodo.objects.get(pk=item_id)
	item.delete()
	messages.success(request, 'Successfully Delete Item')
	return redirect('todoapp:home')


def singup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password1 = request.POST['password1']

		if password == password1:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username is already used.')
				return redirect('todoapp:singup')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'Email address is already used.')
				return redirect('todoapp:singup')
			else:
				user = User.objects.create_user(username=username, email=email, password=password)
				messages.success(request, 'Successfully Register!')
				return redirect('todoapp:home')
		else:
			messages.info(request, 'Wrong Password!')
			return redirect('todoapp:singup')
	return render(request, 'todoapp/singup.html')


def singin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, 'Successfully Login!')
			return redirect("todoapp:home")
		else:
			messages.info(request, 'Username and password are wrong!')

	return render(request, 'todoapp/singin.html')


def singout(request):
	logout(request)
	messages.success(request, 'Successfully Logout!')
	return redirect('todoapp:home')
