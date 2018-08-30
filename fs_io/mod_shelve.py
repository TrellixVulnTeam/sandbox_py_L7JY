# shelve
import shelve

TMP = "../tmp/"

shelfFile = shelve.open(TMP + "mydata")
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open(TMP + "mydata")
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
