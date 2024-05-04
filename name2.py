import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if '-' in filename:
            new_filename = filename.replace('-', '_')
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# 调用函数并传入要操作的文件夹路径
directory = 'D:/aidea-foot/train_20210106/labels'
rename_files(directory)