import os
import json
from jdic import jdic
class jsoner:
  def __init__(self,path,default={}):
    self.path=path
    if not os.path.isfile(path):
      with open(path,"w") as f:
        f.write(json.dumps(default))
    with open(path) as f:
      self.data=jdic(json.load(f))
  def save(self):
   with open(self.path,"w") as f:
     f.write(json.dumps(self.data))