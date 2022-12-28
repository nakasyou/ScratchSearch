from flask import Flask, request, make_response
import jinja2
import search
import indexer
from jsoner import jsoner
from info import info
app = Flask(__name__)

def jinjafile(path,**d):
  if request.args.get("lang"):
    lang=request.args.get("lang")
  elif request.cookies.get('lang'):
    lang=request.cookies.get('lang')
  else:
    lang=request.headers.get('Accept-Language').split(",")[0].split("-")[0]
  with open(path) as f:
    text=jinja2.Template(f.read()).render(**d)
  trn=jsoner("./html/translate.json")
  for t in trn.data:
    v=trn.data[t]
    if lang in v:
      text=text.replace(t,v[lang])
  resp=make_response(text)
  resp.set_cookie('lang',lang)
  return resp
@app.route('/')
def index():
  return jinjafile("./html/index.html")
@app.route("/search")
def searchuser():
  q=str(request.args.get("q"))
  if len(q)<5:
    return jinjafile("./html/400.html",seq="Search string must be at least 5 characters"),400
  result=search.search(q)
  return jinjafile("./html/result.html",result=result,q=q)
@app.route("/adder")
def adder():
  id=str(request.args.get("id"))
  if id!="None" and id!="":
    i=indexer.index(id)
    print(i)
    if i:
      return jinjafile("html/adder.html",msg="success!")
    else:
      return jinjafile("html/adder.html",msg="invald id or not found id.")
  else:
    return jinjafile("html/adder.html")
@app.route("/portal/<id>")
def portal(id):
  return jinjafile("./html/portal.html",id=id,info=info(id))
app.run(host='0.0.0.0', port=81)
