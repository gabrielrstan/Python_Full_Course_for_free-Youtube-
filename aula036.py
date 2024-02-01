import os
import shutil

path = 'pasta2/test copy.txt'
path2 = 'em'
path3 = 'pasta copy'

try:
   # os.remove(path)
   # os.rmdir(path2)
    shutil.rmtree(path3)
except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
except OSError as e:
    print(e)
else:
    print(path3 + " foi excluido")