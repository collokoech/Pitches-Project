import unittest

from app.models import User, Post

class ProjectTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='collokoech4', email='collokoech4@gmail.com', password='1234')
        self.new_post = Post()
        

if __name__ == '__main__':
    unittest.main()