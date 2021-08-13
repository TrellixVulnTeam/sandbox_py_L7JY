import tarfile

DATA = "../data/"
TMP = "../tmp/"

TAR_ARCHIVE = TMP + "archive.tar"
GZTAR_ARCHIVE = TMP + "archive.tar.gz"


def create_tar_archive():
    with tarfile.open(TAR_ARCHIVE, 'w') as tar:
        tar.add(DATA + "lines.txt", "lines.txt")
        tar.add(DATA + "loremipsum.txt", "loremipsum.txt")


def append_to_tar_archive():
    # mode='a' can only be used for uncompressed tar archives
    with tarfile.open(TAR_ARCHIVE, 'a') as tar:
        tar.add(DATA + "sample.txt", "sample.txt")


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
        tar.extractall(TMP)


# Compressed tar archive

def create_gztar_archive():
    # gz, bz2, xz(lzma)
    with tarfile.open(GZTAR_ARCHIVE, 'w:gz') as tar:
        tar.add(DATA + "lines.txt", "lines.txt")
        tar.add(DATA + "sample.txt", "sample.txt")


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
