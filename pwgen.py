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

    def __init__(self, text_file):
        self.file = text_file
    

    '''
    Leet Combinations
    Takes a string as an argument and returns a list of possible combination with leet substitution
    '''

    def LeetCombo(self, password, bool, final_combos):

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
            
            words = password.split(" ")
            for count, word in enumerate(words):
                for letters in product(*getPlaces(leet, word)):
                    words[count] = "".join(letters)
                    if len(final_combos) < 10**7:
                        final_combos.append(" ".join(i for i in words))
                    else:
                        self.WritePass(final_combos)
                        final_combos = []
                        final_combos.append(" ".join(i for i in words))
    
            return final_combos
        
        else:
            return final_combos



    '''
    Word Combination
    Genrates a word list using a string of characters
    Takes 3 arguments, Minimum combination length, Maximum combination length, and a character set
    Character set can be passed as a string of characters like "abcdefghijklmnopqrstuvwxyz"
    '''


    def WordCombos(self, min, max, chr_set, bool, final_combos):
        if bool == 2:
            chrs = chr_set
            min_length, max_length = min, max    
            for n in range(min_length, max_length+1):
                for xs in product(chrs, repeat=n):
                    if len(final_combos) < 10**7:
                        final_combos.append(''.join(xs))
                    else:
                        self.WritePass(final_combos)
                        final_combos = []
                        final_combos.append(''.join(xs))
            
            return final_combos
        else:
            return final_combos

    '''
    A function to add prefixes to the combinations
    Takes threee arguments:
    prefix -> The prefix to be added 
    combos -> A list of combinations to add prefixes
    to_comb -> A bool value to check if the prefix needs to have combinations
    '''
    
    def AddPrefix(self, prefix, combos, to_comb, bool):

        if bool == 2:
            
            if to_comb == 2:
                prefixes = self.LeetCombo(prefix[0], 2, [])
            else:
                prefixes = prefix
            
            after = []

            for combo in combos:
                for pre_combo in prefixes:
                    if (len(combos) + len(after) < 10**7):
                        word = pre_combo + combo
                        after.append(word)
                    else:
                        combos.extend(after)
                        self.WritePass(combos)
                        combos = []
                        after = []
                        after.append(word)

            combos.extend(after)
            
            return combos
        
        else:
            return combos


    
    '''
    A function to add Suffixes to the combinations
    Takes three arguments:
    suffix -> The suffix to be added 
    combos -> A list of combinations to add suffixes
    to_comb -> A bool value to check if the suffix needs to have combinations
    '''
    
    def AddSuffix(self, suffix, combos, to_comb, bool):

        if bool == 2:


            if to_comb == 2:
                suffixes = self.LeetCombo(suffix[0], 2, [])
            else:
                suffixes = suffix
            
            after = []
            
            for combo in combos:
                for suf_combo in suffixes:
                    if (len(combos) + len(after) < 10**7):
                        word = combo + suf_combo
                        after.append(word)
                    else:
                        combos.extend(after)
                        self.WritePass(combos)
                        combos = []
                        after = []
                        after.append(word)

            combos.extend(after)
            
            return combos
        
        else:
            return combos

    
    '''
    A function to add combinations of numbers as their prefix
    Takes three arguments:
    NumMinLength -> An integer value to set the minimum length of number combinations as prefix
    NumMaxLength -> An integer value to set the maximum length of number combinations as prefix
    combos -> A list of combinations to add the prefix to
    '''
    

    def AddNumPrefix(self, NumMinLength, NumMaxLength, combos, bool):

        if bool == 2:

            number_combos = self.WordCombos(NumMinLength, NumMaxLength, '0123456789', 2, [])


            after = []

            for combo in combos:
                for pre_combo in number_combos:
                    if (len(combos) + len(after) < 10**7):
                        word = str(pre_combo) + combo
                        after.append(word)
                    else:
                        combos.extend(word)
                        self.WritePass(combos)
                        combos = []
                        after = []
                        after.append(word)

            combos.extend(after)

            return combos

        else:
            return combos

    
    '''
    A function to add combinations of numbers as their suffix
    Takes three arguments:
    NumMinLength -> An integer value to set the minimum length of number combinations as suffix
    NumMaxLength -> An integer value to set the maximum length of number combinations as suffix
    combos -> A list of combinations to add the suffix to
    '''
    

    def AddNumSuffix(self, NumMinLength, NumMaxLength, combos, bool):

        if bool == 2:

            number_combos = self.WordCombos(NumMinLength, NumMaxLength, '0123456789', 2, [])
            
            after = []

            for combo in combos:
                for suf_combo in number_combos:
                    if (len(combos) + len(after) < 10**7):
                        word = combo + str(suf_combo)
                        after.append(word)
                    else:
                        combos.extend(after)
                        self.WritePass(combos)
                        combos = []
                        after = []
                        after.append(word)
            
            combos.extend(after)

            return combos
            
        else:
            return combos



    '''
    A function to write a list of combinations to a text file
    '''

    def WritePass(self, combos):
        with open(f"{self.file}.txt", 'w') as data:
            for word in combos:
                data.write(word + '\n')
            data.close()
