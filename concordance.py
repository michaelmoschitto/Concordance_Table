from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        
        try:
            stop_file = open(filename)
            stop_str = stop_file.read()
            stop_file.close()
        except:
            raise FileNotFoundError('cannot read from an empty file')
            
        self.stop_table = HashTable(191)
        stop_list = stop_str.split('\n')
        for word in stop_list:
            self.stop_table.insert(word, 0)
        

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        
        try:
            conc_file = open(filename)
            # conc_file.close()
        except:
            raise FileNotFoundError('invalid conc file')
            
        self.concordance_table = HashTable(191)
        
        # print(self.stop_table.get_all_keys())
        line_number = 1
        
        for line in conc_file:
            inserted = []
            line = self.strip_line(line) 
            word_list = line.split()
            for word in word_list:
                self.concordance_table.insert(word, line_number)
            line_number += 1
            # print(line)
        conc_file.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        list = self.concordance_table.get_all_keys()
    
        sorted_list = sorted(list)
        # print(sorted_list)
        # print(self.concordance_table.get_index('laws'))
        # # print(len(self.concordance_table))
        # print(self.concordance_table.get_index_multiples('laws'))
        # print(self.concordance_table.get_table())
    #     # print(sorted_list)
        out_string = ''
    # 
        for word in sorted_list:
            out_string += word + ': ' +  self.to_string(self.concordance_table.get_value(word)) + '\n'
    
        # print(out_string[:-1])    
    # 
        out_file = open(filename, 'w+')
        out_file.write(out_string[:-1])
        # print(out_string[:-1])
        out_file.close()
    # # 
    # 
    def to_string(self, list):
        string = ''
        for word in list:
            string += str(word) + ' '
        return string[:-1]
    
    def strip_line(self, line):
        line = line.lower()
        line = line.replace('-', ' ')
        to_delete = string.punctuation + string.digits
        for chr in line:
            if chr in to_delete:
                line = line.replace(chr, '')
        new_line = []
        line = set(line.split())
        for word in line:
            if not self.stop_table.in_table(word):
                new_line.append(word)
        line = ' '.join(new_line)
        line = line.strip()
        return line
        
# 
        
        
