import os
import easygui

path = easygui.diropenbox()

# for root, dirs, files in os.walk(".", topdown = False):
# for root, dirs, files in os.walk(path):
    # for file in files:
        # print(root + '\\' + file)

f = open(path + '\.gitignore', 'w', encoding='utf-8')

for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            f.write(file + '\n')
            print(file)


for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        f.write(dir + '\n')
        print(dir)

f.close()

input('Create .gitignore in your directory')