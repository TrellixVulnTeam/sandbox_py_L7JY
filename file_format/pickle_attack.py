import base64
import os
import pickle
import subprocess


class DeleteImportant:
    def __reduce__(self):
        # return os.remove, ("important.txt",)  # dangerous code
        # return subprocess.Popen, (("rm", "important.txt",),)  # dangerous code
        return os.getcwd, ()


data = pickle.dumps(DeleteImportant())
print(data)

string_data = str(base64.b64encode(data))
print(string_data)
string_data = string_data.lstrip("b").strip("'")
print(string_data)

data = base64.b64decode(string_data.encode())
print(data)
loaded = pickle.loads(data)
print(loaded)
