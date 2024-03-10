# ----------
# 画像名を一括で変更するPythonスクリプト
# ----------

import os

dir_folders = input("\n- フォルダ名を入力してください: ")

dir_pictures = os.listdir(dir_folders)

for i in dir_pictures:
    number = 1
    for j in os.listdir(dir_folders + "/" + i):
        ext = os.path.splitext(j)[1]
        file_before = dir_folders + "/" + i + "/" + j
        file_after = dir_folders + "/" + i + "/" + i + "_" + str(number) + ext
        os.rename(file_before, file_after)
        number += 1