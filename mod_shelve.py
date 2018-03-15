# shelve
import shelve

shelfFile = shelve.open('tmp/mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('tmp/mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
