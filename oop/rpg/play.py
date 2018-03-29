from thievs import Thief

hoge = Thief(name="Hoge", sneaky=False)  # 多重継承の場合は、positionalに頼るべきではない。
print(hoge)
print(hoge.sneaky)
print(hoge.agile)
print(hoge.hide(8))
