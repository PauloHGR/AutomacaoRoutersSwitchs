from librouteros import connect
import ssl, sys


class Mikro:
	"""docstring for Mikro"""
	def __init__(self):
		super(Mikro, self).__init__()

	def talk(self, command):
		
		for dns in command:
			if dns['allow-remote-requests'] == True:
				print('Allow Remote Requests is enable')
			else:
				print('Allow Remote Requests is disable')


mikro = Mikro()
api = connect(username='pauloh', password='est@paulo', host='XXX.XX.XXX.XXX')
command = api(cmd='/ip/dns/print')
mikro.talk(command)
api.close()
