import sys
from PIL import Image
import os
# 图像的绝对路径
image_path = '/Users/ljch/Desktop/test-1/git/photo_6289301662044196242_y.jpg'

try:
    # 尝试使用 Pillow 打开并验证
    img = Image.open(image_path)
    print(f"成功加载图片: {img.format}, {img.size}, {img.mode}")
    
    # 在 MacOS 上，这通常会自动打开系统的“预览(Preview)”应用来展示图片
    img.show()
except FileNotFoundError:
    print(f"找不到图片: {image_path}")
except ImportError:
    print("需要安装 Pillow 库。请在终端运行: pip install Pillow")
#test




