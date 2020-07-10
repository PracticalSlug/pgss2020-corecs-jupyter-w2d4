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
flag_enc = bytearray(b'\x13\x08\x0f\n07#\x15\x13Q\x13UA\x12\x1bR\x16\x05P\x1cNP]\x08GN\x03^\x16\x17NU\x08]K\x1e')



def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()



def level_4_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == bytearray(b'\xdc\xf0\xc2\x94\x1a\x1b|\xf6P\x19\xfd\xa3\xf1DKK') ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_4_pw_check()

### NOTE: You can make a new cell or put code below here to work with it.
### NOTE: You can comment out the `level_3_pw_check()` line viz. insert "#" at
###         beginning of line.

# The strings below are over 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["calelectric","calelectrical","calelectricity","calembour","calemes","calenda","calendal","calendar","calendared","calendarer","calendarial","calendarian","calendaric","calendaring","calendarist","calendars","calendas","calender","calendered","calenderer","calendering","calenders","calendric","calendrical","calendry","calends","calendula","calendulas","calendulin","calentural","calenture","calentured","calenturing","calenturish","calenturist","calepin","calesa","calesas","calescence","calescent","calesero","calesin","calf","calfbound","calfdozer","calfhood","calfish","calfkill","calfless","calflike","calfling","calfret","calfs","calfskin","calfskins","calgary","calgon","caliban","calibanism","caliber","calibered","calibers","calibogus","calibrate","calibrated","calibrater","calibrates","calibrating","calibration","calibrations","calibrator","calibrators","calibre","calibred","calibres","caliburn","caliburno","calic","calicate","calices","caliche","caliches","caliciform","calicle","calicles","calico","calicoback","calicoed","calicoes","calicos","calicular","caliculate","calybite","calycanth","calycanthaceae","calycanthaceous","calycanthemous","calycanthemy","calycanthin","calycanthine","calycanthus","calycate","calyceal","calyceraceae","calyceraceous","calyces","calyciferous","calycifloral","calyciflorate","calyciflorous","calyciform","calycinal","calycine","calycle","calycled","calycles","calycli","calycocarpum","calycoid","calycoideous","calycophora","calycophorae","calycophoran","calycozoa","calycozoan","calycozoic","calycozoon","calycular","calyculate"]