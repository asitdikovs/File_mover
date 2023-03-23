import os
from shutil import move

user_name_path = os.path.expanduser("~")
root_dir = f'{user_name_path}/Documents/Python/File Mover/Root_folder/'
destination_path = f'{user_name_path}/Documents/Python/File Mover/Folder_to_move/'
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")


# function to loop through root folder
def get_non_hidden_files_except_current_file(source_folder):
    return [f for f in os.listdir(source_folder) if os.path.isfile(source_folder + f) and not f.startswith('.') and not f.__eq__(__file__)]


# function to move and rename files if they exist in target folder
def move_files(filename, source_folder, destination_folder):
    src = os.path.join(source_folder, filename)
    i = 0
    while True:
        base = os.path.basename(src)
        name = base if i == 0 else "_{}".format(i).join(os.path.splitext(base))
        dst_path = os.path.join(destination_folder, name)
        if not os.path.exists(dst_path):
            move(src, dst_path)
            break
        i += 1


def file_mover(files):
    for file in files:
        if file.endswith(doc_types):
            move_files(file, root_dir,destination_path + 'Documents')
        elif file.endswith(audio):
            move_files(file, root_dir,destination_path + 'Music')
        elif file.endswith(video):
            move_files(file, root_dir,destination_path + 'Videos')
        elif file.endswith(img):
            move_files(file, root_dir,destination_path + 'Pictures')
        else:
            move_files(file, root_dir, destination_path + 'Other')


if __name__ == "__main__":
    files_to_move = get_non_hidden_files_except_current_file(root_dir)
    file_mover(files_to_move)





