import os

# 資料夾路徑
folder_path ='C:/Users/user/.cache/torch/hub/ultralytics_yolov5_master/runs/detect/exp6/labels'

# 檢查資料夾路徑是否存在
if not os.path.exists(folder_path):
    print("資料夾路徑不存在！")
    exit()

# 找出所有的.txt檔案
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# 排序所有的.txt檔案
sorted_txt_files = sorted(txt_files)

# 依序處理每個.txt檔案
for i, txt_file in enumerate(sorted_txt_files):
    # 檔案完整路徑
    file_path = os.path.join(folder_path, txt_file)

    # 讀取檔案內容
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # 檢查每一行的內容是否符合正確格式
    valid_lines = []
    for line in lines:
        line_split = line.split()
        if len(line_split) == 5:  # 檢查每行是否有五個元素
            try:
                int(line_split[0])  # 確認第一個元素可以轉換為整數
                valid_lines.append(line)
            except ValueError:
                print(f"檔案 {txt_file} 中的行 {line} 第一個元素無法轉換為整數，將被忽略。")
        else:
            print(f"檔案 {txt_file} 中的行 {line} 格式錯誤，將被忽略。")

    # 將符合正確格式的檔案內容依照類別排序
    sorted_lines = sorted(valid_lines, key=lambda x: int(x.split()[0]))

    # 覆寫排序後的檔案內容
    with open(file_path, 'w') as f:
        f.writelines(sorted_lines)

    print(f"已排序檔案 {txt_file} 中的內容。")

print("所有檔案排序完成！")
