# Demonstration of reading a binary file (planets)
# use "planet-writer.c" for creating input data

import struct

record_size = 40  # No. of bytes in a planet record

# Just read the fifth record
with open("../tmp/planets.dat", "rb") as file:
    file.seek(4 * record_size)
    content = file.read(record_size)

    pos, name, moons, mass = struct.unpack("@i20sid", content)
    # Convert byte sequence to a string and strip the trailing nulls
    name = name.decode().rstrip("\0")

    print("%d: %8s: %2d moons, mass = %6.2f" % (pos, name, moons, mass))

# Loop over all records
with open("../tmp/planets.dat", "rb") as file:
    # Read the entire file in one go
    content = file.read()
    for pos, name, moons, mass in struct.iter_unpack("@i20sid", content):
        name = name.decode().rstrip("\0")
        print("%d: %8s: %2d moons, mass = %6.2f" % (pos, name, moons, mass))
