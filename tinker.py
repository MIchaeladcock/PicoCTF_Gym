import hashlib

pos_pw_list = open('dictionary.txt','r')

#print(pos_pw_list)

correct_pw_hash = open('level5.hash.bin', 'rb').read()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

for i in pos_pw_list:
	#print(i.replace("\n",""))
	if hash_pw(i.replace("\n","")) == correct_pw_hash:
		print("The password is: ", i)
	#else:
		#print("Fuck", i)