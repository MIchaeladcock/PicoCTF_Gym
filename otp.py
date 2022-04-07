#!/usr/bin/python3 -u

'''
Description

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) 
'''
#nc mercury.picoctf.net 58913
#******************Welcome to our OTP implementation!******************

#This is the encrypted flag!
#51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57

##-------------SOLVE-----------------------------------------------------------##

#set encrypted flag var ef = 0x51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57

# send 50k 'a's
# python -c "print('a' * 49968); print('a' * 32)" | nc mercury.picoctf.net 58913
# encrypted key 03464b4f1a1c3a313d1951573d195102383d1907533d1905033d1904043d1904

# python3 -c "print('\x00'*(50000-32)+'\n'+'\x00'*32)" | nc mercury.picoctf.net 58913
# encrypted flag 5541103a246e415e036c4c5f0e3d415a513e4a560050644859536b4f57003d4c
# encrypted key 6227295e455c7838375c7866375c7862355c786430635c7838665c7863365c78

#set encrypted flag var ea = 0x03464b4f1a1c3a313d1951573d195102383d1907533d1905033d1904043d1904
#6227295e455c7838375c7866375c7862355c786430635c7838665c7863365c78

#set plantext 'a's var pt = 0x61616161616161616161616161616161616161616161616161616161616161

#'{:x}'.format(ef^ea^pa)
#'5235656362343233623362343334373263333563633266343130313163366432'

#key =  '{:x}'.format(ef^ea^pt)
#print(bytes.fromhex(key).decode('utf-8'))
#R5ecb423b3b43472c35cc2f41011c6d2



import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"


def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location


print("******************Welcome to our OTP implementation!******************")
print('a'*49968)
print('a'* 32)

c = startup(0)
while c >= 0:
	c = encrypt(c)


