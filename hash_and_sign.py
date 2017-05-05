import os
import hashlib
import getpass
# https://pythonhosted.org/python-gnupg/
import gnupg

ignore_files = ["sha256sum.txt", "sha256sum.txt.asc"]


def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


def create_sha256_checkusms(rootfolder=os.getcwd()):
    sha256sum_list = []
    for dirpath, subFolders, files in os.walk(rootfolder):
        files = [f for f in files if not f[0] == '.' and f not in ignore_files]
        subFolders[:] = [d for d in subFolders if not d[0] == '.']
        # print(dirpath)
        if len(files) > 0:
            sha256sum = os.path.join(dirpath, 'sha256sum.txt')
            with open(sha256sum, "w") as sumfile:
                for file in files:
                    file_path = os.path.join(dirpath, file)
                    line = "{}  {}\n".format(sha256_checksum(file_path), file)
                    sumfile.write(line)
            print("{} written".format(sha256sum))
            sha256sum_list.append(sha256sum)
    return sha256sum_list


def sign_sha256sum_list(sha256sum_list,passph=""):
    gpg = gnupg.GPG()
    for sha256sum_file in sha256sum_list:
        asc_file = sha256sum_file + '.asc'
        stream = open(sha256sum_file, "rb")
        sign = gpg.sign_file(stream, keyid='8B57ACA9', output=asc_file, detach=True, passphrase=passph)
        stream.close()
        stream = open(asc_file, "rb")
        verified = gpg.verify_file(stream, sha256sum_file)
        stream.close()
        if not verified:
            raise ValueError('Sign file {} could not be verified!\n'.format(asc_file))
        else:
            print('Sign file {} has been verified\n'.format(asc_file))


if __name__ == "__main__":
    p = getpass.getpass(prompt="Type the GPG passphrase: ")
    sha256sum_list = create_sha256_checkusms()
    sign_sha256sum_list(sha256sum_list,p)

