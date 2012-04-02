import os,re,sys

def fun(arg, dirname, fnmes):
	out_list = []
	for fname in fnmes:
		filepath = os.path.join(dirname,fname)
		if os.path.isfile(filepath):
			fp = open(filepath ,'r')
			text = fp.read()
			fp.close()
			if re.search(arg,text):
				# print full path. Calling os.path.basename will
				# give us just the name.
				print filepath



def main():
	strg=sys.argv[1]
	os.path.walk('.', fun, strg)


if __name__=='__main__':
	main()

