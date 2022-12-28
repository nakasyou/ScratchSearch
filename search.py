import jsoner
import os
import jpfy
import hash
def search(seq):
  seq=jpfy.jpfy(seq)
  words=[seq[i:i+5] for i in range(len(seq)-5)]
  result={}
  for word in words:
    h=hash.md5(word)
    if os.path.isfile(f"./data/word/{h}.json"):
      json=jsoner.jsoner(f"./data/word/{h}.json")
      for id in json.data.ids:
        id=int(id)
        if id in result:
          result[id]+=1
        else:
          result[id]=1
  data = sorted(result.items(), key=lambda x:x[0])
  result=[]
  for d in data:
    if os.path.isfile(f"./data/id/{d[0]}.json"):
      j=jsoner.jsoner(f"./data/id/{d[0]}.json")
      result.append({
        "title":j.data.title,
        "desc":j.data.description+" "+j.data.instructions,
        "username":j.data.username,
        "stats":j.data.statistics,
        "n":d[1],
        "id":j.data.id,
        "times":j.data.times
      })
  return result
if __name__=="__main__":
  print(search("grifpatch"))