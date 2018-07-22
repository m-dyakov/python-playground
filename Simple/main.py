import sys
import methods

if len(sys.argv) == 1:
    print('No arguments provided')
    sys.exit(0)

x = sys.argv[1]
if methods.isInt(x):
    print('Value {0} is a number'.format(x))
else:
    print('Value {0} is not a number'.format(x))