# program lets you compare contents of 2 files, tells you if they are identical or not

import hashlib

# function takes absolute path, reads file data in binary, hashes it with SHA1, returns the hex value of the hash 
def hashGen():
    path = input("--> Enter absolute path: ")
    with open(path,'rb') as file:
            content = file.read()
            hash = hashlib.sha1()
            hash.update(content)
            hexval = hash.hexdigest()
    return hexval

# get user input and load hex dumps into strings
print("-> File 1:")
hex1 = hashGen()
print("-> File 2:")
hex2 = hashGen()

# compare hex strings, tell user if they're different
if hex1 == hex2:
    print("Files are identical")
else:
    print("Files are different")