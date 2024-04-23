
from django.test import TestCase, Client

#Test of the app's sole URL pattern

class ClubStintsAppTest(TestCase):
    def test_club_stints_app_test(self):
        hypothetical_user = Client()
        hypothetical_request = hypothetical_user.get("")
        self.assertEqual(hypothetical_request.status_code, 200) 
        
        



        



        

        
        
    
