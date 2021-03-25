from django.http import HttpResponse
from django.shortcuts import render
import joblib
import pickle


def home(request):
	return render(request,"home.html")


def getPred(cie1,cie2,presenty,behaviour):
	lr=joblib.load(open('marks.sav','rb'))
	prediction=round(lr.predict([[cie1,cie2,presenty,behaviour]])[0],2)

	if prediction >30:
		return 30
	else:

		return prediction
	print(prediction)

def result(request):
	cie1=int(request.GET['cie1'])
	
	cie2=int(request.GET['cie2'])
	presenty=int(request.GET['presenty'])
	behaviour=int(request.GET['behaviour'])
	
	result=getPred(cie1,cie2,presenty,behaviour)
	print(result)
	return render(request,'result.html',{'result':result})


    
  