from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def get_index(request):
    return render(request, 'cakeshop/cake_list.html')


def get_register(request):
    if request.method == 'POST':  # kiểm tra xem yêu cầu có phải là phương thức POST hay không
        # lấy giá trị của trường username từ form
        username = request.POST['username']
        email = request.POST['email']  # lấy giá trị của trường email từ form
        # lấy giá trị của trường password1 từ form
        password1 = request.POST['password1']
        # lấy giá trị của trường password2 từ form
        password2 = request.POST['password2']
        if len(password1) < 6:
            messages.error(request, 'Password must longer than 6 characters!'),
            return render(request, 'authentication/register.html')
        if password1 == password2:  # kiểm tra xem hai trường password có giống nhau hay không
            # kiểm tra xem username đã tồn tại trong cơ sở dữ liệu chưa
            if User.objects.filter(username=username).exists():
                # nếu đã tồn tại, hiển thị thông báo lỗi
                messages.error(request, 'Username is already taken.')
                # return redirect('register')
                return render(request, 'authentication/register.html')
            else:  # nếu chưa tồn tại, tạo user mới
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()  # lưu user vào cơ sở dữ liệu
                # hiển thị thông báo thành công
                messages.success(request, 'You have successfully registered.')
                # return redirect('login') # chuyển hướng người dùng đến trang đăng nhập
                return redirect("/authentication/login/")

        else:  # nếu hai trường password không giống nhau, hiển thị thông báo lỗi
            er = messages.error(request, 'Passwords do not match.')
            print(er)
            # return redirect('register')
            return render(request, 'authentication/register.html')
    else:  # nếu yêu cầu không phải là phương thức POST, trả về template đăng ký
        return render(request, 'authentication/register.html')


def get_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # check_value = request.POST.get('check')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # if check_value:
            #     request.session['user_id'] = user.id
            # request.session['username'] = username
            return redirect('/')
        else:
            messages.error(request, 'Email or password not correct!')
            # Invalid login
            # return render(request, 'authentication/login.html', {'error': 'Invalid login credentials.'})
    context = {}
    return render(request, 'authentication/login.html', context)


def get_logout(request):
    logout(request)
    return redirect("/authentication/login/")
