import logging, sys


#basic config for logging
#send output to stderr instead of stdout to differenciate logging output from normal code output
#if you do 2>/dev/null the errors will be omited and only program output will be displayed
logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(asctime)s %(name)s %(levelname)s: %(message)s')

log = logging.getLogger(__name__)

def dosum(a, b, count=1):
	log.info('Starting sum')
	if a == b == 0:
		log.warning('Will be just 0 for any count')
	res = (a + b) * count
	log.info('(%s + %s) * %s = %s' % (a, b, count, res))
	print(res)
 	
dosum(5,3)

#logging to a file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('please provide a filename as an argument')
        sys.exit(1)
    logging_file = sys.argv[1]
    logging.basicConfig(level=logging.INFO, filename=logging_file, format='%(asctime)s %(name)s %(levelname)s: %(message)s')

log = logging.getLogger(__name__)

def fibo(num):
    log.info(f'calcutating up to the {num}th fibonacci number')
    a, b = 0, 1
    for n in range(num):
        a, b = b, a+b
        print(b, '', end='')
    print(b)

if __name__ == '__main__':
    import datetime
    fibo(datetime.datetime.now().second)



