#!/usr/bin/python
import crypt,sys

if len(sys.argv) != 2:
	print('Modo de uso: ./'+sys.argv[0]+' wordlist')
else:
	print('#############################################')
	print("# Password Salt Resolver for Linux v1.20   .#")
	print("# Dev. Luiz G F Michelmann                 .#")
	print("# Site: https://www.francosinformatica.com .#")
	print('#############################################\n')

	#senha completa
	senhaC = raw_input('Digite o hash completo: ')
	
	#salt
	salt_puro = senhaC.split('$')
        salt = "$"+salt_puro[1]+"$"+salt_puro[2]+"$"
	

	wordlist = open(sys.argv[1], 'r')

	for passwd in wordlist:
		passwd = passwd.rstrip('\n')
		print('Testando...')
		cod = crypt.crypt(passwd,salt)
		if(senhaC == cod):
			print('[+] Senha encontrada: '+passwd)
			exit()

	wordlist.close()
