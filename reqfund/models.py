#encoding=utf-8
from django.db import models

class ReqFundInfo(models.Model):
	req_date = models.CharField(max_length=20, default='')
	req_team = models.CharField(max_length=10)
	req_account = models.CharField(max_length=20, default='')
	rapplicant= models.CharField(max_length=10, default='')
	ragent = models.ForeignKey('AgentInfo', null=True)
	rmedium = models.ForeignKey('MediumInfo', null=True)
	ramount = models.CharField(max_length=5, default='')
	reb_proprotion = models.CharField(max_length=10,default='')
	rpay_way = models.CharField(max_length=2, default='')
	rpayment_date = models.CharField(max_length=20, default='')
	rfund_state = models.CharField(max_length=3, default='')
	rauditor = models.CharField(max_length=10, default='')
	rmanager = models.CharField(max_length=10, default='')
	audit_state = models.CharField(max_length=3, default='')
	extend_add = models.CharField(max_length=20, default='')
	submit = models.CharField(max_length=1, default='')
	isDelete = models.BooleanField(default=False)
	def __str__(self):
		return self.req_team.encode('utf-8')
	
class AgentInfo(models.Model):
	agency_company = models.CharField(max_length=10)
	contract_add = models.CharField(max_length=40)
	bank_account = models.CharField(max_length=20)
	subbranch_name = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)
	def __str__(self):
		return self.agency_company.encode('utf-8')


class MediumInfo(models.Model):
	mtitle = models.CharField(max_length=10)
	account_way = models.CharField(max_length=3, default='CPC')
	isDelete = models.BooleanField(default=False)
	def __str__(self):
		return self.mtitle.encode('utf-8')

