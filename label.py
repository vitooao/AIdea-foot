import csv

def convert_to_yolo_label(row):
    image_name = row[0]
    x1, y1, x2, y2 = map(int, row[1:])
    width = 120
    height = 400
    
    label1 = f"0 {x1/width} {y1/height} 0.75 0.3"
    label2 = f"1 {x2/width} {y2/height} 0.5 0.1"
    
    return image_name, label1, label2


# 讀取CSV文件並轉換為YOLO標籤
filename = 'D:/aidea-foot/train_20210106/annotation.csv'  # 請替換為你的CSV文件名稱
output_directory = 'D:/aidea-foot/train_20210106/labels'  # 請替換為你想要保存標籤的目錄

with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳過標題行
    yolo_labels = [convert_to_yolo_label(row) for row in reader]

# 生成YOLO標籤檔案
for image_name, label1, label2 in yolo_labels:
    output_filename = f"{output_directory}/{image_name.replace('.png', '.txt').replace('.jpg', '.txt').replace('.JPG', '.txt')}"
    with open(output_filename, 'w') as file:
        file.write(label1 + '\n')
        file.write(label2 + '\n')
