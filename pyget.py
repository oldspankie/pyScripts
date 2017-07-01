import sys
import urllib.request
#import datetime

if not sys.argv.__len__() > 1:
    print("py3get 0.2")
    print("pyget <url> [saveas]")
    print()
    print("url - required")
    print("saveas - optional")
else:
    arg1=sys.argv[1]
    if not sys.argv.__len__() > 2:
        arg2 = arg1.split('/')[-1]
    else:
        arg2=sys.argv[2]
    
    print("Getting file " + arg2)
    print("From " + arg1)

    urllib.request.urlretrieve(arg1, arg2)
