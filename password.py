# Password re-try
password = 'a123456'
i = 3
while i > 0:
	pwd = input('Please input the password: ')
	if pwd == password:
		print('Success to log in!')
		break
	else:
		i = i - 1
		print('Password does not matched! You have ', i, ' more chance(s) to try.')