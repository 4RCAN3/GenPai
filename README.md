<h1 align="center">GenPai</h1>
<p align="center"><i>GenPai is a powerful tool to generate a wordlist, and combinations through diverse customization</i></p>
<div align="center">
  <a href="https://github.com/4RCAN3/PG/stargazers"><img src="https://img.shields.io/github/stars/4RCAN3/PG" alt="Stars Badge"/></a>
<a href="https://github.com/4RCAN3/PG/network/members"><img src="https://img.shields.io/github/forks/4RCAN3/PG" alt="Forks Badge"/></a>
<a href="https://github.com/4RCAN3/PG/pulls"><img src="https://img.shields.io/github/issues-pr/4RCAN3/PG" alt="Pull Requests Badge"/></a>
<a href="https://github.com/4RCAN3/PG/issues"><img src="https://img.shields.io/github/issues/4RCAN3/PG" alt="Issues Badge"/></a>
<a href="https://github.com/4RCAN3/PG/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/4RCAN3/PG?color=2b9348"></a>
<a href="https://github.com/4RCAN3/PG/blob/master/LICENSE"><img src="https://img.shields.io/github/license/4RCAN3/PG?color=2b9348" alt="License Badge"/></a>
</div>
<br>


## What is GenPai
  - This tool is made for making generation of WordLists and password combinations fairly easy through a user-friendly GUI and diverse customization. 
  - GenPai offers a range of settings that can be applied to generate combinations based on certain information, or if you want to generate a WordList. 
  - GenPai stores all the combinations in a text file. You can create multiple text files to store the combinations by changing the settings. 


## Available Settings 

#### General Settings

- Including Leet Combinations: Leet (or "1337"), is a system of modified spellings used primarily on the Internet. It often uses character replacements in ways that play on the similarity of their glyphs via reflection or other resemblance. This setting can be applied to make leet combinations of a custom word.
- Including Word List: Including this setting will create a Word List based on the settings provided for it.
- Custom Word: Make combinations for a custom word, for example make leet combinations for the custom word, add combinations of prefixes to the custom word, etc. 

### Prefix and Suffix Settings

- Add prefix: Add a prefix to all the combinations being generated. This will not override the previous combinations but will create the same amount of combinations with a prefix. 
- Add suffix: Add a suffix to all the combinations being generated. This will not override the previous combinations but will create the same amount of combinations with a suffix. 
- Add combinations of prefix and suffix: Makes Leet Combinations of the prefix or suffix and add them as prefixes or suffixes. 
- Add Numbers as prefix: Adds numerical combinations as prefix. 
- Add Numbers as suffix: Adds numerical combinations as suffix.
- Max Combo length for prefix: Set a maximum limit for the length of numerical combinations as prefixes. For example, setting this to 4 will generate numerical combinations upto 9999
- Max Combo length for suffix: Set a maximum limit for the length of numerical combinations as suffixes. 
- Min Combo length for prefix: Set a minimum limit for the length of numerical combinations as prefixes. For example, setting this to 2 will generate numerical combinations from 10, 11, etc. 
- Min Combo length for suffix: Set a minimum limit for the length of numerical combinations as suffixes. 
- Use a wordlist as prefix: Generates a wordlist based on the WordList settings and adds them as prefixes. 
- Use a wordlist as suffix: Generates a wordlist based on the WordList settings and adds them as suffixes. 

### Settings for WordList

- Include Numbers: This will include combinations of numbers in the defualt character list that is used to generate the wordlist (The default character list is a-z)
- Use default Character list: This will include the default character list to generate the wordlist (a-z)
- Min. Combo length: This sets the minimum length for the combinations being generated for the word list. Example: setting this to 2, will contain combinations like aa, ab. 
- Max. Combo length: This sets the maximum length for the combinations being generated for the word list. Example: setting this to 4, will contain combinations like aaaa, abcd, aacd, etc.
- Custom Character List: Use this to override the default alphabet list and use a custom character list to generate the word list. 
- Extend the default list: Use this to extend the default alphabet list (a-z). This will add the charcaters to the default character list. 

### Store Combinations

- Use the default Text file: Choosing this options will store the combinations to the default text file (combs.txt)
- Use a custom text file: Adding a file name (without extension) to this will create a new text file with that name and store the combinations in that file


## Installation and setup

- Clone the repository into your local machine: `git clone https://github.com/4RCAN3/PG/`
- After cloning, open the command prompt in the respective directory and type `gen.bat`
- Run the GUI by typing `python ui.py`

## Languages used

<img src = "https://img.shields.io/badge/python%20-%236C0101.svg?style=for-the-badge&logo=python&logoColor=white" alt="python"/>

# Contribute

Contributions are always welcome! Please create a PR to add Github Profile.

## :pencil: License

This project is licensed under [MIT](https://opensource.org/licenses/MIT) license.

## :man_astronaut: Show your support
