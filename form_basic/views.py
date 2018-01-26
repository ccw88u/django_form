from django.shortcuts import render
from form_basic.forms import ReguserForm

# Create your views here.

def index(request):
	return render(request, 'form_basic/index.html')

def reguser(request):
    form = ReguserForm()

    if request.method == "POST":
        form = ReguserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    print 'form_basic/reguser.html'
    return render(request, 'form_basic/reguser.html', {'form':form})  