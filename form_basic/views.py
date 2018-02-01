# -*- coding: utf-8 -*-
from django.shortcuts import render
from form_basic.forms import ReguserForm, websiteForm

# Create your views here.

def index(request):
	return render(request, 'form_basic/index.html')

def statictest(request):
    return render(request, 'form_basic/statictest.html')

def mediatest(request):

    return render(request, 'form_basic/mediatest.html')

def testforloop(request):
    formlst = [('name', 'owen'), ('tel', '09XXXXXXXX'), ('addr', '台北市內湖路......')]
    return render(request, 'form_basic/testforloop.html', {'formlst':formlst} )

def reguser(request):
    form = ReguserForm()

    if request.method == "POST":
        ##form = ReguserForm(request.POST)
        form = ReguserForm(request.POST, request.FILES)
        if form.is_valid():

            # Check if they provided a profile picture
            #if 'profile_pic' in request.FILES:
                #print('found it')
                # If yes, then grab it from the POST form reply                
                #form.profile_pic = request.FILES['profile_pic']
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    print 'form_basic/reguser.html'
    return render(request, 'form_basic/reguser.html', {'form':form})  


def websiteadd(request):
    form = websiteForm()

    ##用來判斷表單是否被呼叫儲存
    registered = False
    if request.method == "POST":
        ##form = ReguserForm(request.POST)
        form = websiteForm(request.POST)
        if form.is_valid():
            registered = True
            form.save(commit=True)
        else:
            print('ERROR FORM INVALID')   

    return render(request, 'form_basic/websiteadd.html', {'form':form, 'registered':registered})    