from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pickle
loaded_model = pickle.load(open('/home/adi/Desktop/ai_prj/demo/HBEATr/adv_app/deploy/random_forest_model_2', 'rb'))

def index(request):
    return render(request,'index.html')

def data(request):
    age=int(request.POST.get('age'))
    tresbps=float(request.POST.get('trestbps'))
    chol=float(request.POST.get('chol'))
    thalach=float(request.POST.get('thalach'))
    oldpeak=float(request.POST.get('oldpeak'))
    ca=float(request.POST.get('ca'))
    sex=str(request.POST.get('sex'))
    exp=str(request.POST.get('exp'))
    fbs=float(request.POST.get('fbs'))
    elec=str(request.POST.get('elec'))
    angina=str(request.POST.get('angina'))
    st=str(request.POST.get('st'))
    st2=str(request.POST.get('st2'))
    print(age,tresbps,chol,thalach,oldpeak,ca,sex,exp,fbs,elec,angina,st,st2)
    # age trestbps chol thalach oldpeak ca sex cp fbs restecg exang slope thal

    io = [age,tresbps,	chol,thalach,oldpeak,ca,sex,exp,fbs,elec,angina,st,st2]
    io1 = []
    io1.extend(io)
    if io[7] == 0:
        io1[7:8] = [0, 0, 1]
    elif io[7] == 1:
        io1[7:8] = [0, 0, 0]
    elif io[7] == 2:
        io1[7:8] = [1, 0, 0]
    else:
        io1[7:8] = [0, 1, 0]

    if io[11] == 0:
        io1[13:14] = [0, 1]
    elif io[11] == 1:
        io1[13:14] = [0, 0]
    else:
        io1[13:14] = [1, 0]

    if io[12] == 0:
        io1[15:16] = [0, 0, 1]
    elif io[12] == 1:
        io1[15:16] = [0, 0, 0]
    elif io[12] == 2:
        io1[15:16] = [1, 0, 0]
    else:
        io1[15:16] = [0, 1, 0]

    io1 = [io1]
    result = loaded_model.predict(io1)
    
    if(result == 1):
        ans=True
        print("You have a risk of Cardiovascular Disease!")
    else:
        ans=False
        print("Congratulations! You do not have any kind of Cardiovascular Risk!!")
    return render(request, 'ans.html',{'ans':ans})