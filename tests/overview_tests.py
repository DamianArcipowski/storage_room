import unittest
from services.overview_func import *

class TestDatabaseFunctions(unittest.TestCase):
    
    def insert_goods(self):
        self.assertEquals(add_goods_to_database('fleece', '1525234', 'pcs', 15))
        
if __name__ == '__main__':
    unittest.main()