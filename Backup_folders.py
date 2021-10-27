from distutils.dir_util import copy_tree
from datetime import datetime


today = datetime.today().strftime('%Y-%m-%d')


From=["C:/from/your/path/A",
      'C:/from/your/path/B'
      ]

To=["C:/to/your/path/A " + today,
    'C:/to/your/path/B ' + today
    ]

substring = "Path/to/Ignore"

for i in range(len(From)):
  if substring in To[i]: #not to overwrite in a certain folder
      print("Skipping " + From[i] + "destination path to be excluded")      
      continue
  copy_tree(From[i], To[i])
