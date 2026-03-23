import random
import os
import ctypes
usrname = os.getlogin()
home = f"C://Users/{usrname}"
check = 0
nope = ['no', 'nah', 'n', '0']

extractcmd = f'tar -xf ./backgrounds.zip -C "{home}/Pictures"'
try:
    with open(f"{home}/Documents/statusbgrandom.txt", mode = 'rt') as file1:
        for line in file1:
            check += int(line)
        print(check)
except FileNotFoundError:
    x = input("This program will extract roughly 100-200 megabytes of data to your Pictures folder. Rest assured, these are all photos. If you want to use your own backgrounds, answer 'NO'(letter for letter, fully capitalized), and then replicate the folder structure that is printed to the console, before placing your images in the appropriate folders.")
    if x == 'NO':
        print('''~/Pictures-
    -backgrounds
        -landscapes
        -minimalscape
        -geometric
        -flowy
        -space
        -cityscapes
''')
        input("Click [ENTER] when you have finished creating the appropriate file structure and uploaded your images.")
        os.system(f'echo 1 >> "{home}/statusbgrandom.txt"')
    else:
        os.system(f'echo 1 >> "{home}/Documents/statusbgrandom.txt"')
        check = input("Is your pictures folder stored in OneDrive?.(Y/n) ").lower()
        if check in nope:
            os.system(f'mkdir "{home}/Pictures"')
        else:
            home += 'OneDrive'
        os.system(f'{extractcmd}')
        os.system(f'echo 1 >> "{home}/Documents/statusbgrandom.txt"')


landscapes = home + '/Pictures/backgrounds/landscapes/'
minimalscapes = home + '/Pictures/backgrounds/minimalscape/'
geometric = home + '/Pictures/backgrounds/geometric/'
flowy = home + '/Pictures/backgrounds/flowy/'
space = home + '/Pictures/backgrounds/space/'
cityscapes = home + '/Pictures/backgrounds/cityscapes/'


folderls = [
    landscapes,
    minimalscapes,
    geometric,
    flowy,
    space,
    cityscapes
    ]

todayfolder = folderls[random.randint(0, 5)]
print(todayfolder)

pictures = os.listdir(todayfolder)
print(pictures)

def count(dirlist):
    count = 0
    for file in dirlist:
        count += 1
    return count

count = count(pictures)
randpic = pictures[random.randint(0, count - 1)]
todaypicture = os.path.abspath(os.path.join(todayfolder, randpic))
print(todaypicture)
ctypes.windll.user32.SystemParametersInfoW(20, 0, todaypicture, 3)
