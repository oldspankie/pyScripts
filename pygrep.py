import sys

if not sys.argv.__len__() > 2:
    print "pygrep <file> <string>"
    print "<file> - file to search"
    print "<string> - string to search for"
else:
    arg1=sys.argv[1]
    arg2=sys.argv[2]
    with open(arg1, 'r') as inF:
        for line in inF:
            if arg2 in line:
                print(line)
