from librouteros import connect
import ssl, sys


class Mikro:
	"""docstring for Mikro"""
	def __init__(self):
		super(Mikro, self).__init__()

	def talk(self, command):
		control=0
		for x in command:

			if x['name'] == sys.argv[1]:
				
				control +=1
				if x['disabled'] == True:
					print('disabled')
				else:
					print('enabled')

		if control == 0:
			print('service no existe')


mikro = Mikro()
api = connect(username='pauloh', password='est@paulo', host='177.66.116.134')
command = api(cmd='/ip/service/print')
mikro.talk(command)
api.close()