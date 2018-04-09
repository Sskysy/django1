#encoding=utf-8

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models

def index(request):
	'''reqfund = models.ReqFundInfo.objects.get(pk=id)'''
	reqfunds = models.ReqFundInfo.objects.all()
	return render(request, 'index.html', {'reqfunds':reqfunds})

def agent(request):
	agents = models.AgentInfo.objects.all()
	return render(request, 'agent.html', {'agents':agents})

def medium(request):
	mediums = models.MediumInfo.objects.all()
	return render(request, 'medium.html', {'mediums':mediums})

def add(request):
	agents = models.AgentInfo.objects.all()
	mediums = models.MediumInfo.objects.all()
	return render(request, 'add.html', {'agents':agents, 'mediums':mediums})

def delete(request, id):
	pass

def add_action(request):
	req_date = request.POST.get('req_date')
	req_team = request.POST.get('req_team')
	req_account = request.POST.get('req_account')
	rapplicant= request.POST.get('rapplicant')
	ragent = request.POST.get('models.MediumInfo.objects.get(pk=agentinfo.id)')
	rmedium = request.POST.get('models.MediumInfo.objects.get(pk=mediuminfo.id)')
	ramount = request.POST.get('ramount')
	reb_proprotion = request.POST.get('reb_proprotion')
	rpay_way = request.POST.get('rpay_way')
	rpayment_date = request.POST.get('rpayment_date')
	rfund_state = request.POST.get('rfund_state')
	rauditor = request.POST.get('rauditor')
	rmanager = request.POST.get('rmanager')
	audit_state = request.POST.get('audit_state')
	extend_add = request.POST.get('rmedium')
	submit=request.POST.get('submit')
	models.ReqFundInfo.objects.create(req_date=req_date, req_team=req_team, req_account=req_account, rapplicant=rapplicant, ragent=ragent,
				rmedium=rmedium, ramount=ramount, reb_proprotion=reb_proprotion,rpay_way=rpay_way, rpayment_date=rpayment_date, rfund_state=rfund_state,
				rauditor=rauditor, rmanager=rmanager, audit_state=audit_state, extend_add=extend_add, submit=submit)
	reqfunds = models.ReqFundInfo.objects.all()
	return render(request, 'index.html', {'reqfunds':reqfunds})

def add_ag(request):
	return render(request, 'add_ag.html')

def add_ag_action(request):
	agency_company = request.POST.get('agency_company')
	contract_add = request.POST.get('contract_add')
	bank_account = request.POST.get('bank_account')
	subbranch_name = request.POST.get('subbranch_name')
	models.AgentInfo.objects.create(agency_company=agency_company, contract_add=contract_add, bank_account=bank_account, subbranch_name=subbranch_name)
	agents = models.AgentInfo.objects.all()
	return render(request, 'add_ag.html', {'agents':agents})

def add_am(request):
	return render(request, 'add_am.html')

def add_am_action(request):
	mtitle = request.POST.get('mtitle')
	account_way = request.POST.get('account_way')
	models.MediumInfo.objects.create(mtitle=mtitle, account_way=account_way)
	mediums = models.MediumInfo.objects.all()
	return render(request, 'add.html', {mediums:mediums})

