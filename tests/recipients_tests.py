from services.recipients_func import *
import unittest
    
class TestDatabaseFunctions(unittest.TestCase):
    
    def test_is_uid(self):
        self.assertFalse(is_userid_in_database('000'))
        self.assertTrue(is_userid_in_database('1111'))
        
        
if __name__ == '__main__':
    unittest.main()