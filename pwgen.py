from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout
from itertools import product
import sys



class Settings():

    #make a global variable to store the final combinations

    '''
    LeetCombo - Func to create leet combinations
    WordCombos - Func to Generate a word list
    AddPrefix - Func to add prefixes to the combinations
    AddSuffix - Func to add suffixes to the combinations
    AddNumPrefix -Func to add numbers as prefixes
    AddNumSuffix - Func to add numbers as suffixes
    WritePass - Func to write all the combinations to a text file
    '''

    def __init__(self):
        pass
    

    '''
    Leet Combinations
    Takes a string as an argument and returns a list of possible combination with leet substitution
    '''

    def LeetCombo(self, password, bool):

        if bool == 2:

            leet = {'a': "A4a@",'b': "Bb8",'c': "Cc",'d': "Dd",'e': "Ee3",'f': "Ff",
            'g': "Gg6",'h': "Hh",'i': "Ii",'j': "Jj",'k': "Kk",
            'l': "Ll",'m': "Mm",'n': "Nn",'o': "Oo0",'p': "Pp",'q': "Qq",
            'r': "Rr",'s': "Ss5",'t': "Tt+",'u': "Uu",'v': "Vv",
            'w': "Ww",'x': "Xx",'y': "Yy",'z': "Zz2", '1': '1', '2': '2', '3': '3eE',
            '4': '4aA', '5': '5sS', '6': '6gG', '7': '7', '8': '8bB', '9': '9', '0': '0oO'}
            
            def getPlaces(leet, word):
                wordList = []
                for el in word:
                    if el.lower() in leet:
                        wordList.append(leet[el.lower()])
                    else:
                        wordList.append(el)
                
                return wordList

            #getPlaces = lambda word: [leet[el.lower()] for el in word]
            
            all_combs = []
            words = password.split(" ")
            for count, word in enumerate(words):
                for letters in product(*getPlaces(leet, word)):
                    words[count] = "".join(letters)
                    all_combs.append(" ".join(i for i in words))
            
            return all_combs
        
        else:
            return []



    '''
    Word Combination
    Genrates a word list using a string of characters
    Takes 3 arguments, Minimum combination length, Maximum combination length, and a character set
    Character set can be passed as a string of characters like "abcdefghijklmnopqrstuvwxyz"
    '''


    def WordCombos(self, min, max, chr_set, bool):
        if bool == 2:
            combos = []
            chrs = chr_set
            min_length, max_length = min, max    
            for n in range(min_length, max_length+1):
                for xs in product(chrs, repeat=n):
                    combos.append(''.join(xs))
            
            return combos
        else:
            return []

    '''
    A function to add prefixes to the combinations
    Takes threee arguments:
    prefix -> The prefix to be added 
    combos -> A list of combinations to add prefixes
    to_comb -> A bool value to check if the prefix needs to have combinations
    '''
    
    def AddPrefix(self, prefix, combos, to_comb, bool):

        if bool == 2:

            after_prefix_combo = []

            if to_comb == 2:
                prefixes = self.LeetCombo(prefix, 2)
            else:
                prefixes = [prefix]
            
            for combo in combos:
                for pre_combo in prefixes:
                    word = pre_combo + combo
                    after_prefix_combo.append(word)

            
            return after_prefix_combo
        
        else:
            return []


    
    '''
    A function to add Suffixes to the combinations
    Takes three arguments:
    suffix -> The suffix to be added 
    combos -> A list of combinations to add suffixes
    to_comb -> A bool value to check if the suffix needs to have combinations
    '''
    
    def AddSuffix(self, suffix, combos, to_comb, bool):

        if bool == 2:

            after_suffix_combo = []

            if to_comb == 2:
                suffixes = self.LeetCombo(suffix)
            else:
                suffixes = [suffix]
            
            for combo in combos:
                for suf_combo in suffixes:
                    word = combo + suf_combo
                    after_suffix_combo.append(word)

            
            return after_suffix_combo
        
        else:
            return []

    
    '''
    A function to add combinations of numbers as their prefix
    Takes three arguments:
    NumMinLength -> An integer value to set the minimum length of number combinations as prefix
    NumMaxLength -> An integer value to set the maximum length of number combinations as prefix
    combos -> A list of combinations to add the prefix to
    '''
    

    def AddNumPrefix(self, NumMinLength, NumMaxLength, combos, bool):

        if bool == 2:
            after_prefix_combo = []

            number_combos = self.WordCombos(NumMinLength, NumMaxLength, '0123456789', 2)

            for combo in combos:
                for pre_combo in number_combos:
                    word = str(pre_combo) + combo
                    after_prefix_combo.append(word)

            return after_prefix_combo

        else:
            return []

    
    '''
    A function to add combinations of numbers as their suffix
    Takes three arguments:
    NumMinLength -> An integer value to set the minimum length of number combinations as suffix
    NumMaxLength -> An integer value to set the maximum length of number combinations as suffix
    combos -> A list of combinations to add the suffix to
    '''
    

    def AddNumSuffix(self, NumMinLength, NumMaxLength, combos, bool):

        if bool == 2:
            after_suffix_combo = []

            number_combos = self.WordCombos(NumMinLength, NumMaxLength, '0123456789', 2)

            for combo in combos:
                for suf_combo in number_combos:
                    word = combo + str(suf_combo)
                    after_suffix_combo.append(word)

            return after_suffix_combo
            
        else:
            return []



    '''
    A function to write a list of combinations to a text file
    '''

    def WritePass(self, combos):
        with open("combs.txt", 'w') as data:
            for word in combos:
                data.write(word + '\n')
            data.close()

