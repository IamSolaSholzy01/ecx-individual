from moviepy.editor import *
from moviepy.video.fx.speedx import speedx

def change_speed(clip, factor):
    """
    INPUT: Filename with path. String
    INPUT: Speed factor. Float

    OUTPUT: New video. MOV
    """
    
    video_clip = VideoFileClip(clip)
    print("...")
    print("...")
    new_clip = speedx(video_clip, factor)
    new_clip.to_gif("new_video.mov")
    return new_clip

video = input('Enter the video file :')
speed = float(input('What speed do you want? :'))

change_speed(video, speed)