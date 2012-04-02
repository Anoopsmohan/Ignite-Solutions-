import sys,re
def main():
        str1=raw_input("Enter the string: ")
	#re.sub() used to find each word and reverse it
	print re.sub(r'[-\w]+', lambda w:w.group()[::-1],str1)

if __name__=='__main__':
	main()      
