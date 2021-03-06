import os, sys
import shutil, glob 

def moveFile(s, d):
    try:
       shutil.move(s, d)
    except os.error, e:
        print "ERROR: Moving file '%s' to '%s' (%s)" % (s, d, e)
        return

def copyFile(f, d):
    try:
        print "Copying file '%s' to '%s'" % (f, d)
        shutil.copy(f, d)
    except os.error, e:
        print "ERROR: Copying file '%s' to '%s' (%s)" % (f, d, e)
        return

def copyFiles(f, d):
    files = glob.glob(os.path.join(os.getenv("UE_PATH"), f))
    for fi in files:
        copyFile(fi, d)

def createDir(d):
    try:
        print "Creating directory '%s'" % d
        if not os.path.exists(d):
            os.makedirs(d)
    except os.error, e:
        print "ERROR: Creating directory '%s' (%s)" % (d, e)
        return

def createDirTree(d, a):
    createDir(d)

    if type(a).__name__ == "list":
        for pf in a:
            copyFiles(pf, d)
    elif type(a).__name__ == "dict":
        for pd in a:
            createDirTree(os.path.join(d, pd), a[pd])
#    elif type(a).__name__ == "string":

def deleteFile(f):
    if os.path.exists(f):
        try:
            os.remove(f)
        except os.error, e:
            print "ERROR: Deleting file '%s' (%s)" % (f, e)
            return

def deleteFiles(fs):
    for f in glob.glob(fs):
        deleteFile(f)

