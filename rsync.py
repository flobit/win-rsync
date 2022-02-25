import os
import sys
import re


def trans_param(param):
    match_result = re.match("([a-z]:)\\\\.*", param,re.IGNORECASE)
    if match_result:
        disk_label = match_result.groups()[0]
        return param.replace(disk_label,"/cygdrive/"+disk_label[0].lower()).replace("\\","/")
    else:
        return param


launcher_file_dir = os.path.dirname(sys.executable)
os.environ["path"] = launcher_file_dir + "\\bin"+";"+os.environ["PATH"]
os.environ["CWRSYNCHOME"] = launcher_file_dir

rsync_final_params=str.join(" ",[ trans_param(arg) for arg in sys.argv[1:]])

# print(rsync_final_params)
# print(launcher_file_dir)

os.system("real_rsync "+rsync_final_params)
