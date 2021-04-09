program dir: reader_prg/
root package: reader
sub packages: compressed, util

```
# at namespace/reader_prg/
# create compressed files
python3 -m reader.compressed.bzipped ../../tmp/test.bz2 data compressed with bz2
python3 -m reader.compressed.gzipped ../../tmp/test.gz data compressed with gzip
```

- "import *" with "__all__" demo
```
# at namespace/
from reader.compressed import *
print(locals())
```

- Executable directory
```
# at namespace/
# read with reader_prg/__main.py__
python3 reader_prg ../tmp/test.gz
python3 reader_prg ../tmp/test.bz2
```

- Executable zip
```
# at namespace/
cd reader_prg
zip -r ../../tmp/reader.zip * -x "*/__pycache__/*"
cd ..
python3 ../tmp/reader.zip ../tmp/test.gz
```

- Executable package
```
# at namespace/reader_prg
# read with reader/__main.py__
python3 -m reader ../../tmp/test.gz
```
