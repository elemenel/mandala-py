'''audio_clips.py organizes all audio services, including file links to audio clips,
sorting and grouping clips based on varied parameters, for use in the master_mandala_maker. py and the FileScripts.py modules.
Copyright(C) by Leon R. Hatton 2017-2024
'''
import sys
import random
import os
import platform
import glob
from moviepy.editor import *
from moviepy.editor import AudioFileClip, ImageClip, VideoFileClip
from functools import lru_cache
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
import Timer as Tm
import logging
import My_template as t
import natsort
import My_logger as Lg



logger = Lg.logging.getLogger(t.my_project) # Initialize global logger
logger = Lg.logging.getLogger(t.my_project) # Initialize global logger
fileHandler = Lg.logging.FileHandler ('/home/sels/Modules/MandalaMaker/Logs/Durations/Durations.log')
fileHandler.setLevel(Lg.logging.INFO)
consoleHandler = Lg.logging.StreamHandler()
consoleHandler.setLevel(Lg.logging.INFO)
logger.setLevel(Lg.logging.INFO)
logger.addHandler(Lg.fileHandler)
logger.addHandler(Lg.consoleHandler)
logger.info('Logger Source: audio_clips.py')
logger.info('********************************************************************')

# Comment out to disable output of long file lists to console. This is the default
# consoleHandler = logging.StreamHandler()
# consoleHandler.setLevel(logging.INFO)
# logger.setLevel(logging.INFO)
# logger.addHandler(consoleHandler)

#Output of time functions commented out (default)
# time_functions()
# logger.info('date_time:  ' + str(date_time))
# logger.info('my_date:  ' + str(my_date))
# logger.info('my_time  :' + str(my_time))
# logger.info('now  :'+  str(now))
# logger.info('project_time:  ' + str(project_time))


global my_path, my_music_path, my_audio_clip, my_track

if sys.platform.startswith('linux'):
    my_path = '/home/sels/Modules/MandalaMaker'
    my_no_audio_video_path = '/home/sels/Videos/no_audio/'
    my_full_vids_video_path = '/home/sels/Videos/Full_Vids/'
    my_music_path = '/home/sels/Music/Audio Clips for Python'
    
else:
    my_music_path = 'M:/Music'
    my_path = 'M:'
    my_no_audio_video_path = 'M:/Videos/no_audio/'
    my_full_vids_video_path = 'M:/Videos/Full_Vids/'

Tm.set_time()
    
# print(my_music_path)
extra_long_clips = []
long_clips = []
medium_clips = []
short_clips = []
custom_length_clips = []

global i
i = 0

# music_clips  ---Music list

# Determine and manage the duration categories (i.e short, medium, long, extra long)


def get_music_file_duration():   # Manually adjustable as noted
    global musicclip_duration
    Audio_length = MP3(i)
    musicclip_duration = round(int(Audio_length.info.length/60))
    Lg.logger.info('The duration of  ' + str(i) +' is:  ' + str(musicclip_duration) + '  minutes')
    Lg.logger.info('=================================================================================================')
    if musicclip_duration in range(int(26), int(72)): # Anything, looking for x min duration clips only
        custom_length_clips.append(i)
    elif musicclip_duration in range(int(1300), int(1700)): #Adjustable
        extra_long_clips.append(i)
    elif musicclip_duration in range(int(1251), int(1299)): #5.5 Adjustable
        long_clips.append(i)
    elif musicclip_duration in range(int(5.25), int(1250)): # Adjustable
        medium_clips.append(i)
    elif musicclip_duration in range(int(1.0), int(5.24)): # Adjustable
        short_clips.append(i)
    else:
        pass
    
        

def print_clips_list():
    Lg.logger.info('For ' + Tm.my_time + ', ' + 'the list of short clips is:   ' + str(short_clips))
    Lg.logger.info('=================================================================================================================')
    Lg.logger.info('For ' + Tm.my_time + ', ' + 'the list of medium clips is:   ' + str(medium_clips))
    Lg.logger.info('=================================================================================================================')
    Lg.logger.info('For ' + Tm.my_time + ', ' + 'the list of long clips is:   ' + str(long_clips))
    Lg.logger.info('=================================================================================================================')
    Lg.logger.info('For ' + Tm.my_time + ', ' + 'the list of extra long clips is:   ' + str(extra_long_clips))
    Lg.logger.info('=================================================================================================================')
   

#This from Stack Overflow(https://stackoverflow.com/questions/66802318/dividing-audio-clips-using-python)
    #Will split an audio file to desired duration in seconds. Use variable my_duration.
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# 
# count = 1
# my_duration = 400 #in seconds, duration of final audio clip
# src_duration = 980 #in seconds, the duration of the original audio
# for i in range(0, src_duration, my_duration):
#     ffmpeg_extract_subclip( my_music_path + '/Various artists - Dream Melodies Vol.  2 - Classical Symphonies/Beethoven- Marcia funebre, from Symphony No. 3 in E flat, \'\'Eroica\'\'.mp3',
#                             i, i + 300,  targetname= my_music_path + '/Various artists - Dream Melodies Vol.  2 - Classical Symphonies/Beethoven- Marcia funebre, from Symphony No. 3 in E flat, \'\'Eroica\'\'_min.mp3')
#     count += 1



                          
                  
# Selections by Genre
# To select a single clip, select one from above and paste it below and uncomment
# all_tracks = [my_path + '']


# global all_clips
# Uncomment to Select Clips from All Sources
# all_tracks =   #  select music_clips add as needed for other clips

#  Uncomment to Select Winston Rhodes Music Only
# all_tracks = winston_rhodes

# Uncomment to select classical clips only
# all_tracks = classical_clips

#Select a specified list? Just copy and paste the selection(s) from the above sets into the select_clips set.

                   



'''
This script randomly selects a track from the list called by the mandala maker,
and removes directory path and extension from clip, leaving the file name only

'''
all_earth_tones = glob.glob(f'/home/sels/Music/Audio Clips for Python/All_clips/*.mp3')
bell_format_tones = glob.glob(f'/home/sels/Music/Audio Clips for Python/Bell_format/*.mp3')
# for i in all_earth_tones:
#     get_music_file_duration()

# special_track = '/home/sels/Music/Audio Clips for Python/All_clips/105.6-528-633.6 Hz FifthHarmonics-fade-60m.mp3' #/home/sels/Music/Audio Clips for Python/All_clips/240-360-480 Hz ThirdHarmonics-fade-60m.mp3' 
# special_track = '/home/sels/Music/Audio Clips for Python/All_clips/Sacral-210.42-288-417 Hz-6sec-60min.mp3'
special_track = '/home/sels/Music/Audio Clips for Python/All_clips/172.8,259.2,432,691.2 Hz.mp3'

suffix = '.mp3'
suffix_a = '.flac'

def pick_earth_tone_track():
    global my_audio_clip
    global my_track
#     my_audio_clip = special_track
    my_audio_clip = random.choice(all_earth_tones)
    Lg.logger.info(f'Audio_Clips:The selected track is {my_audio_clip}')
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 6)
    if len(clipped_track) > 0:
        this_track = clipped_track[6]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    return my_track
    Lg.logger.info(f'Audio_Clips:The selected track is {my_track}')
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    Lg.logger.info(f'Audio_Clips:For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
    print(f'Audio_Clips:For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
# pick_earth_tone_track()

def pick_special_track():
    global my_audio_clip
    global my_track
#     my_audio_clip = special_track
    my_audio_clip = special_track
    Lg.logger.info(f'The selected track is {my_audio_clip}')
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 6)
    if len(clipped_track) > 0:
        this_track = clipped_track[6]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    return my_track
    Lg.logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    Lg.logger.info(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
    print(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
# pick_special_track()


def pick_bell_format_track():
    global my_audio_clip
    global my_track
#     my_audio_clip = special_track
    my_audio_clip = random.choice(bell_format_tones)
    Lg.logger.info(f'Audio_Clips:The selected track is {my_audio_clip}')
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 6)
    if len(clipped_track) > 0:
        this_track = clipped_track[6]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    return my_track
    Lg.logger.info(f'Audio_Clips:The selected track is {my_track}')
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    Lg.logger.info(f'Audio_Clips:For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
    print(f'Audio_Clips:For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
# pick_bell_format_track()


def pick_medium_track():
    global my_audio_clip
    global my_track
    my_audio_clip = random.choice(medium_clips)
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 6)
    if len(clipped_track) > 0:
        this_track = clipped_track[6]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    return my_track
    Lg.logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    Lg.logger.info(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
    print(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
# pick_medium_track()

def pick_long_track():
    global my_audio_clip
    global my_track
    my_audio_clip = random.choice(long_clips) #extended_clips or long_clips
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 6)
    if len(clipped_track) > 0:
        this_track = clipped_track[6]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    return my_track
    print(str(my_track))
    Lg.logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    Lg.logger.info(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
    print(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
# pick_long_track()
# Lg.logger.info(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
# print(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
# print(str(my_track))    

def pick_short_track():
    global my_audio_clip
    global my_track
    my_audio_clip = random.choice(short_clips) #extended_clips or long_clips
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 6)
    if len(clipped_track) > 0:
        this_track = clipped_track[6]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    return my_track
    Lg.logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    Lg.logger.info(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
    print(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
# pick_short_track()



def pick_x_long_track():
    global my_audio_clip
    global my_track
    my_audio_clip = random.choice(solfeggio_extra_long_tracks)
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 6)
    if len(clipped_track) > 0:
        this_track = clipped_track[6]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    return my_track
    Lg.logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    Lg.logger.info(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
    print(f'For {my_track}, the duration of this music clip is {musicclip_duration} minutes')
# pick_x_long_track()


def get_special_track():
    my_special_track = '/home/sels/Music/Audio Clips for Python/FiveChakraTones-321-432-528-639-852 Hz.mp3'  #/home/sels/Music/Audio Clips for Python/352, 704, 1408 Hz Thymus Chakra Harmonic Frequency Tones.mp3'  # my_music_path + '/Meditation - Music and Nature/Night Visions.mp3'  # 7  minutes my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Crossing To The Other Side.mp3'  # 4 minutes
    global my_audio_clip
    global my_track
    my_audio_clip = my_special_track #Include full path
#     ch = '/'
#     clipped_track = my_audio_clip.split(ch, 5)
#     if len(clipped_track) > 0:
#         this_track = clipped_track[5]
#     if suffix in this_track:
#         my_track = this_track.removesuffix(suffix)
#     else:
#         my_track = this_track.removesuffix(suffix_a)
    

#my_music_path + '/Earth Tones/194.18-388.36-1165.08-earthtones-6secbellx180.mp3'
#  Use this to manually select a single track, of any length or genre




# my_track = [my_music_path + '/Solfeggio Tones/Solfeggio_174_bell.mp3', # Pain Reduction
#                            my_music_path + '/Solfeggio Tones/Solfeggio_417_bell.mp3', # Change
#                            my_music_path + '/Solfeggio Tones/Solfeggio_741_bell.mp3']

# my_angle = [int(174), int(417), int(714)]

# matched = list(zip(my_track, my_angle))
# print(str(matched))

# print_clips_list()

# import random
# 
# # def random_music_clip(music_list):
#   """
#   This function randomly selects a music clip from a list and returns it.
# 
#   Args:
#     music_list: The list of music clips to choose from.
# 
#   Returns:
#     The randomly selected music clip.
#   """

#   # Get the number of music clips in the list.
#   num_music_clips = len(music_list)
# 
#   # Select a random index from 0 to the number of music clips - 1.
#   random_index = random.randint(0, num_music_clips - 1)
# 
#   # Return the music clip at the selected index.
#   return music_list[random_index]
# 
# ['song1.mp3', 'song2.mp3', 'song3.mp3']
# music_clip = random_music_clip(music_list)
# 
# # Play the music clip.
# subprocess.Popen(['mpg123', music_clip])
# 
# 
# import random
# 
# def random_music_clip(music_list):
#   """
#   This function randomly selects a music clip from a list and returns it.
# 
#   Args:
#     music_list: A list of music clips.
# 
#   Returns:
#     The randomly selected music clip.
#   """
# 
#   # Get the number of music clips in the list.
#   num_music_clips = len(music_list)
# 
#   # Select a random index from 0 to num_music_clips - 1.
#   random_index = random.randint(0, num_music_clips - 1)
# 
#   # Return the music clip at the selected index.
#   return music_list[random_index]
# 
# music_clip = random_music_clip(music_list)
# for i in range(10):
#   music_clip = random_music_clip(music_list)
# 
# 



#Work on some more
# selected_set = solfeggio_fade_tones_3
# def get_indexed_track():
#     my_indexed_track = selected_set[i]
#     global my_audio_clip
#     global my_track
#     my_audio_clip = my_indexed_track #Include full path
#     ch = '/'
#     clipped_track = my_audio_clip.split(ch, 5)
#     if len(clipped_track) > 0:
#         this_track = clipped_track[5]
#     if suffix in this_track:
#         my_track = this_track.removesuffix(suffix)
#     else:
#         my_track = this_track.removesuffix(suffix_a)
#     return my_track
#     Lg.logger.info('The selected track is ' + str(my_track))
#     Audio_length = MP3(my_audio_clip)
#     musicclip_duration = round(int(Audio_length.info.length/60))
#     Lg.logger.info(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
#     print(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))




# Lg.logger.info('Contents of long_clips list are   ' + str(long_clips))
# Lg.logger.info('Contents of regular_clips list are   ' + str(extended_clips))
# Lg.logger.info('Contents of short_clips list are   ' + str(short_clips))






# audioclip = AudioFileClip(my_audio_clip)
# Lg.logger.info(str(audioclip.duration))
# # new_clip = audioclip.set_duration(400)
# # Lg.logger.info(str(new_clip.duration))
# list = long_clips
# # Getting length of list using len() function
# length = len(list)
# i = 0

# while i < length:
#     Lg.logger.info(list[i])
#     i += 1

# METHOD 2 from Geeksforgeeks.com
# Lg.logger.infos list of files with duration to shell


#     import os
#     path_of_the_directory = my_path + '/Lengthy Audio/'
#     object = os.scandir(path_of_the_directory)
#     Lg.logger.info("Files and Directories in '% s':" % path_of_the_directory)
#     for n in object :
#         if n.is_dir() or n.is_file():
#             Lg.logger.info(n.name)
#             get_duration()
#            
#     object.close()
#Split audio clips
# 
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# 
# count = 1
# duration_of_clip = 300 #in seconds, duration of final audio clip
# src_duration = 600 #in seconds, the duration of the original audio
# for i in range(0, src_duration, duration_of_clip):
#     ffmpeg_extract_subclip("src_audio.wav", i, i + 3,
#                         targetname=f'results/audio_clip_{count}.wav')
#     count += 1

# Strip Audio from MP4 Clip
'''
# initialize the variables for audio and video files
mp4_file ="Video.mp4"#video file name
mp3_file="audio.mp3"#create new audio file    
    
#  VideoFileClip(path) function from the moviepy library read the video file (.mp4)   
videoclip = VideoFileClip(mp4_file)

# Now convert the video into audio (.mp3) file
audioclip = videoclip.audio

audioclip.write_audiofile(mp3_file)

audioclip.close()
videoclip.close()


# Get Video Duration

import moviepy.editor

# Converts into more readable format
def convert(seconds):
    hours = seconds / 3600
    seconds % = 3600

    mins = seconds / 60
    seconds %= 60

    return hours, mins, seconds


# Create an object by passing the location as a string
video = moviepy.editor.VideoFileClip("D:\path\to\video.mp4")

# Contains the duration of the video in terms of seconds
video_duration = int(video.duration)

hours, mins, secs = convert(video_duration)

print("Hours:", hours)
print("Minutes:", mins)
print("Seconds:", secs)
'''


