from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



    def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('ziontable')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
                       raise e                  
                   time.sleep(0.5)  
                 
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_browser_title(self):
        self.browser.get('http://localhost:8000/')
        #self.browser.get(self.live_server_url)
        self.assertIn('CITY of DASMARINAS',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CITY of DASMARINAS', header_text)

        inputbox1 = self.browser.find_element_by_id('StudentID')
        self.assertEqual(inputbox1.get_attribute('placeholder'), 'InputID')
        inputbox1.send_keys('TUPC 18 0725')
        time.sleep(1)

        inputbox2 = self.browser.find_element_by_id('CompleteName')
        self.assertEqual(inputbox2.get_attribute('placeholder'), 'First/Middle/LastName')
        inputbox2.send_keys('Joyce Romina Contreras')
        time.sleep(1)

        inputbox3 = self.browser.find_element_by_id('Address')
        self.assertEqual(inputbox3.get_attribute('placeholder'), 'Full Address')
        inputbox3.send_keys('Blk 18 Lot 13 Laos St. Salawag, Dasmarinas City')
        time.sleep(1)

        inputbox4 = self.browser.find_element_by_id('Gender')
        self.assertEqual(inputbox4.get_attribute('placeholder'),'F/M/Others')
        inputbox4.send_keys('F')
        time.sleep(1)

        inputbox6 = self.browser.find_element_by_id('MothersName')
        self.assertEqual(inputbox6.get_attribute('placeholder'),'First/Middle/Last Name')
        inputbox6.send_keys('Miriam C. Mallari')
        time.sleep(1)

        inputbox7 = self.browser.find_element_by_id('MOccupation')
        self.assertEqual(inputbox7.get_attribute('placeholder'),'Occupations')
        inputbox7.send_keys('OFW')
        time.sleep(1)

        inputbox8 = self.browser.find_element_by_id('FathersName')
        self.assertEqual(inputbox8.get_attribute('placeholder'),'First/Middle/Last Name')
        inputbox8.send_keys('Deiloe M. Mallari')
        time.sleep(1)

        inputbox9 = self.browser.find_element_by_id('FAOccupation')
        self.assertEqual(inputbox9.get_attribute('placeholder'),'Occupations')
        inputbox9.send_keys('Machinist')
        time.sleep(1)

        inputbox10 = self.browser.find_element_by_id('Annual Income')
        self.assertEqual(inputbox10.get_attribute('placeholder'),'Input Income')
        inputbox10.send_keys('20,000')
        time.sleep(1)

        btnSubmit = self.browser.find_element_by_id('rbtnsubmit')
        btnSubmit.click()
        time.sleep(2)
        
        inputbox11 = self.browser.find_element_by_id('School')
        self.assertEqual(inputbox11.get_attribute('placeholder'),'Your School')
        inputbox11.send_keys('TUPC')
        time.sleep(1)

        inputbox12 = self.browser.find_element_by_id('SAddress')
        self.assertEqual(inputbox12.get_attribute('placeholder'),'Present School')
        inputbox12.send_keys('Salawag Ave. Dasmarinas City')
        time.sleep(1)

        inputbox13 = self.browser.find_element_by_id('YrSection')
        self.assertEqual(inputbox13.get_attribute('placeholder'),'Yr&Sec.')
        inputbox13.send_keys('BSIE-ICT')
        time.sleep(1)

        inputbox14 = self.browser.find_element_by_id('ngpa')
        self.assertEqual(inputbox14.get_attribute('placeholder'),'Average')
        inputbox14.send_keys('94')
        time.sleep(1)

        inputbox15 = self.browser.find_element_by_id('nawards')
        self.assertEqual(inputbox15.get_attribute('placeholder'),'Recieved Awards')
        inputbox15.send_keys('Best in Technical Drawing')
        time.sleep(1)

        inputbox16 = self.browser.find_element_by_id('ncerts')
        self.assertEqual(inputbox16.get_attribute('placeholder'),'Recieved Certificates')
        inputbox16.send_keys('Top 3 in class')
        time.sleep(1)

        inputbox17 = self.browser.find_element_by_id('nprecincts')
        self.assertEqual(inputbox17.get_attribute('placeholder'),'prercincts')
        inputbox17.send_keys('0420B')
        time.sleep(1)

        inputbox18 = self.browser.find_element_by_id('apScholar')
        self.assertEqual(inputbox18.get_attribute('placeholder'),'Apllied Scholarship')
        inputbox18.send_keys('Full Scholarship')
        time.sleep(1)

        btnSubmit = self.browser.find_element_by_id('rbtnsubmit')
        btnSubmit.click()
        time.sleep(2)