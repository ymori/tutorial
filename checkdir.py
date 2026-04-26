import pathlib
import glob
import pprint
p_temp = pathlib.Path('mygame')

pprint.pprint(list(p_temp.glob('**/*.png')))

print("Hello2")
print("Hello3")
print("UpdateTest")
print("UpdateTest2")
print("UpdateTest3")
print("UpdateOnlyVSCode")