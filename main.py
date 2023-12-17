import html, sys, urllib.parse, base64
from argparse import ArgumentParser


class Encoder:
	data = None
	args = None

	def __init__(self) -> None:
		#get input from stdin (if provided that way)
		if(sys.stdin != None):
			for line in sys.stdin:
				self.data = line
		else:
			sys.exit()


if __name__ == '__main__':
	instance = Encoder()
	parser = ArgumentParser(description='encodes given data into specified format')
	parser.add_argument('-m', '--mode', required=True)
	instance.args = parser.parse_args()

	if (instance.args.mode == 'url'):
		instance.data = urllib.parse.quote_plus(str(instance.data))
	elif (instance.args.mode == 'html'):
		instance.data = html.escape(instance.data)
	elif (instance.args.mode == 'base64'):
		instance.data = base64.urlsafe_b64encode(bytes(instance.data, 'utf-8'))
	else:
		print('None existing mode specified...\nPlease choose from [url, html, base64]')
		sys.exit()

	sys.stdout.write(str(instance.data))