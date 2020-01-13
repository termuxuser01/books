import argparse
import functools
import logging
import operator

#using sys.argv for parsing CI arguments

parser = argparse.ArgumentParser(
        description='Adds an operation to one or more nubers'
        )
parser.add_argument("number",
        help='One or more numbers to add an operation to.',
        #the + symbol tells that this option is requiered at least one or more times
        nargs='+', type=int)
parser.add_argument('-o', '--operation',
        help='The operation to perform on the numbers',
        choices=['add', 'sub', 'mul', 'div'], default='add')
parser.add_argument('-v', '--verbose', action='store_true',
        help='Increase output verbosity')

#parse arguments and send them to the opts variable
opt = parser.parse_args()
logging.basicConfig(level=logging.INFO if opt.verbose else logging.WARNING)
log = logging.getLogger()

options = getattr(operator, opt.operation)

log.info(f'Applying {opt.operation} to {opt.number}')
print(functools.reduce(operation, opt.number))
    
