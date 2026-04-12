"""
生成Android应用图标
"""
from PIL import Image, ImageDraw, ImageFont
import os

# 图标尺寸配置
sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192,
}

# 创建图标
def create_icon(size):
    # 创建图像
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制圆形背景
    margin = size // 10
    draw.ellipse([margin, margin, size-margin, size-margin], 
                 fill=(98, 0, 238, 255))  # 紫色背景
    
    # 绘制时钟图标
    center = size // 2
    radius = size // 3
    
    # 时钟外圈
    draw.ellipse([center-radius, center-radius, 
                  center+radius, center+radius], 
                 outline=(255, 255, 255, 255), width=max(2, size//24))
    
    # 时钟中心点
    dot_size = max(2, size//32)
    draw.ellipse([center-dot_size, center-dot_size, 
                  center+dot_size, center+dot_size], 
                 fill=(255, 255, 255, 255))
    
    # 时针
    hour_len = radius * 0.5
    draw.line([center, center, 
               center, center - hour_len], 
              fill=(255, 255, 255, 255), width=max(2, size//32))
    
    # 分针
    min_len = radius * 0.7
    draw.line([center, center, 
               center + min_len*0.7, center - min_len*0.7], 
              fill=(255, 255, 255, 255), width=max(1, size//48))
    
    return img

# 生成各尺寸图标
base_path = 'android-app/app/src/main/res'

for folder, size in sizes.items():
    # 创建目录
    dir_path = os.path.join(base_path, folder)
    os.makedirs(dir_path, exist_ok=True)
    
    # 生成图标
    icon = create_icon(size)
    
    # 保存图标
    icon_path = os.path.join(dir_path, 'ic_launcher.png')
    icon.save(icon_path, 'PNG')
    print(f'生成: {icon_path} ({size}x{size})')
    
    # 保存圆形图标
    round_path = os.path.join(dir_path, 'ic_launcher_round.png')
    icon.save(round_path, 'PNG')
    print(f'生成: {round_path} ({size}x{size})')

print('\n✅ 图标生成完成！')
