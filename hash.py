import hashlib

def md5(d):
  
  
  return hashlib.md5(d.encode()).hexdigest()