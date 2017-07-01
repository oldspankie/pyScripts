import sys

if not sys.argv.__len__() > 2:
    print("py3grep 0.3 - cgriffith")
    print("pygrep <file> <string> [n]")
    print()
    print("file - file to search <req>")
    print("string - string to search for <req>")
    print("n - count line numbers [optional]")
else:
    arg1=sys.argv[1]
    arg2=sys.argv[2]
    if not sys.argv.__len__() > 3:
        num = False
    else:
        if sys.argv[3] is 'n':
            num = True
        else:
            num = False

    cnt = 0
    with open(arg1, 'r') as inF:
        for line in inF:
            if num is True:
                cnt += 1
            if arg2 in line:
                if num is True:
                    string = str(cnt) + ": " + line
                else:
                    string = line
                print(string)
