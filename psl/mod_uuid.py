# Generating unique identifiers
import uuid

# use the uuid4 function to create a random sequence using
# the underlying os.urandom() function
result = uuid.uuid4()
print("UUID4: ", result)
result = uuid.uuid4()
print("UUID4: ", result)

print('---')

# create a UUID using uuid5, which takes a namespace and
# name value. Note that this version is not crypto-safe
result = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print("UUID5: ", result)
result = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print("UUID5: ", result)

print("~~~~~~~~~~~~~~~~~~~~~~~")

# format
result = uuid.uuid4()
print(result)
print(result.hex)
print(result.urn)
print(result.fields)
print(result.node)
