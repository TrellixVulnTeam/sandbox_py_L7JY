```namespace/reader/
python3 -m reader.compressed.bzipped ../../tmp/test.bz2 data compressed with bz2
python3 -m reader.compressed.gzipped ../../tmp/test.gz data compressed with gzip
```

```namespace/
python3 reader ../tmp/test.gz
python3 reader ../tmp/test.bz2
```

- Executable zip
```namespace/
cd reader
zip -r ../../tmp/reader.zip * -x "*/__pycache__/*"
cd ..
python3 ../tmp/reader.zip ../tmp/test.gz
```
