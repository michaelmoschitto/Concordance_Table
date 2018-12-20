
class HashTableValue:
    
    def __init__(self, key, value): 
        self.key = key
        self.value_list = [value]
        
    def set_value(self, value):
        self.value_list.append(value) 
    
    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value_list

class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        
        hash = self.horner_hash(key)
        
        if self.hash_table[hash] is None: #this means that the key is not in the table 
            self.hash_table[hash] = HashTableValue(key, value)
            self.num_items += 1
            # print('is None', key,value)
            
        else:
            if self.hash_table[hash].get_key() == key: #case key value pairs and just ahve to append to the value list
                if value != self.hash_table[hash].get_value()[-1]:
                    # print('same key', key, value)
                    self.hash_table[hash].set_value(value)
                    
            elif self.hash_table[hash].get_key() != key: #collision case where have to use quadratic probing 
                collisions = 0
                collision_index = hash
                
                # print('collision index', collision_index)
                while self.hash_table[collision_index] is not None and self.hash_table[collision_index].get_key() != key:
                    collisions += 1
                    collision_index = self.rehash(hash, collisions)
                    # print('collision Index2', collision_index, self.table_size)
                if self.hash_table[collision_index] is None:
                    # print('quad None', key,value)
                    self.hash_table[collision_index] = HashTableValue(key, value)
                    self.num_items += 1
                else:
                    if value != self.hash_table[collision_index].get_value()[-1]:
                        # print('quad append', key, value)
                        self.hash_table[collision_index].set_value(value)
                        
                
        
        
        if self.get_load_factor() > .5:
            self.increase_table_size()
        
            
    def increase_table_size(self):
        old_hash_table = list(self.hash_table)
        self.table_size = 2 * self.table_size + 1
        self.hash_table = [None] * self.table_size
        self.num_items = 0
        for item in old_hash_table:
            if item is not None:
                for value in item.get_value():
                    self.insert(item.get_key(), value)
            
        
        
        

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.""" """𝑜𝑟𝑑(𝑠𝑡𝑟[𝑖]) ∗ 31𝑛−1−𝑖"""
        # key = key.lower()
        i = 0
        hash = 0 
        n = min(8, len(key))
        
        while(i <= n - 1):
            hash += ord(key[i]) * (31 ** (n - 1 - i)) #hash += ord((key.lower()[i])) * (31 ** (n - 1 - i))
            i += 1
        return hash % self.table_size
        
    def rehash(self, original_hash, collisions):
        return (original_hash + collisions ** 2) % self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        hash = self.horner_hash(key)
        index = hash
        collisions = 0
        while self.hash_table[index] != None:
            if self.hash_table[index].get_key() == key:
                return True
            else:
                collisions += 1
                index = self.rehash(hash, collisions)
                # if index == hash:
                #     return False
        return False

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        hash = self.horner_hash(key)
        index = hash
        stopped = False
        collisions = 0
        # 
        # if not self.in_table(key):
        #     return None
            
        while self.hash_table[index] != None:
            if self.hash_table[index].get_key() == key:
                return index
            else:
                collisions += 1
                index = self.rehash(hash, collisions)
        return None
                
        
        
    # def get_index_multiples(self, key):
    #     """ Returns the index of the hash table entry containing the provided key. 
    #     If there is not an entry with the provided key, returns None."""
    #     index = []
    #     for i in range(len(self.hash_table)):
    #         if self.hash_table[i] is not None and self.hash_table[i].get_key() == key:
    #             index.append(i)
    #     return index

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        key_list = []
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                key_list.append(self.hash_table[i].get_key())
        return key_list

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        if not self.in_table(key):
            return None
        return self.hash_table[self.get_index(key)].get_value()
        

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / len(self.hash_table)
        
    def get_table(self):
        table = []
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is None:
                table.append(None)
            else:
                table.append((self.hash_table[i].get_key(), self.hash_table[i].get_value()))
        return table

    
