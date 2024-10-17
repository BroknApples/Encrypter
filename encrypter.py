import os
import sys

####################################################################################
# Encryption class which all encryption types inherit from
####################################################################################
class Encryption():
  def __init__(self):
    # Defaults
    self.name = None
    self._seperator = ' '
    self._dict = {}

  def encrypt(self, filename, encrypted_filename = None) -> bool:
    """
    ####Default encryption function. Some encryption types may have their own version of this function.####
    Encrypt a file from one language to another.

    Args:
        filename (str): Name of the file to be encrypted
        encrypted_filename (str, optional): Name of the encrypted file. Defaults to None.

    Returns:
        bool: True if operation succeeded, False if some error occurred
    """
    # Get content of unencrypted file
    with open(filename, 'r') as readfile:
      old_text = readfile.read()
      
    # Default filename prepends 'encryption-type_encrypted_' to the original file
    if (encrypted_filename is None):
      encrypted_filename = f'{self.name}_encrypted_{filename}'

    # Encrypt file
    with open(encrypted_filename, 'w') as writefile:
      for (char) in (old_text):
        # Character not in dictionary
        if (char not in self._dict):
          print(f"ERROR: '{char}' not in {self.name} dictionary.\n")
          writefile.close()
          os.remove(encrypted_filename)
          return -1
          
        # Write char to file
        match(char):
          case '\n', '\t':
            writefile.write(char)
          case _:
            writefile.write(self._dict[char])
          
    # Finished with no errors
    return True

  def decrypt(self, filename, decrypted_filename = None):
    """####Default decryption function. Some encryption types may have their own version of this function.####"""
    with open(filename, 'r') as readfile:
      old_text = readfile.read()
      
    # Default filename prepends 'MorseCode_encrypted_' to the original file
    if (decrypted_filename is None):
      decrypted_filename = f'{self.name}_decrypted_{filename}'
      
    # Decrypt file
    with open(decrypted_filename, 'w') as writefile:
      for (char) in (old_text):        
        # Write char to file
        for (key, value) in (self._dict.items()):
          if (char != value):
            continue
          
          writefile.write(key)
          break
          
    # Finished with no errors
    return True

####################################################################################
# ShiftSix shifts all letters right by 6 and adds 6 to each number
####################################################################################
class ShiftSixEncryption(Encryption):
  def __init__(self):
    super().__init__()
    self.name = 'ShiftSix'
    self._seperator = ' '
    self._dict = {
      'SHIFT': '--...-',
      '\n': '\n',
      '\t': '\t',
      ' ': ' ',
      'A': 'G',
      'B': 'H',
      'C': 'I',
      'D': 'J',
      'E': 'K',
      'F': 'L',
      'G': 'M',
      'H': 'N',
      'I': 'O',
      'J': 'P',
      'K': 'Q',
      'L': 'R',
      'M': 'S',
      'N': 'T',
      'O': 'U',
      'P': 'V',
      'Q': 'W',
      'R': 'X',
      'S': 'Y',
      'T': 'Z',
      'U': 'A',
      'V': 'B',
      'W': 'C',
      'X': 'D',
      'Y': 'E',
      'Z': 'F',
      'a': 'g',
      'b': 'h',
      'c': 'i',
      'd': 'j',
      'e': 'k',
      'f': 'l',
      'g': 'm',
      'h': 'n',
      'i': 'o',
      'j': 'p',
      'k': 'q',
      'l': 'r',
      'm': 's',
      'n': 't',
      'o': 'u',
      'p': 'v',
      'q': 'w',
      'r': 'x',
      's': 'y',
      't': 'z',
      'u': 'a',
      'v': 'b',
      'w': 'c',
      'x': 'd',
      'y': 'e',
      'z': 'f',
      '0': '6',
      '1': '7',
      '2': '8',
      '3': '9',
      '4': '0',
      '5': '1',
      '6': '2',
      '7': '3',
      '8': '4',
      '9': '5',
      '`': '`',
      '~': '~',
      '!': '!',
      '@': '@',
      '#': '#',
      '$': '$',
      '%': '%',
      '^': '^',
      '&': '&',
      '*': '*',
      '(': '(',
      ')': ')',
      '-': '-',
      '_': '_',
      '=': '=',
      '+': '+',
      '[': '[',
      '{': '{',
      ']': ']',
      '}': '}',
      '\\': '\\',
      '|': '|',
      ';': ';',
      ':': ':',
      '"': '"',
      "'": "'",
      ',': ',',
      '<': '<',
      '.': '.',
      '>': '>',
      '/': '/',
      '?': '?'
    }
    
####################################################################################
# MorseEncryption follows this format: https://makoa.org/jlubin/morsecode.htm
####################################################################################
class MorseEncryption(Encryption):
  def __init__(self):
    super().__init__()
    self.name = 'MorseCode'
    self._seperator = ' '
    self._dict = {
      'SHIFT': '--...-',
      '\n': '\n',
      '\t': '\t',
      ' ': '..--',
      'a': '.-',
      'b': '-...',
      'c': '-.-.',
      'd': '-..',
      'e': '.',
      'f': '..-.',
      'g': '--.',
      'h': '....',
      'i': '..',
      'j': '.---',
      'k': '-.-',
      'l': '.-..',
      'm': '--',
      'n': '-.',
      'o': '---',
      'p': '.--.',
      'q': '--.-',
      'r': '.-.',
      's': '...',
      't': '-',
      'u': '..-',
      'v': '...-',
      'w': '.--',
      'x': '-..-',
      'y': '-.--',
      'z': '--..',
      '1': '.----',
      '2': '..---',
      '3': '...--',
      '4': '....-',
      '5': '.....',
      '6': '-....',
      '7': '--...',
      '8': '---..',
      '9': '----.',
      '0': '-----',
      '`': '--.---',
      '~': '---.--',
      '!': '.-....',
      '@': '---..-',
      '#': '..---.',
      '$': '..----',
      '%': '...-.-',
      '^': '-...--',
      '&': '.---..',
      '*': '-..--',
      '(': '---...',
      ')': '...---',
      '-': '.---.',
      '_': '----.-',
      '=': '---.-',
      '+': '-...-',
      '[': '-..---',
      '{': '..--.',
      ']': '.--...',
      '}': '--..-',
      '\\': '----..',
      '|': '....-.',
      ';': '-....-',
      ':': '.----.',
      '"': '..-...',
      "'": '...--.',
      ',': '-.....',
      '<': '--..--',
      '.': '.-----',
      '>': '..--..',
      '/': '....--',
      '?': '-.----'
    }

  def encrypt(self, filename, encrypted_filename = None) -> bool:
    """
    ####MorseCode encryption function.####
    Encrypt a file from English to Morse Code.

    Args:
        filename (str): Name of the file to be encrypted
        encrypted_filename (str, optional): Name of the encrypted file. Defaults to None.

    Returns:
        bool: True if operation succeeded, False if some error occurred
    """
    # Get content of unencrypted file
    with open(filename, 'r') as readfile:
      old_text = readfile.read()
      
    # Default filename prepends 'MorseCode_encrypted_' to the original file
    if (encrypted_filename is None):
      encrypted_filename = f'MorseCode_encrypted_{filename}'

    # Encrypt file
    with open(encrypted_filename, 'w') as writefile:
      for (char) in (old_text):
        # Character not in dictionary
        if (char.lower() not in self._dict):
          print(f"ERROR: '{char}' not in {self.name} dictionary.\n")
          writefile.close()
          os.remove(encrypted_filename)
          return False
        
        # Handle Uppercase letters
        if (char.isupper()):
          writefile.write(self._dict['SHIFT'] + self._seperator)
          char = char.lower()
          
        # Write char to file
        match(char):
          case '\n' | '\t':
            writefile.write(char)
          case _:
            writefile.write(self._dict[char] + self._seperator)
          
    # Finished with no errors
    return True

  def decrypt(self, filename, decrypted_filename = None) -> bool:
    """
    ####Default encryption function.####
    Decrypt a file from written in some encryption back to english.

    Args:
        filename (str): Name of the file to be encrypted
        decrypted_filename (str, optional): Name of the decrypted file. Defaults to None.

    Returns:
        bool: True if operation succeeded, False if some error occurred
    """
    # Get content of encrypted file
    with open(filename, 'r') as readfile:
      old_text = readfile.read()
      
    # Default filename prepends 'MorseCode_encrypted_' to the original file
    if (decrypted_filename is None):
      decrypted_filename = f'MorseCode_decrypted_{filename}'
      
    # Decrypt file
    with open(decrypted_filename, 'w') as writefile:
      shift = False
      curr_str = ''
      for (char) in (old_text):        
        # Print tab char or newline char
        if (char == '\t' or char == '\n'):
          writefile.write(char)
          continue
        
        # Morse Code character has not ended
        if (char != self._seperator):
          curr_str += char
          continue
        
        # If current char is the shift character
        if (curr_str == self._dict['SHIFT']):
          shift = True
          curr_str = ''
          continue

        # Write char to file
        for (key, value) in (self._dict.items()):
          if (curr_str != value):
            continue
          
          if (shift == True):
            writefile.write(key.upper())
            shift = False
          else:
            writefile.write(key)
          curr_str = ''
          break
          
    # Finished with no errors
    return True

####################################################################################
# Program main code
####################################################################################
ENCRYPT = '-e'
DECRYPT = '-d'
QUIT = '-q'

encryption_methods = [MorseEncryption(), ShiftSixEncryption()]

print('Enter an argument in this format: (use_type) filename.txt -method new_filename.txt\n')
print('Flags:')
print('Encrypt: -e\nDecrypt: -d\nQuit Program: -q\n')
print('Encryption Methods:')
print('MorseCode: -mc\nShiftSix: -s6\n')
print('Ex1: -e your_file.txt -mc new_name.txt')
print('Ex2: -d your_file.txt -ss | default output file is ShiftSix_decrypted_your_file.txt')
print('Ex3: -q | Quit Program\n')

while(True):
  arguments = str(input('Enter an argument: '))
  
  if ((arguments.replace(' ', '') == QUIT) or (arguments[0:2] == QUIT)):
    sys.exit()
  
  arg_type = ''
  filename = ''
  method = ''
  new_filename = ''
  
  arg_type_flag = True
  filename_flag = True
  method_flag = True
  new_filename_flag = True
  
  # Parse user arg
  period_found = False
  for (i) in (arguments):
    if (arg_type_flag): # type
      if (i == ' '):
        arg_type_flag = False
        continue
      arg_type += i
      
    elif (filename_flag): # filename
      if (period_found and i == ' '):
        period_found = False
        filename_flag = False
        continue
      
      if (i == '.'):
        period_found = True
      filename += i
      
    elif (method_flag): # encryption method
      if (i == ' '):
          method_flag = False
          continue
      method += i
      
    elif (new_filename_flag): # new filename
      if (period_found and i == ' '):
        new_filename_flag = False
        continue
      
      if (i == '.'):
        period_found = True
      new_filename += i
      
  print(f'Args: {arg_type}, {filename}, {method}, {new_filename}')
  
  if (not os.path.exists(filename)): # file doesnt exist
    print(f"ERROR: File: '{filename}' does not exist.")
    continue
  elif (new_filename.replace(' ', '') == ''): # use default new filename
    new_filename = None
  elif (os.path.exists(new_filename)): # new filename is already a file
    retry = False
    temp = ''
    while (temp != '1' or temp != '0'):
      temp = str(input(f"ERROR: '{new_filename}' already exists, would you like to replace this file?(type 1 to replace, type 0 to re-enter arguments): "))
      if (temp == '1'):
        new_filename = input('Enter a new filename:')
        break
      elif (temp == '0'):
        retry = True
        break
    if (retry):
      continue
  
  if (arg_type == ENCRYPT):
    match (method):
      case '-mc':
        if (not encryption_methods[0].encrypt(filename, new_filename)):
          print(f"Could not encrypt '{filename}' using {encryption_methods[0].name}")
      case '-s6':
        if (not encryption_methods[1].encrypt(filename, new_filename)):
          print(f"Could not encrypt '{filename}' using {encryption_methods[1].name}")
      case _:
        print("Invalid encryption method.")
  elif (arg_type == DECRYPT):
    match (method):
      case '-mc': # morse code
        if (not encryption_methods[0].decrypt(filename, new_filename)):
          print(f"Could not decrypt '{filename}' using {encryption_methods[0].name}")
      case '-s6': # shift six
        if (not encryption_methods[1].decrypt(filename, new_filename)):
          print(f"Could not decrypt '{filename}' using {encryption_methods[1].name}")
      case _:
        print("Invalid decryption method.")