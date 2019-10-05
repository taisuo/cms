import json
def returnResult(code,msg,data=""):
    dic = {
        "code": code,
        "msg": msg,
        "data":data
    }
    dic1 = json.dumps(dic)
    return dic1