from django.http import HttpResponse
import os
import json

nameFolder = 'botstatus'
# デバッグの時はこっち
# nameFolder = '../../botstatus'
    
def get_filedata(dict_botstatus, bot_no):
    if os.path.exists(nameFolder + "/bot{}.txt".format(bot_no)):
        file_txt = open(nameFolder + "/bot{}.txt".format(bot_no), "r")
        lines = file_txt.readlines()
        if len(lines) > 0:
            line = lines[-1].replace("\n", "").split(" ")
        else:
            line = ""
        dict_botstatus["bot{}".format(bot_no)] = line
    else:
        dict_botstatus["bot{}".format(bot_no)] = ""
    
    return dict_botstatus
    

def get_botstatus():
    dict_botstatus = {}
    
    # それぞれのBotの状態を取得
    dict_botstatus = get_filedata(dict_botstatus, "1")
    dict_botstatus = get_filedata(dict_botstatus, "2")
    dict_botstatus = get_filedata(dict_botstatus, "3")
 
    return HttpResponse(json.dumps(dict_botstatus))


