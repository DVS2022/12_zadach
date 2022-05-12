import json
# data_userpass = {'user1': "password1"}
# with open('10.json', 'w') as f:
# 	json.dump(data_userpass, f)

def login_function(login, password):
	with open('10.json', 'r') as f:
		data_userpass = json.load(f)
	if login in data_userpass.keys():
		if data_userpass[login] == password:
			print('Успешный вход!')
		else:
			print('Неверный пароль!')
	else:
		 print('Неверный логин!')		

def reg_function(login, password):
	with open('10.json', 'r') as f:
		data_userpass = json.load(f)
	if login not in data_userpass.keys():
		data_userpass[login] = password
		with open('10.json', 'w') as f:
			json.dump(data_userpass, f)
			print('Успешная регистрация!')
	else:
		print('Такой логин уже есть')


while True:
	break_point = input('Выйти из программы? ')
	if break_point == 'да':
		break
	chose_what = input('регистрация или вход? ')
	if chose_what == 'вход':
		login_function(input('Введите логин: '), input('Введите пароль: '))
	elif chose_what == 'регистрация':
		reg_function(input('Введите логин: '), input('Введите пароль: '))
	