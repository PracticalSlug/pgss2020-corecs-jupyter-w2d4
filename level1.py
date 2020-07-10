### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

# v-- this is the flag in encrypted form!
flag_enc = bytearray(b'\x13\x01\x17\x07,:/\x1a\x1eW\x18@E\x18\x06X\x12\x05P\x11YY^\x03]L^\r[YQ\t\x0cQ\x1c')



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "chthonian"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()