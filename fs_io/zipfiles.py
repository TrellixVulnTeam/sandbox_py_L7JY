# Zipfile Module
import zipfile

TMP = "../tmp/"

# Create
zip = zipfile.ZipFile(TMP + 'Archive.zip', 'w', zipfile.ZIP_LZMA)
zip.write(TMP + "purchased.txt", "purchased.txt")
zip.write(TMP + "wishlist.txt", "wishlist.txt")

# Closing the zip
zip.close()

# Open and List
zip = zipfile.ZipFile(TMP + 'Archive.zip', 'r')
print(zip.namelist())

# Metadata in the zip folder
for meta in zip.infolist():
    print(meta)

info = zip.getinfo("purchased.txt")
print(info)

# Access to files in zip folder
print(zip.read("wishlist.txt"))
with zip.open('wishlist.txt') as f:
    print(f.read())

# Extracting files
# zip.extract("purchased.txt")  # specific file
zip.extractall(TMP)  # output path

# Closing the zip
zip.close()

# auto-close
with zipfile.ZipFile(TMP + 'Archive2.zip', 'w', zipfile.ZIP_LZMA) as newzip:
    newzip.write(TMP + "purchased.txt")
    newzip.write(TMP + "wishlist.txt")
