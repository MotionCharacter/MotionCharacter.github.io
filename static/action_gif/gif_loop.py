import os
from moviepy.editor import VideoFileClip

def make_gif_loop(input_directory, output_directory):
    # 确保输出目录存在
    os.makedirs(output_directory, exist_ok=True)
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".gif"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"looped_{filename}")
            
            # Load GIF file
            clip = VideoFileClip(input_path)
            
            # Write the GIF with loop enabled
            clip.write_gif(output_path, loop=0)  # loop=0 means infinite loop
            
            print(f"Processed: {filename} -> {output_path}")

# 输入文件夹路径（包含待处理的 GIF 文件）
input_directory = "/content/input"

# 输出文件夹路径（存放循环播放的 GIF 文件）
output_directory = "/content/output"

make_gif_loop(input_directory, output_directory)
