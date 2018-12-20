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
   # 
    def test_no_conc_file(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_concordance_table('fake_concordance.txt')
   # # 
    def test_01(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       # print(conc.stop_table.get_table())
       conc.load_concordance_table('file1.txt')
       # print(conc.concordance_table.get_table())
       conc.write_concordance("file1_con.txt")
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))
   # 
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
   # 
    def test_buggy(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("stop_words.txt")
        conc.write_concordance("stop_words_con.txt")
        self.assertTrue(filecmp.cmp("stop_words_con.txt", "blank.txt"))
    
    def test_buggy2(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("all_punc.txt")
        conc.write_concordance("all_punc_con.txt")
        self.assertTrue(filecmp.cmp("all_punc_con.txt", "blank.txt"))
        
    def test_buggy3(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("all_digits.txt")
        conc.write_concordance("all_digits._con.txt")
        self.assertTrue(filecmp.cmp("all_digits._con.txt", "blank.txt"))
        
    def test_buggy4(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("same.txt")
        conc.write_concordance("same_con.txt")
        self.assertTrue(filecmp.cmp("same_con.txt", "same_sol.txt"))
    # # 
    # def test_war_and_peace(self):
    #     conc = Concordance()
    #     conc.load_stop_table("stop_words.txt")
    #     conc.load_concordance_table("war_and_peace.txt")
    #     conc.write_concordance("war_and_peace_con.txt")
    # 
    # def test_santa(self):
    #     conc = Concordance()
    #     conc.load_stop_table("stop_words.txt")
    #     conc.load_concordance_table("Santa.txt")
    #     conc.write_concordance("Santa_con.txt")
    #     self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))
    
    # def test_the_file(self):
    #     conc = Concordance()
    #     conc.load_stop_table("stop_words_minus_the.txt")
    #     conc.load_concordance_table("file_the.txt")
    #     conc.write_concordance("file_the_con.txt")
    


if __name__ == '__main__':
   unittest.main()
