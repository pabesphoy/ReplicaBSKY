def get_credentials() -> dict:
	credentials = dict()
	with open('credentials.txt') as f:
		for line in f.readlines():
			try:
				key, value = line.split(": ")
			except ValueError:
				# raises error when email and password not supplied
				print('Add your email and password in credentials file')
				exit(0)
			credentials[key] = value.rstrip(" \n")
	return credentials
