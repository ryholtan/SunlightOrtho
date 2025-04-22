from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import crop

# Load the newly uploaded video
video_path = "images/sunflowers.mp4"
clip = VideoFileClip(video_path)

# Crop the top half (cut top 400px from a 800px tall video)
height = clip.h
cropped_clip = crop(clip, y1=height // 1.5)

# Save the cropped video
output_path = "images/sunflowers_cropped_bottom_half.mp4"
cropped_clip.write_videofile(output_path, codec="libx264", audio=False)

output_path
