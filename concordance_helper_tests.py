import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):
    
    def test_no_stop_file(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_stop_table("fake_stop_words.txt")
        # # print(conc.stop_table.get_table())
        # conc.load_concordance_table('file1.txt')
        # # print(conc.concordance_table.get_table())
        # conc.write_concordance("file1_con.txt")
        # self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))
   
    def test_no_conc_file(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_concordance_table('fake_concordance.txt')
   # 
    def test_01(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       # print(conc.stop_table.get_table())
       conc.load_concordance_table('file1.txt')
       # print(conc.concordance_table.get_table())
       conc.write_concordance("file1_con.txt")
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))
   
    def test_02(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file2.txt")
       conc.write_concordance("file2_con.txt")
       self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))
   #  # 
    def test_03(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("declaration.txt")
       conc.write_concordance("declaration_con.txt")
       self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))
       
    
if __name__ == '__main__':
   unittest.main()
