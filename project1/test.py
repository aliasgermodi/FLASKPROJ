from app import app
import unittest

#Word 'test' has to be the first word on the each function to run test.

class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that login page loads properly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure that login runs correctly with correct credentials
    def test_correct_page_login(self):
        tester = app.test_client(self)
        response = tester.post(
		'/login', 
		data=dict(username='admin', password='admin'), 
		follow_redirects=True)
        self.assertIn(b'You were logged in.', response.data)


    # Ensure that login runs correctly with incorrect credentials
    def test_incorrect_logine_page(self):
	tester = app.test_client(self)
        response = tester.post(
		'/login', 
		data=dict(username='w', password='w'), 
		follow_redirects=True)
        self.assertIn(b'Invalid Credentials. Please try again.', response.data)
        
	
    # Ensure that logout page loads properly	
    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
		'/login', 
		data=dict(username='admin', password='admin'), 
		follow_redirects=True)
	response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You were logged out', response.data)

    # Ensure that main page has login
    def test_main_route(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to login first.' in response.data) 	
 
    #Ensure post show up on the main page from database
    def test_post_show_up(self):
        tester = app.test_client(self)
        response = tester.post(
		'/login', 
		data=dict(username='admin', password='admin'), 
		follow_redirects=True)
        self.assertIn(b'Well', response.data)
	
if __name__ == '__main__':
    unittest.main()
