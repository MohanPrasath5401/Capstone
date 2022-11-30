from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUP,SignUP2,Profile,Profile2,PostForm,comment
from .models import Post
from .models import Profile1 as MyProfile
from django.contrib.auth.models import User
from django.views.generic import UpdateView ,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin

# Create your views here.
@login_required(login_url="login")
def profile(request):
    return render(request,'userApp/profile.html')

@login_required(login_url="login")
def Profile_user(request,id1):
    u1 = User.objects.filter(id=id1)[0]
    context = {'user1':u1}
    return render(request,"userApp/profile_user.html",context)


def Loginpage(request):
    form = AuthenticationForm()
    context = {'form':form,'legend':'Login Now'}
    next = ""
    if request.GET:
        next = request.GET('next')
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        print('h1')
        if form.is_valid():
            print('h2')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            print('h3')
            if user is not None:
                print('h4')
                login(request,user)
                if next =="":
                    return redirect('profile')
                else:
                    return redirect(next)
            else:
                messages.warning(request,"username or password is incorrect")
    
    return render(request,'userApp/login.html',context)


def Register(request):
    u_form = SignUP()
    p_form = Profile()
    context = {'u_form':u_form,'p_form':p_form,"legend":"Register Yourself Today"}
    if request.method == 'POST':
       u_form = SignUP(request.POST)
       p_form = Profile(request.POST)
       print(u_form.is_valid())
       print(p_form.is_valid())
       if u_form.is_valid and p_form.is_valid():
            print('h2')
            u_form.save()
            p_form.save()
            messages.success(request,f"Account Created")
            return redirect('login')
    return render(request,"userApp/login.html",context)

def Signup(request):
    u_form = SignUP2()
    p_form = Profile2()
    context = {'u_form':u_form,'p_form':p_form,"legend":"Register Yourself Today Get Job"}
    if request.method == 'POST':
       u_form = SignUP2(request.POST)
       p_form = Profile2(request.POST)
       print(u_form.is_valid())
       print(p_form.is_valid())
       if u_form.is_valid and p_form.is_valid():
            print('h2')
            u_form.save()
            p_form.save()
            messages.success(request,f"Account Created")
            return redirect('login')
    return render(request,"userApp/login.html",context)

def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password changed successfully")
                return redirect('profile')
    
    fm = PasswordChangeForm(user=request.user)
    context = {'form':fm,'legend': "changed password"}
    return render(request,"userApp/login.html",context)

@login_required(login_url="login")
def CreatePost(request):
    form = PostForm()
    context = {'form':form,'legend':"POST NOW"}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            mark1 = form.save(commit=False)
            mark1.author = request.user
            form.save()
            return redirect("allpost")
    return render(request,'userApp/createpost.html',context)

@login_required(login_url="login")
def AllPost(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,"userApp/allpost.html",context)

@login_required(login_url="login")
def SpecificPost(request,id1):
    post = Post.objects.filter(id=id1)[0]
    context = {'post':post}
    return render(request,"userApp/onepost.html",context)

#Class based view
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     model = Post
     fields = ['title','content']
     template_name = 'userApp/createpost.html'
     login_url = '/login/'
    
     def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

     def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
     model = Post
     success_url = '/User/allpost/'

     def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def Comment(request,id1):
    form = comment()
    post = Post.objects.filter(id=id1)[0]
    comments = post.comment.all()
    if request.method == 'POST':
        form = comment(request.POST)
        if form.is_valid():
            mark1 = form.save(commit=False)
            mark1.post = post
            mark1.name = request.user
            form.save()
    context = {'form':form,'post1':post,'comments':comments}
    return render(request,'userApp/onepost.html',context)