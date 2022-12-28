import jsoner
import os
def info(id):
  if os.path.isfile(f"./data/id/{id}.json"):
    j=jsoner.jsoner(f"./data/id/{id}.json")
    result={
        "title":j.data.title,
        "desc":j.data.description+" "+j.data.instructions,
        "username":j.data.username,
        "stats":j.data.statistics,
        "id":j.data.id,
        "times":j.data.times
    }
    return result
  else:
    return None