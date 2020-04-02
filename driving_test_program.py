country = input('What is your nation?')
country = str(country)
if country == 'US':
	age = input('How old are you?')
	age = int(age)
	if age >= 18:
		print('Yes u can drive if u have license!')
	else:
		print('sorry that u cant bcz u r 2 young:(')
elif country == 'CN':
	age = input('How old are you?')
	age = int(age)
	if age >= 20:
		print('Yes u can drive if u have license!')
	else:
		print('sorry that u cant bcz u r 2 young:(')
else:
	print('sorry we cant recogenised your nation or we dont have the knowlage about your country')
