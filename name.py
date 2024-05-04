import os

def rename_files(folder_path):
    # 取得資料夾中所有檔案的清單
    file_list = os.listdir(folder_path)
    
    for file_name in file_list:
        # 建立原始檔案的完整路徑
        old_file_path = os.path.join(folder_path, file_name)
        
        # 取得檔案的檔名與副檔名
        base_name, extension = os.path.splitext(file_name)
        
        # 建立新的檔案名稱，加上"<-2>"
        new_file_name = f"{base_name}_2{extension}"
        
        # 建立新檔案的完整路徑
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # 將檔案重新命名
        os.rename(old_file_path, new_file_path)

# 指定要進行檔案改名的資料夾路徑
folder_path = "D:/aidea-foot/train_20210106/labels"

# 呼叫函式進行檔案改名
rename_files(folder_path)
