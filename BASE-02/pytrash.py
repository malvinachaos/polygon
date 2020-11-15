import argparse
from os import mkdir, getlogin, replace, listdir, path, getcwd, remove, system


# Creating needed folders and files
USER = getlogin()
PATH = f"/home/{USER}/.local/share/PyTrash"
FILE = PATH + "/.pytrashdata"

if not path.exists(PATH):
    mkdir(PATH)
    print(f"Created directory '{PATH}'")
if not path.exists(FILE):
    system(f"touch {FILE}")
    print(f"Created data file")

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

parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.2")

args = parser.parse_args()

def files_exist(files, Path=""):
    non = []
    for i in files:
        if not path.exists(Path+i):
            non.append(i)
            print("GOTCHA!")
    return non

def load():
    READ = []
    with open(FILE, "r") as DATA:
        for i in DATA.readlines():
            READ.append(i)
    return READ

def upload(READ):
    with open(FILE, "w") as DATA:
        for i in READ:
            DATA.write(i+"\n")

if args.r:
    string= "', '"
    f = files_exist(args.r)

    if not len(f):
        file_list = load()
        for i in args.r:
            replace(i, f"{PATH}/{i}")
            print(i, "MOVED")
            file_list.append(f"{path.abspath(i)}\n")
        upload(file_list)
    else:
        print(f"Files: '{string.join(f)}' aren't exist")

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
    string= "', '"
    f = files_exist(args.i, PATH + "/")
    data = load()

    if not len(f):
        for item in args.i:
            one = 0
            for i in data:
                if i.find(item) != -1:
                    one = i[:-1]
            print(f'''
Info about '{item}':
    Path: {one}
    Size: {path.getsize(PATH+"/"+item)} Bytes
    Date: {path.getctime(PATH+"/"+item)}
''')
    else:
        print(f"Files: '{string.join(f)}' don't exist")

elif args.u:
    string= "', '"
    f = files_exist(args.u, PATH + "/")

    if not len(f):
        file_list = load()

        for i, item in enumerate(file_list):
            for j in args.u:
                if j in item:
                    replace(PATH+"/"+j, item[:-1])
                    print(j, "RESTORED")
                    file_list.pop(i)
        upload(file_list)
    else:
        print(f"Files: '{string.join(f)}' aren't exist")

elif args.c:
    for i in listdir(PATH):
        i = PATH + "/" + i
        if path.isfile(i):
            remove(i)
        else:
            rmdir(i)

elif args.m:
    pass

