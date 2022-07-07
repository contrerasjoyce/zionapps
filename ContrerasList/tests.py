from django.test import TestCase
from ContrerasList.views import Homerun
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from ContrerasList.models import Applicant,List

class MyMainPage(TestCase):  
    def test_root_url_resolves_to_mainpage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, Homerun)
    def test_only_saves_applicants_when_necessary(self): 
        self.client.get('/')        
        self.assertEqual(Applicant.objects.count(), 0)
      
class ListViewTest(TestCase):
 
    def test_uses_list_template(self):
        list_ = List.objects.create()        
        response = self.client.get(f'/ContrerasList/{list_.id}/')
        self.assertTemplateUsed(response, 'form.html')
     
   
    def test_displays_all_list_applicants(self):        
        list_ = List.objects.create()        
        Applicant.objects.create(nNames='Joyce', list=list_)        
        Applicant.objects.create(nNames='Contreras', list=list_)
   
    def test_passes_correct_list_to_template(self):       
        other_list = List.objects.create()        
        correct_list = List.objects.create()        
        response = self.client.get(f'/ContrerasList/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)  
 
class NewListTest(TestCase):   

    def test_redirects_after_POST(self):        
        response = self.client.post('/ContrerasList/new', data={'Name': 'MyNames','School': 'YourSchool','Precinct':'PrecinctId','NxtName': 'othername','Year': 'MySchoolYear','GPA': 'Mygrade'})                     
        new_list = List.objects.first()        
        self.assertRedirects(response, f'/ContrerasList/{new_list.id}/')
       
class NewApplicantTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):       
        other_list = List.objects.create()        
        correct_list = List.objects.create()        
        self.client.post(f'/ContrerasList/{correct_list.id}/add_applicant', data={'Name': 'MyNames','School': 'YourSchool','Precinct':'PrecinctId','NxtName': 'othername','Year': 'MySchoolYear','GPA': 'Mygrade'}) 
      
        self.assertEqual(Applicant.objects.count(), 1)        
        new_applicant = Applicant.objects.first()        
        self.assertEqual(new_applicant.nNames, '')       
        self.assertEqual(new_applicant.list, correct_list)
      
    def test_redirects_to_list_view(self):        
        other_list = List.objects.create()        
        correct_list = List.objects.create()        
        response = self.client.post(f'/ContrerasList/{correct_list.id}/add_applicant',data={'Name': 'MyNames','School': 'YourSchool','Precinct':'PrecinctId','NxtName': 'othername','Year': 'MySchoolYear','GPA': 'Mygrade'})   
        self.assertRedirects(response, f'/ContrerasList/{correct_list.id}/')
   
class ORM(TestCase):

    def test_saving_and_retrieving_applicants(self):
        list_ = List()        
        list_.save()
      
        first_applicant = Applicant()        
        first_applicant.nNames = 'The first list applicant' 
        first_applicant.list = list_ 
        first_applicant.save()        
               
        second_applicant = Applicant()      
        second_applicant.nNames = 'Applicant the second'
        second_applicant.list = list_         
        second_applicant.save()
       
        saved_list = List.objects.first()          
        self.assertEqual(saved_list, list_)
                 
        saved_applicants = applicant.objects.all()
        self.assertEqual(saved_applicants.count(), 2)
       
        first_saved_applicant = saved_applicants[0]
        second_saved_applicant = saved_applicants[1]             
        self.assertEqual(first_saved_applicant.nNames, 'The first list applicants')
        self.assertEqual(first_saved_applicants.list, list_)
        self.assertEqual(second_saved_applicants.nNames, 'Applicant the second')
        self.assertEqual(second_saved_applicants.list, list_)
