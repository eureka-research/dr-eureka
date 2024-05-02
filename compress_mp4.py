import os
import subprocess

# Set the path to the main folder
main_folder = "/Users/jasonma/dreureka-website/videos"

# Recursively iterate through all subfolders
for root, dirs, files in os.walk(main_folder):
    for filename in files:
        # Check if the file has a .mp4 extension
        if filename.endswith(".mp4"):
            # Get the full path of the input file
            input_file = os.path.join(root, filename)
            
            # Create the output file name by adding "_compressed" before the extension
            output_file = os.path.splitext(filename)[0] + "_compressed.mp4"
            output_file = os.path.join(root, output_file)
            
            # Use FFmpeg to compress the video with more aggressive settings
            subprocess.call(['ffmpeg', '-i', input_file, '-vcodec', 'libx264', '-preset', 'slow', '-crf', '28', '-acodec', 'aac', '-b:a', '64k', output_file])
            
            print(f"Compressed {input_file} -> {output_file}")