class Encryption():
  def __init__(self):
    # Defaults
    self.name = "Unknown"
    self._dict = {}
    self._seperator = " "
  
  def encrypt(self, filename, encrypted_filename = "NULL"):
    old_file = open(filename, "r")
    old_text = old_file.read()
    
    # Custom filenames
    if (encrypted_filename == "NULL"):
      new_file = open("encrypted_" + filename, "w")
    else:
      new_file = open(encrypted_filename, "w")
    
    # Loop through file and convert to the encryption method
    for (char) in (old_text):
      new_line = False
      # Handle Uppercase letters
      if (char.isupper()):
        new_file.write(self._dict["SHIFT"] + self._seperator)
        char = char.lower()
      # Do NOT add a space after newline char
      elif (char == "\n"):
        new_line = True
        
      if (char in self._dict):
        new_str = self._dict[char]
      else: # Character not in dictionary
        print("ERROR: Character not in dictionary: " + char + ".\n")
        return -1
      
      # Write char to file
      new_file.write(new_str)
      if (not new_line):
        new_file.write(self._seperator)

  def decrypt(self, filename, decrypted_filename = "NULL"):
    old_file = open(filename, "r")
    old_text = old_file.read()
    
    # Custom filnames
    if (decrypted_filename == "NULL"):
      new_file = open("encrypted_" + filename, "w")
    else:
      new_file = open(decrypted_filename, "w")
    
    
    # Loop through file and convert to the encryption method
    ######
    # get key by self.dict.items()["value_here"]
    ######
    curr_char = ""
    for (char) in (old_text):
      # If current char is the seperator char and 
      if (char == self.seperator and char != self.dict["SHIFT"]):
        new_file.write(curr_char)
      new_line = False
      # Handle Uppercase letters
      if (char.isupper()):
        new_file.write(self._dict["SHIFT"] + self._seperator)
        char = char.lower()
      # Do NOT add a space after newline char
      elif (char == "\n"):
        new_line = True
        
      if (char in self._dict):
        new_str = self._dict[char]
      else: # Character not in dictionary
        print("ERROR: Character not in dictionary: " + char + ".\n")
        return -1
      
      # Write char to file
      new_file.write(new_str)
      if (not new_line):
        new_file.write(self._seperator)
        
####################################################################################
# MorseEncryption follows this format: https://makoa.org/jlubin/morsecode.htm
####################################################################################
class MorseEncryption(Encryption):
  def __init__(self):
    super().__init__()
    self.name = "Morse_Code"
    self._dict = {
      "SHIFT": "--...-",
      "\n": "\n",
      "\t": "\t",
      " ": "..--",
      "a": ".-",
      "b": "-...",
      "c": "-.-.",
      "d": "-..",
      "e": ".",
      "f": "..-.",
      "g": "--.",
      "h": "....",
      "i": "..",
      "j": ".---",
      "k": "-.-",
      "l": ".-..",
      "m": "--",
      "n": "-.",
      "o": "---",
      "p": ".--.",
      "q": "--.-",
      "r": ".-.",
      "s": "...",
      "t": "-",
      "u": "..-",
      "v": "...-",
      "w": ".--",
      "x": "-..-",
      "y": "-.--",
      "z": "--..",
      "1": ".----",
      "2": "..---",
      "3": "...--",
      "4": "....-",
      "5": ".....",
      "6": "-....",
      "7": "--...",
      "8": "---..",
      "9": "----.",
      "0": "-----",
      "`": "--.---",
      "~": "---.--",
      "!": ".-....",
      "@": "---..-",
      "#": "..---.",
      "$": "..----",
      "%": "...-.-",
      "^": "-...--",
      "&": ".---..",
      "*": "-..--",
      "(": "---...",
      ")": "...---",
      "-": ".---.",
      "_": "----.-",
      "=": "---.-",
      "+": "-...-",
      "[": "-..---",
      "{": "..--.",
      "]": ".--...",
      "}": "--..-",
      "\\": "----..",
      "|": "....-.",
      ";": "-....-",
      ":": ".----.",
      "'": "..-...",
      '"': "...--.",
      ",": "-.....",
      ",": "--..--",
      ".": ".-----",
      ">": "..--..",
      "/": "....--",
      "?": "-.----"
    }
    
morse_encrypt = MorseEncryption()
morse_encrypt.encrypt("filename.txt")
print(morse_encrypt.name)