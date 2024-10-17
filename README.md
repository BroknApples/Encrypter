Python script that can encrypt files in some specified encryption method

If you wish to create your own encryption method then create a class that inherits from the Encryption class
and at the end of the encrypter.py script, add your new class to the 'encryption_methods' list and add a case to the match statement. Create a custom encryption/decryption method if you so wish(very much needed when your encryption method adds more than one character in place of one; or if you do not feel like adding uppercase/lowercase letters or you only want to add chars and not symbols to a dictionary)

How To Use:
----------------
Put file in the same directory as the encrypter.py script file (you cannot type / in a filename)
Open folder in Terminal
Type 'python encrypter.py'
Follow instructions
... and voila! your file is now encrypted(or decrypted)!

Current Methods:
----------------
MorseCode
ShiftSix