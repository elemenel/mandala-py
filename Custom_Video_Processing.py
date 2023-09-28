'''Custom_Video_Processing.py'''

import moviepy.editor as mp
from moviepy.editor import *
from moviepy.editor import AudioFileClip, ImageClip, VideoFileClip, concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip

import My_logger as Lg
global new_fps


# Use to concatenate two videos
def concatenate_my_videos():
    print(f'Starting concatenate_my_videos')
    Lg.logger.info(f'Starting concatenate_my_videos')
    #Paths to the two video files
    clip1 = VideoFileClip('/media/sels/Productions/Videos/no_audio/Breathing Yin-Yang with 417-1251-2085 Hz Solfeggio 3rd and 5th Harmonic Frequency Tones-36min-232312555.mp4')
    clip2 = VideoFileClip('/media/sels/Productions/Videos/no_audio/Breathing Yin-Yang angles with 264-528-1056-2112 Hz Harmonic Tones-60min-232293914.mp4')
    #Merge the two files together using concatenation
    final_clip = concatenate_videoclips([clip1, clip2])
    #Write and save the new file to desired location
    final_clip.write_videofile('/home/sels/Videos/Mixing Folder/Double-Breath Color-Changing Yin-Yang.mp4')
    print(f'Completed concatentate_my_videos')
    Lg.logger.info(f'Completed concatenate_my_videos')
concatenate_my_videos()


global new_fps

def change_frame_rate():
    global new_fps
    print(f'Starting change_frame_rate')
    Lg.logger.info(f'Starting change_frame_rate')
    #Load the video clip
    clip = VideoFileClip('/home/sels/Videos/Mixing Folder/Double-Breath Color-Changing Yin-Yang.mp4')
    print(f'FPS = {clip.fps} fps')
    Lg.logger.info(f'FPS = {clip.fps} fps')
    #Set the desired frame rate
    new_fps = clip.fps * 5
    print(f'New FPS = {new_fps} fps')
    Lg.logger.info(f'New frame rate: {new_fps} fps')
    #Change the frame rate of the clip
    new_clip = clip.set_fps(new_fps)
    new_clip.write_videofile(f'/home/sels/Videos/Mixing Folder/Double-Breath Color-Changing Yin-Yang at {new_fps} .mp4')
    print(f'Completed change_frame_rate')
    Lg.logger.info(f'Completed change_frame_rate')
change_frame_rate()    
 
 
 
 
 # Append 1/2 of video to produce a full picture ending instead of a blank screen
def end_with_full_image():
    print(f'Starting end_with_full_image')
    Lg.logger.info(f'Starting end_with_full_image')             
    #Get path of clip
    clip = VideoFileClip(f'/home/sels/Videos/Mixing Folder/Double-Breath Color-Changing Yin-Yang at {new_fps} .mp4')
    duration = clip.duration
    print(f'Duration: {duration / 60} minutes')
    Lg.logger.info(f'Duration:  {duration/60} minutes')            
    print(f'3/4 Duration: {duration /60 *.74}  minutes')
    Lg.logger.info(f'3/4 Duration:  {duration/60 * .74} minutes')  
    three_quarter_clip = clip.subclip(0, clip.duration * .74)
    full_clip = concatenate_videoclips( [clip, three_quarter_clip])
    full_clip.write_videofile(f'/home/sels/Videos/Mixing Folder/Double-Breath Color-Changing Yin-Yang at {new_fps} with full image .mp4')
    print(f'Completed end_with_full_image')
    Lg.logger.info(f'Completed end-with_full_image')              
end_with_full_image()                    
    
    
    
                             
                             