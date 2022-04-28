from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['uname']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        emailadr = request.POST['email']
        password = request.POST['psw']
        cpassword = request.POST['cpsw']

        print(password)
        print(cpassword)
        if (username or password or emailadr) != '':
            print('STARTED')
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    print('user exits')
                    messages.info(request, 'user exists')
                    return redirect('register')
                elif User.objects.filter(email=emailadr).exists():
                    print('email exits')
                    return redirect('register')
                else:
                    print('user SSSexits')
                    user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                    email=emailadr,
                                                    password=password)
                    user.save()
                    return render(request, 'log.html')
            else:
                messages.info(request, 'Passwords not matched')
                print("password not match")
                return redirect('register')
        else:
            messages.info(request, "Can't empty fields")
            return redirect('register')
    return render(request, 'register.html', )


def login(request):
    if request.method == 'POST':
        u_name = request.POST['user_name']
        p_ass = request.POST['pass']

        user = auth.authenticate(username=u_name, password=p_ass)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid user')
            # return redirect('log')
    return render(request, 'log.html', )



def logout(request):
    auth.logout(request)
    return redirect('/')



