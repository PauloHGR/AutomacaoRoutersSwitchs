from librouteros import connect
import ssl


class Mikro:
	"""docstring for Mikro"""
	def __init__(self):
		super(Mikro, self).__init__()

	def talk(self, command):
		for x in command:
			for i,j in x.items():
				if i == 'installed-version':
					print(i + ': ' + j)


mikro = Mikro()
api = connect(username='pauloh', password='est@paulo', host='XXX.XXX.XXX.XXX')
command = api(cmd='/system/package/update/print')
mikro.talk(command)
api.close()
