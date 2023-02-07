from services.overview_func import *
import unittest
    
class TestDatabaseFunctions(unittest.TestCase):
    
    def test_is_sku(self):
        self.assertTrue(is_sku_in_database('2222'))
        self.assertFalse(is_sku_in_database('xxx'))
        self.assertFalse(is_sku_in_database('0000'))
        
        
if __name__ == '__main__':
    unittest.main()