from django.shortcuts import render, redirect
from .forms import RegisterForm, inForm
import predict
from .models import LoanForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', context={'form': form})

def index(request):
    return render(request, 'index.html')

def infoForm(request):
    if request.method=='POST':
        form = inForm(request.POST)
        if form.is_valid():
            loanFile=LoanForm()
            loanFile.age=form.cleaned_data['age']
            loanFile.credit=form.cleaned_data['credit']
            loanFile.vouch=form.cleaned_data['guarantee']
            loanFile.income=form.cleaned_data['income']
            loanFile.house=form.cleaned_data['house']
            loanFile.user_id=request.user.id
            
            loanFile.decision=predict.predict([loanFile.age,loanFile.credit,loanFile.vouch,loanFile.income,loanFile.house])
            loanFile.save()
            print loanFile.decision
            print 'save successfully'
            return render(request, 'result.html')
    else:
        form=inForm()
        return render(request, 'infoForm.html',{'infoForm': inForm})
def result(request):
    return null

def home(request):
    return render(request, 'home.html')


