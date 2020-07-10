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
flag_enc = bytearray(b"\x15\x07\x08\x06\'!#\x15\x1b]\x14AH\x19\x03X\x17\x1eV\x17FXU\x18QC\x1f\x1eTXQ\rZQ\x19")



def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == bytearray(b'\x65\x6e\x6b\x69\x64\x75').decode()):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_2_pw_check()