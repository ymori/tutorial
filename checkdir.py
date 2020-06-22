import pathlib
import glob
import pprint
p_temp = pathlib.Path('mygame')

pprint.pprint(list(p_temp.glob('**/*.png')))

print("Hello2")
