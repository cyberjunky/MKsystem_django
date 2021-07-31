import pandas as pd
from datetime import datetime
import shutil
from pathlib import Path
import os

# path_log = "MKsystemApp/management/commands/log/"
path_log = "log/"

def print_log(str_log, name_file):
    # logフォルダがなければ作成
    if not os.path.isdir(path_log):
        os.mkdir(path_log)
        str_log = "[print_log]mkdir {}".format(path_log)
        print_log(str_log, name_file)

    str_print_log = "{} {}" \
        .format(datetime.now().strftime("%H:%M:%S"), str_log)
    print(str_print_log)
    path_log_targ = path_log + name_file + '_'
    str_ftime = datetime.now().strftime("%Y%m%d")
    file_object = open(
        path_log_targ + str_ftime + '.log', "a+")
    file_object.writelines(str_print_log + "\n")
    file_object.close()
