from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from BookApp.forms import RegisterForm, LoginForm
from BookApp.models import User, Publisher, Book, Autthor
from BookApp.PictureCode.CodeImg import create_img
from django.http import JsonResponse

class RegisterView(View):
    '''
    用户注册操作
    '''


    def get(self, request):
        return render(request, 'register.html')


    def post(self, request):
        #接收用户注册输入的数据，传递给form表单进行数据验证
        register_forms = RegisterForm(request.POST)
        #判断forms组件是否返回错误信息
        if register_forms.is_valid():
            #说明数据合法， 将用户数据保存到数据库中
            #从forms组件中取出用户数据
            username = register_forms.cleaned_data.get('username')
            password = register_forms.cleaned_data.get('password')
            email = register_forms.cleaned_data.get('email')
            #校验验证码
            #获取用户的验证码
            img_dode = request.POST.get('img_code')
            #获取保存在session中的验证码
            code = request.session['code']
            if img_dode == code:
                #验证码正确，将数据保存到数据库中
                User.objects.create(username= username, password= password, email= email)
                return redirect('/login/')
            else:
                return render(request, 'register.html', {'code_error': '验证码错误'})
        else:
            #数据不合法
            return render(request, 'register.html', locals())


def CodeImg(request):
    img, text = create_img()
    #将验证码保存到 session
    request.session['code']=text
    return HttpResponse(img, content_type='image/png')


def UsernameCount(request, username):
    #用户是否重复
    count = User.objects.filter(username=username).count()
    #ajax 请求接收的json类型的响应
    return JsonResponse({'code': '200', 'errmsg': 'ok', 'count': count})


class LoginView(View):
    '''
    用户登录
    '''


    def get(self, request):
        return render(request, 'login.html')


    def post(self,request):
        login_forms = LoginForm(request.POST)
        if login_forms.is_valid():
            username = login_forms.cleaned_data.get('username')
            password = login_forms.cleaned_data.get('password')
            user = User.objects.filter(username= username, password= password)
            if user:
                return redirect('/index/')
            else:
                return render(request, 'login.html', {'errormsg': '账号或密码错误'})
        else:
            return render(request, 'login.html', {'errormsg': '账号或密码错误'})


def index(request):
    #响应首页
    return render(request, 'index.html')


def publisher_list(request):
    # 响应出版社列表页
    #从数据库中获取出版社的信息
    publisher = Publisher.objects.all()
    return render(request, 'publisher_list.html', locals())


def publisher_add(request):
    #添加出版社信息
    if request.method == 'POST':
        # 获取用户提交的数据
        name = request.POST.get('name')
        address = request.POST.get('address')
        #将数据保存到数据库中
        Publisher.objects.create(name= name, address= address)
        #数据保存成功， 重定向到列表页
        return redirect('/publisher_list/')
    return render(request, 'add_publisher.html')


def publisher_del(request):
    id = request.GET.get('id')
    Publisher.objects.filter(id= id).delete()
    return redirect('/publisher_list/')


class EditPublisher(View):

    def get(self, request):
        #向用户展示修改前的信息
        id = request.GET.get('id')
        edit_data = Publisher.objects.get(id= id)
        return render(request, 'edit_publisher.html', locals())


    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        edit_data = Publisher.objects.filter(id= id)
        edit_data.update(name= name, address= address)
        return redirect('/publisher_list/')


def book_list(request):
    # 响应出版社列表页
    #从数据库中获取出版社的信息
    book = Book.objects.all()
    return render(request, 'book_list.html', locals())


def book_add(request):
    #添加图书信息
    if request.method == 'POST':
        # 获取用户提交的数据
        name = request.POST.get('name')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        publisher_id = request.POST.get('publisher_id')
        #将数据保存到数据库中
        Book.objects.create(name= name, price= price, inventory= inventory, publisher_id= publisher_id)
        #数据保存成功， 重定向到列表页
        return redirect('/book_list/')
    publisher = Publisher.objects.all()
    return render(request, 'add_book.html', locals())


def book_del(request):
    id = request.GET.get('id')
    Book.objects.filter(id= id).delete()
    return redirect('/book_list/')


class EditBook(View):

    def get(self, request):
        #向用户展示修改前的信息
        id = request.GET.get('id')
        edit_data = Book.objects.get(id= id)
        publisher = Publisher.objects.all()
        return render(request, 'edit_book.html', locals())


    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        publisher_id = request.POST.get('publisher_id')
        edit_data = Book.objects.filter(id= id)
        edit_data.update(name= name,
                         price= price,
                         inventory= inventory,
                         publisher_id= publisher_id)
        return redirect('/book_list/')


def author_list(request):
    # 响应作者列表页
    #创建一个列表用于返回数据
    data = []
    #从数据库中获取作者的信息
    authors = Autthor.objects.all()
    for author in authors:
        books = author.book.all()
        for book in books:
            data.append((author.id,author.name,book.name))
    return render(request, 'author_list.html', locals())

class AddAuthor(View):

    def get(self, request):
        #将作品也就是图书名称传递到html，进行选择
        book = Book.objects.all()
        return render(request, 'add_author.html', locals())

    def post(self, request):
        name = request.POST.get('name')
        books = request.POST.get('books')
        author = Autthor.objects.create(name= name)
        author.book.add(books)
        return redirect('/author_list/')


def check_author(request):
    #查看作者的作品
    id = request.GET.get('id')
    author_name = Autthor.objects.get(id= id)
    print(author_name)
    book = Book.objects.filter(autthor__id= id)
    print(book)
    return render(request, 'check_author.html', locals())

def author_del(request):
    id = request.GET.get('id')
    Autthor.objects.filter(id= id).delete()
    return redirect('/author_list/')


class EditAuthor(View):

    def get(self, request):
        #向用户展示修改前的信息
        id = request.GET.get('id')
        edit_data = Autthor.objects.get(id= id)
        book = Book.objects.all()
        return render(request, 'edit_author.html', locals())


    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        books = request.POST.get('books')
        edit_data = Autthor.objects.get(id= id)
        edit_data.name = name
        edit_data.book.set(books)
        edit_data.save()
        return redirect('/author_list/')