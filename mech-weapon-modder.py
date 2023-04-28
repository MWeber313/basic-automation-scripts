import json
import os
from tkinter import Tk 
from tkinter.filedialog import askdirectory



# current_dir = os.listdir('D:\Games\BATTLETECH Heavy Metal\BattleTech_Data\StreamingAssets\data\weapon')
select_dir = askdirectory(title="Select Folder")
current_dir = os.listdir(select_dir)




for file in current_dir:
    with open(f'{select_dir}\{file}', 'r+') as file_object:
        contents = json.load(file_object)
        print(contents.keys())
        if 'Capacity' in contents.keys():
            contents['Tonnage'] = 0.5
            contents['Capacity'] = 1000
        if 'Category' in contents.keys():
            if contents['Category'] == 'AntiPersonnel':
                contents['Tonnage'] = 0.5
            else:
                contents['Tonnage'] = 1
        file_object.seek(0)
        json.dump(contents, file_object, indent=4)
        file_object.truncate()
    # with open(file, 'r+') as file_object:
    #     contents = json.load(file_object)
    #     print(contents)
        
    # with open(f'D:\Games\BATTLETECH Heavy Metal\BattleTech_Data\StreamingAssets\data\weapon\{file}', 'r+') as file_object:
    #     if contents['Category'] == 'AntiPersonnel':
    #         contents['Tonnage'] = 0.5
    #     else:
    #         contents['Tonnage'] = 1
    #     file_object.seek(0)
    #     json.dump(contents, file_object, indent=4)
    #     file_object.truncate()

# for file in current_dir:
#     with open(file, 'r+') as file:
#         contents = json.load(file)
#         print(contents['Tonnage'])
#     # contents['Tonnage'] = 1
#     # print('Current Tonnage: ', contents['Tonnage'])



# print(os.getcwd())

