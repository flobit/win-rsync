import os
import sys
import re

def trans_cygwin_path_to_windows(path):
    if(path.startswith("/cygdrive/")):
        return path[10]+":/"+path[12:]
    else:
        return path
    
def trans_windows_arg_path_to_cygwin(path):
    match_result = re.match("([a-z]:)\\\\.*", path, re.IGNORECASE)
    if match_result:
        disk_label = match_result.groups()[0]
        return path.replace(disk_label, "/cygdrive/"+disk_label[0].lower()).replace("\\", "/")
    else:
        return path

def trans_windows_path_to_cygwin(path):
    return trans_windows_arg_path_to_cygwin(path).replace("\\", "/")

def trans_param(param):
    # process file
    if param.startswith("--files-from="):
        file_path=trans_cygwin_path_to_windows(param[13:])
        with  open(file_path,"r+") as list_file:
            file_content="".join([trans_windows_path_to_cygwin(line) for line in list_file.readlines()])
            list_file.seek(0)
            list_file.write(file_content)
            print(file_content)
    return "\"" + trans_windows_arg_path_to_cygwin(param) + "\""
        
    


launcher_file_dir = os.path.dirname(sys.executable)
os.environ["path"] = launcher_file_dir + "\\bin"+";"+os.environ["PATH"]
os.environ["CWRSYNCHOME"] = launcher_file_dir

rsync_final_params = str.join(" ", [trans_param(arg) for arg in sys.argv[1:]])

print(rsync_final_params)
# print(launcher_file_dir)

os.system("real_rsync "+rsync_final_params)
