import os

folder_path = "D:/aidea-foot/train_20210106/labels"  # 指定要更改文件的文件夹路径

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        # 构造新的文件名
        new_filename = os.path.splitext(filename)[0] + ".txt"
        
        # 构造完整的文件路径
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)
        
        # 重命名文件
        os.rename(old_filepath, new_filepath)
