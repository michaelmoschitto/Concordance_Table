import unittest
from hash_quad import *

class TestList(unittest.TestCase):
    
    def test_same(self):
        ht = HashTable(10)
        ht.insert('a', 0)
        ht.insert('a', 7)
        ht.insert('k', 2)
        # print(ht.horner_hash('k'))
        ht.insert('k', 3)
        ht.insert('u', 5)
        ht.insert('u', 5)
        ht.insert('e', 9)
        ht.insert('e', 10)
        ht.insert('o', 5)
        ht.insert('o', 5)
        
    # def test_On(self):
    # 
    # 
    #     print(ht.get_table())
    
    def test_cat(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash('cat'), 3)
        ht.insert('cat', 3)
        ht.insert('cat', 5)
        ht.insert('u', 5)
        ht.insert('e', 9)
        self.assertEqual(ht.get_num_items(), 3)
        ht.insert('f', 10)
        # ht.insert('o', 5)
        # ht.insert('o', 5)
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table(), [None, ('u', [5]), None, None, None, None, None, None, None, None, None, ('e', [9]), ('f', [10]), ('cat', [3, 5]), None])


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
        ht.insert('cat', 1)
        ht.insert('bat', 1)
        ht.insert('dat', 2)
        ht.insert('tad', 3)
        ht.insert('at', 4)
        ht.increase_table_size()
    
    def test_quad_prob_append(self):
        ht = HashTable(10)
        ht.insert('a', 1)
        self.assertEqual(ht.horner_hash('a'), 7)
        ht.insert('k', 1)
        self.assertEqual(ht.horner_hash('k'), 7)
        ht.insert('k', 2)
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
        # print(ht.get_table())
    
    
    def test_num_items(self):
        ht = HashTable(10)
        ht.insert('cat', 0)
        ht.insert('in', 0)
        ht.insert('the', 0)
        ht.insert('hat', 0)
        self.assertEqual(ht.get_num_items(), 4)
        ht.insert('cat', 0)
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
        self.assertEqual(ht.get_table(), [('P', [-1]), ('bat', [1]), ('cat', [0]), ('dat', [2]), ('tad', [3]), None, None, ('at', [4]), ('S', [7]), None, None, None, ('g', [5]), None, None, None, None, None, None, ('{', [6])])
        ht.increase_table_size() #doing this manually because the load size does not exceed .5 but want to check if it will rehash to what I think it will with the new tables table_size
        self.assertEqual(ht.get_table(), [('{', [6]), ('S', [7]), None, ('dat', [2]), None, None, None, ('at', [4]), ('bat', [1]), None, None, None, None, None, None, None, None, None, None, None, None, ('g', [5]), None, None, None, None, ('cat', [0]), None, None, ('tad', [3]), None, None, None, None, None, None, None, None, None, ('P', [-1]), None])
    
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
        self.assertEqual(ht.get_table(), [None, None, None, ('cat', [5]), None, None, None])
        self.assertEqual(ht.get_table_size(), 7)
    
        ht.insert("cat", 6)
        ht.insert("cat", 7)
    
        self.assertEqual(ht.get_table(), [None, None, None, ('cat', [5, 6, 7]), None, None, None])
    # # 
    def test_02b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)
    # 
    def test_02c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)
    # 
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
    def test_03(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        self.assertEqual(ht.get_value("cat"), [5, 17])
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

if __name__ == '__main__':
   unittest.main()
