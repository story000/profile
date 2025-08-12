#!/usr/bin/env python3
import os
import json

def generate_image_lists():
    """生成所有项目的图片列表JSON文件"""
    base_dir = os.path.dirname(__file__)
    images_dir = os.path.join(base_dir, 'images')
    
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.svg')
    all_images = {}
    
    if os.path.exists(images_dir):
        for project_folder in os.listdir(images_dir):
            project_path = os.path.join(images_dir, project_folder)
            
            # 跳过非文件夹和README
            if not os.path.isdir(project_path) or project_folder.startswith('.'):
                continue
                
            images = []
            try:
                files = os.listdir(project_path)
                for file in files:
                    if file.lower().endswith(image_extensions):
                        images.append(file)
                
                # 按文件名排序
                images.sort()
                
                # 项目配置：图片列表 + 封面图片选择
                project_config = {
                    "images": images,
                    "cover_image": images[0] if images else None  # 默认第一张图片作为封面
                }
                
                all_images[project_folder] = project_config
                
                print(f"项目 {project_folder}: 找到 {len(images)} 张图片")
                for i, img in enumerate(images):
                    cover_indicator = " (封面)" if i == 0 else ""
                    print(f"  - {img}{cover_indicator}")
                    
            except OSError as e:
                print(f"读取 {project_folder} 文件夹时出错: {e}")
                all_images[project_folder] = {"images": [], "cover_image": None}
    
    # 写入JSON文件
    output_file = os.path.join(base_dir, 'images-list.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_images, f, indent=2, ensure_ascii=False)
    
    print(f"\n图片列表已保存到: {output_file}")
    return all_images

if __name__ == '__main__':
    generate_image_lists()