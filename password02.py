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
		print('Password does not match!')
		if i > 0:
			print('You have ', i, ' more chance(s) to try.')
		else:
			print('Fail to log in.  Your account is going to be locked')