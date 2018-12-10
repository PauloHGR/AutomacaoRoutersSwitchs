import pexpect

_USERNAME = 'cisco'
_PASSWORD = 'cisco'

class Cisco():
	"""docstring for Cisco"""
	def __init__(self):
		super(Cisco, self).__init__()

	def login(self):
		child = pexpect.spawn('ssh 10.0.10.1')
		child.expect('login as:')
		child.sendline(_USERNAME)
		child.expect('Password:')
		child.sendline(_PASSWORD)
		return child

	def cisco_enable(self, child):
		child.expect('Router>')
		child.sendline('enable')
		child.expect('Router#')
		

def main():
	
	child = login()
	cisco_enable()
	#command
	child.sendline('show ip route')
	print (child.before)

if __name__ == '__main__':
    main()