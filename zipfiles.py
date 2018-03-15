# Zipfile Module
import zipfile

tmp_path = "./tmp/"

# Create
zip = zipfile.ZipFile(tmp_path + 'Archive.zip', 'w', zipfile.ZIP_LZMA)
zip.write(tmp_path + "purchased.txt", "purchased.txt")
zip.write(tmp_path + "wishlist.txt", "wishlist.txt")

# Closing the zip
zip.close()

# Open and List
zip = zipfile.ZipFile(tmp_path + 'Archive.zip', 'r')
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
zip.extractall(tmp_path)  # output path

# Closing the zip
zip.close()


# auto-close
with zipfile.ZipFile(tmp_path + 'Archive2.zip', 'w', zipfile.ZIP_LZMA) as newzip:
    newzip.write(tmp_path + "purchased.txt")
    newzip.write(tmp_path + "wishlist.txt")
