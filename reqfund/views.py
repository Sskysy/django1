#encoding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
	'''reqfund = models.ReqFundInfo.objects.get(pk=id)'''
	reqfunds = models.ReqFundInfo.objects.all()
	return render(request, 'index.html', {'reqfunds':reqfunds})

def add(request):
	agents = models.AgentInfo.objects.all()
	mediums = models.MediumInfo.objects.all()
	return render(request, 'add.html', {'agents':agents, 'mediums':mediums})

def add_action(request):
	req_date = request.POST.get('req_date')
	req_team = request.POST.get('req_team')
	req_account = request.POST.get('req_account')
	rapplicant= request.POST.get('rappllicant')
	ragent = request.POST.get('ragent')
	rmedium = request.POST.get('rmedium')
	ramount = request.POST.get('ramount')
	reb_proprotion = request.POST.get('reb_proprotion')
	rpay_way = request.POST.get('rpay_way')
	rpayment_date = request.POST.get('rpayment_data', '年/月/日')
	rfund_state = request.POST.get('rfund_state')
	rauditor = request.POST.get('rauditor')
	rmanager = request.POST.get('rmanager')
	audit_state = request.POST.get('audit_state')
	extend_add = request.POST.get('extend_add')
	submit = request.POST.get('submit')
	models.ReqFundInfo.objects.create(req_date=req_date, req_team=req_team, req_account=req_account, rapplicant=rapplicant, ragent=ragent,
				rmedium=rmedium, ramount=ramount, reb_proprotion=reb_proprotion,rpay_way=rpay_way, rpayment_date=rpayment_date, rfund_state=rfund_state,
				rauditor=rauditor, rmanager=rmanager, audit_state=audit_state, extend_add=extend_add, submit=submit)
	reqfunds = models.ReqFundInfo.objects.all()
	return render(request, 'index.html', {'reqfunds':reqfunds})

