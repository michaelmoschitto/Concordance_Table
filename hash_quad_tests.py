import unittest
from hash_quad import *

class TestList(unittest.TestCase):
    
    def test_cat(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash('cat'), 3)
        ht.insert('cat', 3)
        ht.insert('u', 5)
        ht.insert('e', 9)
        self.assertEqual(ht.get_num_items(), 3)
        ht.insert('f', 10)
        # ht.insert('o', 5)
        # ht.insert('o', 5)
        self.assertEqual(ht.get_num_items(), 4)
        # self.assertEqual(ht.get_table(), [None, ('u', [5]), None, None, None, None, None, None, None, None, None, ('e', [9]), ('f', [10]), ('cat', [3, 5]), None])
        self.assertEqual(ht.get_all_keys(), ['u', 'e', 'f', 'cat'])
    
    
    def test_01a(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_table_size(), 7)
    
    def test_01b(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_num_items(), 0)
    
    def test_01c(self):
        ht = HashTable(7)
        self.assertAlmostEqual(ht.get_load_factor(), 0)
    
    def test_01d(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_all_keys(), [])
    # 
    def test_01e(self):
        ht = HashTable(7)
        self.assertEqual(ht.in_table("cat"), False)
    # 
    def test_01f(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_value("cat"), None)
    # 
    def test_01g(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)
    # 
    def test_01h(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)
        self.assertEqual(ht.horner_hash("CaT"), 5)
    
    def test_increase_table_size(self):
        ht = HashTable(10)
        ht.insert('cat', 0)
        # ht.insert('cat', 1)
        ht.insert('bat', 1)
        ht.insert('dat', 2)
        ht.insert('tad', 3)
        ht.insert('at', 4)
        # ht.increase_table_size()
    
    def test_quad_prob_append(self):
        ht = HashTable(10)
        ht.insert('a', 1)
        self.assertEqual(ht.horner_hash('a'), 7)
        ht.insert('k', 1)
        self.assertEqual(ht.horner_hash('k'), 7)
        # ht.insert('k', 2)
        self.assertTrue(ht.in_table('k'))
    
    
    def test_in_and_get_table_after_probing(self):
        ht = HashTable(10)
        ht.insert('cat', 0)
        ht.insert('act', 1)
        # print(ht.get_table())
        self.assertTrue(ht.get_index('act'), 3)
        self.assertTrue(ht.in_table('act'))
        self.assertTrue(ht.get_value('act'), 1)
    
    def test_similar_hashes(self):
        ht = HashTable(10)
        # self.assertEqual(ht.horner_hash("tad"), 3)
        # self.assertEqual(ht.horner_hash("at"), 3)
        # self.assertEqual(ht.horner_hash("dat"), 3)
        # self.assertEqual(ht.horner_hash("g"), 3)
        # self.assertEqual(ht.horner_hash('{'), 3)
        self.assertEqual(ht.horner_hash('cat'), 2)
        self.assertEqual(ht.horner_hash('act'), 2)
        self.assertEqual(ht.horner_hash('tac'), 2)
        self.assertEqual(ht.horner_hash('tca'), 2)
        self.assertEqual(ht.horner_hash('atc'), 2)
    
    def test_rehash(self):
        ht = HashTable(10)
        ht.insert('cat', 0)
        # print(ht.get_table())
        ht.insert('tac', 0)
        # print(ht.get_table())
        ht.insert('act', 0)
        # print(ht.get_table())
        ht.insert('cta', 0)
        # print(ht.get_table())
        ht.insert('tca', 0)
        # print(ht.get_table())
        ht.insert('atc',0)
        # print(ht.get_all_keys())
        self.assertEqual(ht.get_all_keys(),['cat', 'tca', 'cta', 'tac', 'act', 'atc'] )
        # print(ht.get_table())
    
    
    def test_num_items(self):
        ht = HashTable(10)
        ht.insert('cat', 0)
        ht.insert('in', 0)
        ht.insert('the', 0)
        ht.insert('hat', 0)
        self.assertEqual(ht.get_num_items(), 4)
    
    
    
    
    
    
    # 
    #     # # self.assertEqual(ht.horner_hash('ad'), 0)
    #     # self.assertEqual(ht.horner_hash("cat"), 2)
    #     # self.assertEqual(ht.horner_hash("bat"), 1)
    #     # self.assertEqual(ht.horner_hash("S"), 3)
    #     # self.assertEqual(ht.horner_hash("P"), 0)
    # 
    # 
    # 
    # 
    def test_quadratic_probing(self):
        ht = HashTable(20)
        ht.insert('P', -1)
        ht.insert('cat', 0)
        ht.insert('bat', 1)
        # the next three all hash to the same value
        ht.insert('dat', 2) #first collision at original hash
        ht.insert('tad', 3) #1^2 away
        ht.insert('at', 4) #2^2 away
        ht.insert('g', 5) #3^2 away
        self.assertAlmostEqual(ht.get_load_factor(), 7 / 20)    
        ht.insert('{', 6) #4^2 away, maps to the last item in the array 
        ht.insert('S', 7) #5^2 away. Check to make sure that the quadratic probing makes it all the way around the list
        # self.assertEqual(ht.get_table(), [('P', [-1]), ('bat', [1]), ('cat', [0]), ('dat', [2]), ('tad', [3]), None, None, ('at', [4]), ('S', [7]), None, None, None, ('g', [5]), None, None, None, None, None, None, ('{', [6])])
        self.assertEqual(ht.get_all_keys(), ['P', 'bat', 'cat', 'dat', 'tad', 'at', 'S', 'g', '{'])
        # ssertEqual(ht.get_table(), [('{', [6]), ('S', [7]), None, ('dat', [2]), None, None, None, ('at', [4]), ('bat', [1]), None, None, None, None, None, None, None, None, None, None, None, None, ('g', [5]), None, None, None, None, ('cat', [0]), None, None, ('tad', [3]), None, None, None, None, None, None, None, None, None, ('P', [-1]), None])
    
    def test_second_hash(self): #this makes sure that the hashes from the resized tables of size 41 above match up with what index they are falling into in the above table
        ht = HashTable(41)
        self.assertEqual(ht.horner_hash("tad"), 29)
        self.assertEqual(ht.horner_hash('{'), 0)
        self.assertEqual(ht.horner_hash("P"), 39)
    
        self.assertEqual(ht.horner_hash("at"), 7)
        self.assertEqual(ht.horner_hash("dat"), 3)
        # self.assertEqual(ht.horner_hash("g"), 3)
        # self.assertEqual(ht.horner_hash('{'), 3)
    
        # self.assertEqual(ht.horner_hash('ad'), 0)
        self.assertEqual(ht.horner_hash("cat"), 26)
        self.assertEqual(ht.horner_hash("bat"), 8)
        self.assertEqual(ht.horner_hash("S"), 1)
        self.assertEqual(ht.horner_hash("P"), 39)
    
    # 
    def test_02a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        # self.assertEqual(ht.get_table(), [None, None, None, ('cat', [5]), None, None, None])
        self.assertEqual(ht.get_all_keys(),['cat'])
        self.assertEqual(ht.get_table_size(), 7)
    
        # ht.insert("cat", 6)
        # ht.insert("cat", 7)
    
        # self.assertEqual(ht.get_table(), [None, None, None, ('cat', [5, 6, 7]), None, None, None])
        self.assertEqual(ht.get_all_keys(), ['cat'])
    
    def test_02b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)
    
    def test_02c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)
    
    def test_02d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])
    # 
    def test_02e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)
    # 
    def test_02f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), [5])
    # 
    def test_02g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)
    # 
    # def test_03(self):
    #     ht = HashTable(7)
    #     ht.insert("cat", 5)
    #     ht.insert("cat", 17)
    #     self.assertEqual(ht.get_value("cat"), [5, 17])
    # 
    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)
    # 
        ht.insert("dog", 8)
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)
    # 
        ht.insert("mouse", 10)
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)
    
        ht.insert("elephant", 12) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        # print('table size', ht.table_size)
        # print('num items', ht.num_items)
        # print(ht.get_table())
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])
        
    def test_long_test(self):
        ht = HashTable(8)
        ht.insert('volleyball', 0)
        
        # print(ht.horner_hash('volleyball'))
        # print('index: ',ht.get_index('volleyball'))
        # print('load factor: ', ht.get_load_factor())
        # print('table size: ', ht.get_table_size())

        self.assertEqual(ht.get_all_keys(), ['volleyball'])
        self.assertEqual(ht.get_value('volleyball'), [0])
        self.assertEqual(ht.get_num_items(), 1)
        self.assertTrue(ht.in_table('volleyball'))
        
        self.assertEqual(ht.horner_hash('volleyball'), 4)
        self.assertEqual(ht.get_index('volleyball'), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 0.125)
        self.assertEqual(ht.get_table_size(), 8)
        
        # ----------------
        ht.insert('baseball', 1)
        
        # print(ht.horner_hash('baseball'))
        # print('index: ',ht.get_index('baseball'))
        # print('load factor: ', ht.get_load_factor())
        # print('table size: ', ht.get_table_size())

        self.assertEqual(ht.get_all_keys(), ['baseball', 'volleyball'])
        self.assertEqual(ht.get_value('baseball'), [1])
        self.assertEqual(ht.get_num_items(), 2)
        self.assertTrue(ht.in_table('baseball'))
        
        self.assertEqual(ht.horner_hash('baseball'), 0)
        self.assertEqual(ht.get_index('baseball'), 0)
        self.assertAlmostEqual(ht.get_load_factor(), 0.25)
        self.assertEqual(ht.get_table_size(), 8)
        
        # ------------
        
        ht.insert('soccer', 2)
        
        # print(ht.horner_hash('soccer'))
        # print('index: ',ht.get_index('soccer'))
        # print('load factor: ', ht.get_load_factor())
        # print('table size: ', ht.get_table_size())

        self.assertEqual(ht.get_all_keys(), ['baseball', 'soccer', 'volleyball'])
        self.assertEqual(ht.get_value('soccer'), [2])
        self.assertEqual(ht.get_num_items(), 3)
        self.assertTrue(ht.in_table('soccer'))
        
        self.assertEqual(ht.horner_hash('soccer'), 1)
        self.assertEqual(ht.get_index('soccer'), 1)
        self.assertAlmostEqual(ht.get_load_factor(), 0.375)
        self.assertEqual(ht.get_table_size(), 8)
        
        # ----------------
        
        ht.insert('football', 3)

        self.assertEqual(ht.get_all_keys(), ['baseball', 'soccer', 'volleyball', 'football'])
        self.assertEqual(ht.get_value('football'), [3])
        self.assertEqual(ht.get_num_items(), 4)
        self.assertTrue(ht.in_table('football'))
        
        self.assertEqual(ht.horner_hash('football'), 5)
        self.assertEqual(ht.get_index('football'), 5)
        self.assertAlmostEqual(ht.get_load_factor(), 0.5)
        self.assertEqual(ht.get_table_size(), 8)
        
        # -------------
        ht.insert('fooTbaLl', 3)

        self.assertEqual(ht.get_all_keys(), ['football', 'soccer', 'fooTbaLl', 'volleyball', 'baseball'])
        self.assertEqual(ht.get_value('football'), [3])
        self.assertEqual(ht.get_num_items(), 5)
        self.assertTrue(ht.in_table('fooTbaLl'))
        
        self.assertEqual(ht.horner_hash('fooTbaLl'),3)
        self.assertEqual(ht.get_index('fooTbaLl'), 3)
        self.assertAlmostEqual(ht.get_load_factor(), 0.29411764705882354)
        self.assertEqual(ht.get_table_size(), 17)
        
        # ---------
        
        ht.insert('football', 4)
        ht.insert('soccer', 5)
        ht.insert('volleyball', 6)
        ht.insert('baseball', 7)



        self.assertEqual(ht.get_all_keys(), ['football', 'soccer', 'fooTbaLl', 'volleyball', 'baseball'])
        self.assertEqual(ht.get_value('football'), [3,4])
        self.assertEqual(ht.get_value('soccer'), [2,5])
        self.assertEqual(ht.get_value('volleyball'), [0,6])
        self.assertEqual(ht.get_value('baseball'), [1,7])

        self.assertEqual(ht.get_num_items(), 5)
        self.assertAlmostEqual(ht.get_load_factor(), 0.29411764705882354)
        self.assertEqual(ht.get_table_size(), 17)
    
# ------
        ht.insert('ofootball', 4)

        self.assertEqual(ht.get_all_keys(), ['football', 'soccer', 'fooTbaLl', 'ofootball', 'volleyball', 'baseball'])
        self.assertEqual(ht.get_value('football'), [3,4])
        self.assertEqual(ht.get_num_items(), 6)
        self.assertTrue(ht.in_table('football'))

        self.assertEqual(ht.horner_hash('ofootball'), 5)
        self.assertEqual(ht.get_index('ofootball'), 5)
        self.assertAlmostEqual(ht.get_load_factor(), 0.35294117647058826)
        self.assertEqual(ht.get_table_size(), 17)
        
        # -------------------
        self.assertEqual(ht.get_index('football'), 0)
        self.assertEqual(ht.get_index('soccer'), 2)
        self.assertEqual(ht.get_index('volleyball'), 8)
        self.assertEqual(ht.get_index('baseball'), 10)
        self.assertEqual(ht.get_index('fooTbaLl'), 3)
        self.assertEqual(ht.get_index('ofootball'), 5)
        
        # ----------
        
        ht.insert('Mfootball', 9)
        
        # print(ht.horner_hash('baseball'))
        # print('index: ',ht.get_index('baseball'))
        # print('load factor: ', ht.get_load_factor())
        # print('table size: ', ht.get_table_size())

        self.assertEqual(ht.get_all_keys(), ['football', 'soccer', 'fooTbaLl', 'ofootball', 'Mfootball', 'volleyball', 'baseball'])
        self.assertEqual(ht.get_value('Mfootball'), [9])
        self.assertEqual(ht.get_num_items(), 7)
        self.assertTrue(ht.in_table('Mfootball'))
        
        self.assertEqual(ht.horner_hash('Mfootball'), 5)
        self.assertEqual(ht.get_index('Mfootball'), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 0.4117647058823529)
        self.assertEqual(ht.get_table_size(), 17)
        
        # -----------------
        print(ht.get_table())
        print(ht.horner_hash('Ufootball'))
        
        # --------
        
        ht.insert('Ufootball', 11)
        
        # print(ht.horner_hash('baseball'))
        # print('index: ',ht.get_index('baseball'))
        # print('load factor: ', ht.get_load_factor())
        # print('table size: ', ht.get_table_size())

        self.assertEqual(ht.get_all_keys(), ['football', 'soccer', 'fooTbaLl', 'ofootball', 'Mfootball', 'volleyball', 'baseball', 'Ufootball'])
        self.assertEqual(ht.get_value('Ufootball'), [11])
        self.assertEqual(ht.get_num_items(), 8)
        self.assertTrue(ht.in_table('Ufootball'))
        
        self.assertEqual(ht.horner_hash('Ufootball'), 2)
        self.assertEqual(ht.get_index('Ufootball'), 11)
        self.assertAlmostEqual(ht.get_load_factor(), 0.47058823529411764)
        self.assertEqual(ht.get_table_size(), 17)

            
if __name__ == '__main__':
   unittest.main()
