import os

# 给当前目录下的images文件夹中所有文件按照一定规律重命名
path  = 'images'
imgs = os.listdir(path)

i = 20
for img in imgs:
    print(img)
    os.rename(os.path.join(path, img), os.path.join(path, str(i)+".jpg"))
    i+=1
