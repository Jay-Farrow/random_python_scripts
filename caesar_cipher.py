# Task: Write a program that simulates caesar's cipher. 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#text = input("Type your message:\n").lower()
#shift = int(input("Type the shift number:\n"))

# First we need to encrypt the entered message. To do so we'll create a function called 'encrypt'.
def encrypt(plain_text, shift_amount):
    temp_list = []
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    
    for letter in plain_text:
        temp_list += letter
    
    new_temp_list = []
    for item in temp_list:
        temp_index = alphabet.index(item)
        index_shift = temp_index + shift_amount
        if index_shift > 25:
            index_shift -= 26
        new_temp_list += alphabet[index_shift]
    
    encoded_text = ''.join(new_temp_list)
    print(f"The encoded text is {encoded_text}")

# Then we need to decrypt the encrypted message. To do so we'll create a function called 'decrypt'.    
def decrypt(encrypted_text, shift_amount):
    temp_list = []
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    
    for letter in encrypted_text:
        temp_list += letter
    
    new_temp_list = []
    for item in temp_list:
        temp_index = alphabet.index(item) 
        index_shift = temp_index - shift_amount
        if index_shift < 0:
            index_shift += 26
        new_temp_list += alphabet[index_shift]
    
    decoded_text = ''.join(new_temp_list)
    print(f"The decoded text is {decoded_text}")

# Now that both functions encrypt and decrypt work correctly. We can clean up or reduce our code by creating one single function called caesar.
def caesar(direction, text, shift):
    if direction == 'encode':
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == 'decode':
        decrypt(encrypted_text=text, shift_amount=shift)


# main code
while True:
    restart_loop = False
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(direction=direction, text=text, shift=shift)
    user_input = input("Do you want to encrypt or decrypt again? (yes/no):\n").lower()
    if user_input == 'yes':
        restart_loop = True
    elif user_input == 'no':
        break
    else:
        print("Invalid input.")
        restart_loop = True
    
    if restart_loop:
        continue

# The first way of implementing this code. The above is the improved way for readability. 
''' 
 if direction == 'encode':
        encrypt(plain_text=text, shift_amount=shift)
        user_input = input("Do you want to encrypt or decrypt again? (yes/no): ").lower()
        if user_input == 'yes':
            restart_loop = True
        elif user_input == 'no':
            break
        else:
            print("Invalid Input.")
            restart_loop = True
    elif direction == 'decode':
        decrypt(encrypted_text=text, shift_amount=shift)
        user_input = input("Do you want to encrypt or decrypt again? (yes/no): ").lower()
        if user_input == 'yes':
            restart_loop = True
        elif user_input == 'no':
            break
        else:
            print("Invalid Input.")
            restart_loop = True
    else:
        print("Invalid Input.")
        restart_loop = True
    
    if restart_loop:
        continue
'''