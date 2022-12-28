import unicodedata
import pykakasi
def jpfy(d):
  kks = pykakasi.kakasi()
  d=d.lower()
  d=unicodedata.normalize('NFKC',d)
  result=[]
  for w in kks.convert(d):
    result.append(w["hepburn"])
  return "".join(result)
if __name__=="__main__":
  print(jpfy("私はあなや。ああAａａａａａカカカｶ"))