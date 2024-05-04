import torch
import os
import csv
from PIL import Image

# 載入模型
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/user/Desktop/traffic/env/fish8.pt')

# 設定資料夾路徑
folder_path = 'C:/Users/user/.cache/torch/hub/ultralytics_yolov5_master/data/images/'

# 設定 CSV 檔案名稱
csv_filename = 'submission.csv'

# 開啟 CSV 檔案並寫入標題行
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['image_filename', 'label_id', 'x', 'y', 'w', 'h', 'confidence'])

    # 取得資料夾內所有的檔案
    file_list = os.listdir(folder_path)

    # 迭代處理每個圖片檔案
    for file in file_list:
        if file.lower().endswith(('.jpg', '.png')):
            image_path = os.path.join(folder_path, file)

            # 進行物件偵測
            results = model(image_path)

            # 取得偵測結果
            detections = results.pred[0]

            # 將偵測結果寫入 CSV 檔案
            for det in detections:
                label = int(det[5]) + 1
                conf = round(det[4].item(), 6)  # 保留到小數第六位
                bbox = det[:4]
                
                xmin, ymin, xmax, ymax = map(int, bbox)
                width = xmax - xmin
                height = ymax - ymin

                csv_writer.writerow([file, label, xmin, ymin, width, height, conf])
