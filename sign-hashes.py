import os
import gnupg


def sha256sum_finder():
    root = os.getcwd()
    for dirpath, subFolders, files in os.walk(root):
        for file in files:
            if (file == 'sha256sum.txt'):
                sha256sum = os.path.join(dirpath, file)
                yield sha256sum

gpg = gnupg.GPG()
for sha256sum_file in sha256sum_finder():
    asc_file= sha256sum_file + '.asc'
    print(sha256sum_file)
    stream = open(sha256sum_file, "rb")
    sign = gpg.sign_file(stream, keyid='8B57ACA9', output= asc_file, detach=True)
    stream.close()
    stream = open(asc_file,"rb")
    verified = gpg.verify_file(stream,sha256sum_file)
    stream.close()
    if not verified:
        raise ValueError('Sign file {} could not be verified!\n'.format(asc_file) )
    else: print('Sign file {} has been varified\n'.format(asc_file))