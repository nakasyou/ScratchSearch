class ddic(dict): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.__dict__ = self
def jdic(dic:dict):
    d=ddic()
    for key in dic.keys():
        value=dic[key]
        if type(value)==dict:
            d[key]=jdic(value)
        else:
            d[key]=value
    return d