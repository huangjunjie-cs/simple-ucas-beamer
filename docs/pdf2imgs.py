import os

from pdf2image import convert_from_path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BUILD_DIR = os.path.join(BASE_DIR, '..', 'build')

# 读取PDF文件
example_path = os.path.join(BUILD_DIR, 'dasfaa2023-example.pdf')
images = convert_from_path(example_path)

# 保存预览图像
for i in range(len(images)):
    save_path = os.path.join(BUILD_DIR, '_images', f'example_{i}.jpg')
    images[i].save(save_path, 'JPEG')
