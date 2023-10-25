#!/usr/bin/env python
# coding: utf-8

# In[75]:


def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            key_char = key[key_index % key_length]
            shift = ord(key_char) - ord('a')
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            key_index += 1
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            key_char = key[key_index % key_length]
            shift = ord(key_char) - ord('a')
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            key_index += 1
        else:
            decrypted_char = char
        decrypted_text += decrypted_char

    return decrypted_text

# Teks yang akan dienkripsi
plain_text = "Success is not final, failure is not fatal, it is the courage to continue that counts"

# Kunci
key = "catur"

# Enkripsi teks
encrypted_text = vigenere_encrypt(plain_text, key)
print("Teks yang dienkripsi:", encrypted_text)

# Dekripsi teks
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Teks yang didekripsi:", decrypted_text)

# Fungsi untuk mengenkripsi dengan Affine Cipher
def affine_encrypt(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a')) * a + b) % 26 + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A')) * a + b) % 26 + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text


# Kunci Affine Cipher pertama
a1 = 4
b1 = 0


# Enkripsi teks Vigenere ke Affine dengan kunci pertama
affine_encrypted_text1 = affine_encrypt(vigenere_encrypted_text, a1, b1)
print("Teks yang dienkripsi dengan Affine Cipher (Kunci 1):", affine_encrypted_text1)


# In[ ]:





# In[ ]:




