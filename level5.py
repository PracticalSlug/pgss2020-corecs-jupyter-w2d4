import hashlib

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
flag_enc = bytearray(b'\x02\x06\x00\x1d,74\x14\x13F\x1fW_\x18\x0bC\x1c\x08A\x16NC^\x0eFB\x05C\x19P_ZS\x13\x0c\x1e')



def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()



def level_5_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == bytearray(b"\x04-\xd9\x9e\xb0\xff\x86S\x81ND\\\xa0\t4'") ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_5_pw_check()

### NOTE: You can make a new cell or put code below here to work with it.
### NOTE: You can comment out the `level_3_pw_check()` line viz. insert "#" at
###         beginning of line.


