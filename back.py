import os
import csv

# 資料夾路徑
folder_path = 'C:/Users/user/.cache/torch/hub/ultralytics_yolov5_master/runs/detect/exp6/labels'

# CSV 檔案路徑
csv_file = 'D:/aidea-foot/output5.csv'

# 取得資料夾中的所有 txt 檔案
txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

# 建立 CSV 檔案並寫入標題行
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['images', 'x1', 'y1', 'x2', 'y2'])

    # 逐個處理 txt 檔案
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)

        # 替換檔案名稱中的 ".txt" 為 ".png"
        png_file = txt_file.replace('.txt', '.png')

        # 讀取檔案並提取數字
        with open(file_path, 'r') as txt:
            lines = txt.readlines()
            line1_nums = lines[0].split()
            line2_nums = lines[1].split()

            # 計算數字乘以指定值並移除小數點
            line1_num2_result = int(float(line1_nums[1]) * 120)
            line1_num3_result = int(float(line1_nums[2]) * 400)
            line2_num2_result = int(float(line2_nums[1]) * 120)
            line2_num3_result = int(float(line2_nums[2]) * 400)

            # 將資訊寫入 CSV 檔案
            writer.writerow([png_file, line1_num2_result, line1_num3_result, line2_num2_result, line2_num3_result])
