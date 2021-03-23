# PGen
This is a tool for generating wordlists and combinations.
The GUI was made successful using the PyQt5 module in Python.

## Languages Used
<img src = "https://img.shields.io/badge/python%20-%236C0101.svg?style=for-the-badge&logo=python&logoColor=white" alt="python"/>

## Options available in the tool
### General Settings
- Leet Combinations: This option allows you to general combinations in leet. For ex: `leet` in _"Leet Speak"_ is `1337`, where `l = 1`, `e = 3`, and `t = 7`
- Generate a word list
- Make combinations for a custom word

### Prefix and Suffix settings
- Add a prefix/suffix to your combination(s)
- Combine the prefix and suffix combination(s)
- Use numbers as prefix/suffix to your combination(s)
- Edit the length of numbers to be used as prefix/suffix

### Settings for WordList
- Include numbers in the wordlist
- Use default alphabet string to generate the wordlist
- Minimum and Maximum combo lengths

## Working
#### After clicking on the "Generate Combinations" button, all the combinations made using the current selected options are stored in a text file called "combs.txt" in the same directory as the program.

- If you want to include leet combinations, check the `Leet Combinations` options.
- To add a prefix to your combinations, type in the prefix you want in your combinations in the `Add Prefix` text box.
- To add a suffix to your combinations, type in the suffic you want in your combinations in the `Add Suffix` text box.
- To add the combinations of prefix and suffix, check the `Add combinations of prefix and suffix` option.
- If you want to include numbers as a prefix, check the `Add numbers as your prefix`, you can then change the `Prefix Number Length` accordingly.
- If you want to include numbers as a suffix, check the "Add numbers as your suffix", you can then change the `Suffix Number Length` accordingly.

###### If you want to generate a WordList as well, check the `Generate a word list` option.
- If you want to include numbers in the word list, check the `Include Number` option.
- If you want to use the default list of letters to make the wordlist, check the `Use default list` option.
- Change the offsets of the combination lengths accordingly using the `Min. Combo Length` and `Max. Combo Length` options.
- If you want to use a custom character list instead of the default list, that is override the default list, enter the characters in the `Custom Characters` textbox.
- To extend the default alphabet list, rather than overriding the default list, enter the characters in `Extend the default alphabet list` textbox.


![image](https://user-images.githubusercontent.com/69053040/112120536-592f2b80-8be4-11eb-8534-c90524b41dba.png)
