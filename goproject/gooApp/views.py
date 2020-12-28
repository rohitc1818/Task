from django.shortcuts import render,redirect,HttpResponse
from gooApp.forms.signupform import CustomerCreationForm
from gooApp.forms.infoform import InfoForm
from gooApp.models import Info
from django.views.generic import View


# Create your views here.

def signup(request):
    if request.method == 'GET':
        form = CustomerCreationForm()
        return render(request, template_name='gooApp/signup.html', context={'form': form})
    else:
        if request.method == 'POST':
            form = CustomerCreationForm(request.POST or None)
            if form.is_valid():
                user = form.save()
                user.email = user.username
                user.save()
                return redirect('homepage')
            context = {
                "form": form,
                }
            return render(request,template_name='gooApp/signup.html',context=context)

class Home(View):
    def get(self,request):
        if request.method == 'GET':
            print('True')
            form = InfoForm()
            return render(request,'gooApp/home.html',{'form':form})

    def post(self,request):
        print('this function exucuted!!!')
        if request.method == 'POST':

            print(request.POST)
            form = InfoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return  redirect('loginpage')
            context = {
                "form": form
            }
            return render(request, 'gooApp/home.html', context=context)


def login(request):
    details = Info.objects.all()
    return render(request,'gooApp/login.html',{'details':details})



