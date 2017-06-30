import sys
import urllib
#import datetime

if not sys.argv.__len__() > 1:
    print "pyget <url> [saveas]"
    print "url - required"
    print "saveas - optional"
else:
    arg1=sys.argv[1]
    if not sys.argv.__len__() > 2:
        arg2 = arg1.split('/')[-1]
    else:
        arg2=sys.argv[2]
    
    print "Getting file " + arg2
    print "From " + arg1

    urllib.urlretrieve(arg1, arg2)
