from os.path import isdir

def dir_path(string):
    if isdir(string):
        return string
    else:
        raise NotADirectoryError(string)
def bprint(*args):
    print("[CPM]: " + " ".join(str(x) for x in args))