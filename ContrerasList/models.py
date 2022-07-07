from django.db import models

class Applicant(models.Model):
	nFullName = models.TextField(default='')
	nAddress = models.TextField(default='')
	aage = models.IntegerField(default='0')
	nGenders = models.TextField(default='')
	acontumber = models.IntegerField(default='0')
	aemailAddress = models.TextField(default='')
	agname = models.TextField(default='')
	asoi = models.TextField(default='')
	nAIncome = models.IntegerField(default='0')
	ausername = models.TextField(default='')
	apassword = models.TextField(default='')
	sstatus = models.TextField(default='')

class School(models.Model):
	applicant = models.ForeignKey(Applicant,default=None, on_delete=models.CASCADE)
	NMSchool = models.TextField(default='')
	slevel = models.TextField(default='')
	nStudentId = models.TextField(default='')
	nGPA = models.IntegerField(default='0')
	sid  = models.ImageField(default='')
	sgwa = models.ImageField(default='')

class Admin(models.Model):
	adminu = models.TextField(default='')
	adminp = models.TextField(default='')
