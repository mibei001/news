import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article  class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article(40,'Legistrative article','John','The Executive Branch','he principal mission of the legislative body is to make laws.','www.dummies.com','www.dummies.com/12.npg','December 15, 1791')
                   

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()

