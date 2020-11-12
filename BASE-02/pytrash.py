import argparse
from os import mkdir, getlogin, replace, listdir, path, getcwd, remove


# Creating needed folders and files
USER = getlogin()
PATH = f"/home/{USER}/.local/share/PyTrash"
FILE = PATH + "/.pytrashdata"
if not path.exists(PATH):
    mkdir(PATH)
    print(f"Created directory '{PATH}'")
DATA = open(FILE, "a")

# Parsing arguments
parser = argparse.ArgumentParser(prog="pytrash", description="console trash")

parser.add_argument("-r", action="extend",\
                    metavar="FILE", nargs="+", type=str,\
                    help="moving to trash listed files")

parser.add_argument("-d", action="store_true",\
                    help="show all deleted files")

parser.add_argument("-i", action="extend",\
                    metavar="FILE", nargs="+", type=str,\
                    help="get more info about listed deleted files")

parser.add_argument("-l", action="store_true",\
                    help="show all deleted files in current directory")

parser.add_argument("-t", metavar="TIME", type=int,\
                    help="undo all deletions during the last TIME minutes")

parser.add_argument("-u", action="extend",\
                    metavar="FILE", nargs="+", type=str,\
                    help="undo listed deleted files to their directory(to list files, use -d or -l)")

parser.add_argument("-c", action="store_true",\
                    help="clear trash(WARNING, THIS OPERATION WILL ERASE ALL FILES IN TRASH)")

parser.add_argument("-m", action="extend",\
                    metavar="FILE", nargs="+", type=str,\
                    help="recover listed files in current directory")

parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.1")

args = parser.parse_args()

if args.r:
    todel = []
    string= "', '"
    for i in args.r:
        if not path.exists(i):
            todel.append(i)

    if not len(todel):
        for i in args.r:
            replace(i, f"{PATH}/{i}")
            print(i, "MOVED")
            DATA.write(f"{path.abspath(i)}\n")
    else:
        print(f"Files: '{string.join(todel)}' aren't exist")

elif args.d:
    string = "\n"
    files = listdir(PATH)
    files.pop(files.index(".pytrashdata"))
    print(f"{string.join(files)}")

elif args.l:
    CURR_PATH = getcwd() + "/"
    with open(FILE, "r") as f:
        for i in f.readlines():
            if CURR_PATH in i:
                print(i[len(CURR_PATH):-1])

elif args.i:
    pass

elif args.u:
    torec = []
    string= "', '"
    for i in args.u:
        if not path.exists(PATH+"/"+i):
            torec.append(i)

    if not len(torec):
        DATA.close()
        DATA = open(FILE, "r")
        filelist = []
        for i in DATA.readlines():
            filelist.append(i)
        DATA.close()

        DATA = open(FILE, "w")
        for i, item in enumerate(filelist):
            for j in args.u:
                if j in item:
                    replace(PATH+"/"+j, item[:-1])
                    filelist.pop(i)
        for i in filelist:
            DATA.write(i+"\n")
        DATA.close()
        DATA = open(FILE, "a")
    else:
        print(f"Files: '{string.join(torec)}' aren't exist")

elif args.c:
    for i in listdir(PATH):
        i = PATH + "/" + i
        if path.isfile(i):
            remove(i)
        else:
            rmdir(i)

elif args.t:
    pass

DATA.close()
