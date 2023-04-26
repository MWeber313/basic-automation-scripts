import json
import os

# with open('D:\Games\BATTLETECH Heavy Metal\BattleTech_Data\StreamingAssets\data\weapon\Weapon_Autocannon_AC2_0-STOCK-Copy.json', 'r+') as file_object:
#     contents = json.load(file_object)
#     contents['Tonnage'] = 10
#     file_object.seek(0)
#     json.dump(contents, file_object, indent=4)
#     file_object.truncate()

# print(contents['Tonnage'])

os.chdir('D:\Games\BATTLETECH Heavy Metal\BattleTech_Data\StreamingAssets\data\weapon')

current_dir = os.listdir('D:\Games\BATTLETECH Heavy Metal\BattleTech_Data\StreamingAssets\data\weapon')

for file in current_dir:
    with open(f'D:\Games\BATTLETECH Heavy Metal\BattleTech_Data\StreamingAssets\data\weapon\{file}', 'r+') as file_object:
        contents = json.load(file_object)
        contents['Tonnage'] = 1
        file_object.seek(0)
        json.dump(contents, file_object, indent=4)
        file_object.truncate()

# for file in current_dir:
#     with open(file, 'r+') as file:
#         contents = json.load(file)
#         print(contents['Tonnage'])
#     # contents['Tonnage'] = 1
#     # print('Current Tonnage: ', contents['Tonnage'])



# print(os.getcwd())

