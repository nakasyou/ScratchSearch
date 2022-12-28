import requests
from jdic import jdic
import hash
import jpfy
from jsoner import jsoner
def index(id):
  result=requests.get("https://scratchdb.lefty.one/v3/project/info/"+str(id))
  result=jdic(result.json())
  if "error" in result:
    return None
  try:
    id=int(id)
  except:
    return None
  title=result.title
  desc=result.description
  instr=result.instructions
  user=result.username
  seq=(title+desc+instr+user)\
    .replace(" ","")\
    .replace("\n","")
  seq=jpfy.jpfy(seq)
  datas=[seq[i:i+5] for i in range(len(seq)-5)]
  result["words"]=datas
  
  idjson=jsoner(f"./data/id/{id}.json",{"words":[]})
  for delword in idjson.data.words:
    d=jsoner(f"./data/word/{hash.md5(delword)}.json",{"word":datas,"ids":[]})
    if delword in d.data.ids:
      d.data.ids.remove(id)
      d.save()
  for data in datas:
    wordjson=jsoner(f"./data/word/{hash.md5(data)}.json",{"word":data,"ids":[]})
    if not id in wordjson.data.ids:
      wordjson.data.ids.append(id)
    wordjson.save()
  idjson.data=result
  idjson.save()

  with open("./data/reserves/users.txt") as f:
    usersdata=f.read().split("\n")
  if not user in usersdata:
    usersdata.append(user)
    usersdata.sort()
    with open("./data/reserves/users.txt","w") as f:
      f.write("\n".join(usersdata))
  return True
if __name__=="__main__":
  index(522557780)