import sys

if not sys.argv.__len__() > 1:
    print("py3cat 0.1 - cgriffith")
    print("pycat <file> [n]")
    print()
    print("file - file to search <req>")
    print("n - count line numbers [optional]")
else:
    arg1=sys.argv[1]
    if not sys.argv.__len__() > 2:
        num = False
    else:
        if sys.argv[2] is 'n':
            num = True
        else:
            num = False

    cnt = 0;
    with open(arg1, 'r') as inF:
        for line in inF:
            if num is True:
                cnt += 1
                string = str(cnt) + ": " + line
            else:
                string = line
            print(string)
