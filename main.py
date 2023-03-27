import os
from shutil import move
from pathlib import Path

user_name_path = os.path.expanduser("~")
desktop_folder = Path(f'{user_name_path}/Desktop')
downloads_folder = Path(f'{user_name_path}/Downloads')
target_folder = Path(f'{user_name_path}/')

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx', '.csv', '.CSV')
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


# function to loop through source folder
def get_non_hidden_files_except_current_file(source_folder):
    return [f for f in os.listdir(source_folder) if os.path.isfile(f"{source_folder}/{f}") and not f.startswith('.') and not f.__eq__(__file__)]


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


def file_mover(files, source_folder):
    for file in files:
        if file.endswith(doc_types):
            move_files(file, source_folder, Path(target_folder/'Documents'))
        elif file.endswith(audio):
            move_files(file, source_folder, Path(target_folder/'Music'))
        elif file.endswith(video):
            move_files(file, source_folder, Path(target_folder/'Videos'))
        elif file.endswith(img):
            move_files(file, source_folder, Path(target_folder/'Pictures'))
        else:
            continue


def options():
    print("Which folders would like to clean up?\n"
          "1. Downloads\n"
          "2. Desktop\n"
          "3. Downloads & Desktop\n")
    option_number = user_input_validation(input("Type here: "))
    if option_number == 1:
        move_downloads_folder()
        print("Done! Downloads folder cleaned up")
    elif option_number == 2:
        move_desktop_folder()
        print("Done! Desktop folder cleaned up")
    elif option_number == 3:
        move_downloads_folder()
        move_desktop_folder()
        print("Done! Desktop and Downloads folders cleaned up")


def move_downloads_folder():
    user_input = input(f'Is this path to Downloads folder correct: {downloads_folder}(y/n):\n')
    if user_input.upper() == "Y":
        files_to_move = get_non_hidden_files_except_current_file(downloads_folder)
        file_mover(files_to_move, downloads_folder)
    else:
        corrected_path = input("Type correct path:\n")
        files_to_move = get_non_hidden_files_except_current_file(corrected_path)
        file_mover(files_to_move, corrected_path)


def move_desktop_folder():
    user_input = input(f'Is this path to Desktop folder correct: {desktop_folder}(y/n):\n')
    if user_input.upper() == "Y":
        files_to_move = get_non_hidden_files_except_current_file(desktop_folder)
        file_mover(files_to_move, desktop_folder)
    else:
        corrected_path = input("Type correct path:\n")
        files_to_move = get_non_hidden_files_except_current_file(corrected_path)
        file_mover(files_to_move, corrected_path)


def user_input_validation(input_to_validate):
    # validating user input
    if input_to_validate.isdigit():
        converted_user_input = int(input_to_validate)
        if converted_user_input == 1:
            return converted_user_input
        elif converted_user_input == 2:
            return converted_user_input
        elif converted_user_input == 3:
            return converted_user_input
        else:
            print("Invalid input")
    else:
        print("Invalid input")


if __name__ == "__main__":
    options()






