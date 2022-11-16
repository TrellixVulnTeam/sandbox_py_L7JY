import tarfile

DATA = "../data/"
TMP = "../tmp/"

TAR_ARCHIVE = TMP + "archive.tar"
GZTAR_ARCHIVE = TMP + "archive.tar.gz"


def create_tar_archive():
    with tarfile.open(TAR_ARCHIVE, 'w') as tar:
        tar.add(DATA + "sample.txt", "sample.txt")
        tar.add(DATA + "sample.html", "sample.html")


def append_to_tar_archive():
    # mode='a' can only be used for uncompressed tar archives
    with tarfile.open(TAR_ARCHIVE, 'a') as tar:
        tar.add(DATA + "loremipsum.txt", "loremipsum.txt")


def read_tar_archive():
    with tarfile.open(TAR_ARCHIVE, 'r') as tar:
        print(tar.getnames())
        file_info = tar.getmember('sample.txt')
        print(file_info)
        print(dir(file_info))
        for member in tar:
            print(member.name)


def read_a_file():
    with tarfile.open(TAR_ARCHIVE, 'r') as tar:
        with tar.extractfile('sample.txt') as file:  # bytes IO
            print(file.read())


def extract_a_file():
    with tarfile.open(TAR_ARCHIVE, 'r') as tar:
        tar.extract('sample.txt', TMP)


def extract_all():
    with tarfile.open(TAR_ARCHIVE, 'r') as tar:
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, TMP)


# Compressed tar archive

def create_gztar_archive():
    # gz, bz2, xz(lzma)
    with tarfile.open(GZTAR_ARCHIVE, 'w:gz') as tar:
        tar.add(DATA + "sample.txt", "sample.txt")
        tar.add(DATA + "sample.html", "sample.html")


def read_gztar_archive():
    with tarfile.open(GZTAR_ARCHIVE, 'r:gz') as tar:
        print(tar.getnames())
        file_info = tar.getmember('sample.txt')
        print(file_info)


if __name__ == "__main__":
    create_tar_archive()
    append_to_tar_archive()
    read_tar_archive()
    read_a_file()
    extract_a_file()
    extract_all()

    print()
    create_gztar_archive()
    read_gztar_archive()
