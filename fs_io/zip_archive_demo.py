# zipfile Module
import zipfile

DATA = "../data/"
TMP = "../tmp/"

ZIP_ARCHIVE = TMP + "archive.zip"


def create_zip_archive():
    # Create
    arc_zip = zipfile.ZipFile(ZIP_ARCHIVE, 'w', zipfile.ZIP_LZMA)
    arc_zip.write(DATA + "sample.txt", "sample.txt")
    arc_zip.write(DATA + "sample.html", "sample.html")

    # Closing the zip
    arc_zip.close()


def append_to_archive():
    # append files to the archive with context manager
    with zipfile.ZipFile(ZIP_ARCHIVE, 'a', zipfile.ZIP_LZMA) as arc:
        arc.write(DATA + "sample.xml", "sample.xml")


def check_validity():
    # Check validity of the file
    print(zipfile.is_zipfile("Archive.zip"))


def read_zip_archive():
    # Open
    with zipfile.ZipFile(ZIP_ARCHIVE, 'r') as arc_zip:
        # List infos
        print(arc_zip.namelist())
        print(arc_zip.infolist())

        # Retrieve a file info
        info = arc_zip.getinfo("sample.html")
        print(info)

        # Access to files in zip folder
        print(arc_zip.read("sample.txt"))  # bytes


def extract_zip():
    with zipfile.ZipFile(ZIP_ARCHIVE, 'r') as arc_zip:
        # Extracting files
        arc_zip.extract("sample.txt", TMP)  # specific file
        arc_zip.extractall(TMP)  # output path


if __name__ == "__main__":
    create_zip_archive()
    append_to_archive()
    check_validity()
    read_zip_archive()
    extract_zip()
