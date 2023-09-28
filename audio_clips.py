'''audio_clips.py organizes all audio services, including file links to audio clips,
sorting and grouping clips based on varied parameters, for use in the master_mandala_maker. py and the FileScripts.py modules.
by Leon Hatton
'''
import sys
import random
import os
import platform
from moviepy.editor import *
from moviepy.editor import AudioFileClip, ImageClip, VideoFileClip
from functools import lru_cache
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
import Timer as Tm
# import My_logger as l
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
#     logger.info('The duration of  ' + str(i) +' is:  ' + str(musicclip_duration) + '  minutes')
#     logger.info('=================================================================================================')
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
    logger.info('For ' + Tm.my_time + ', ' + 'the list of short clips is:   ' + str(short_clips))
    logger.info('=================================================================================================================')
    logger.info('For ' + Tm.my_time + ', ' + 'the list of medium clips is:   ' + str(medium_clips))
    logger.info('=================================================================================================================')
    logger.info('For ' + Tm.my_time + ', ' + 'the list of long clips is:   ' + str(long_clips))
    logger.info('=================================================================================================================')
    logger.info('For ' + Tm.my_time + ', ' + 'the list of extra long clips is:   ' + str(extra_long_clips))
    logger.info('=================================================================================================================')
   
# strauss_clips = [my_music_path + '/Gerard Schwarz - Strauss Also Sprach Zarathustra; Salome/Four Symphonic Interludes (from Intermizzo).mp3', # 24  minutes
#                my_music_path + '/Gerard Schwarz - Strauss Also Sprach Zarathustra; Salome/Dance of the Seven Veils.mp3',  # 10  minutes
#                 [my_music_path + '/Gerard Schwarz - Strauss Also Sprach Zarathustra; Salome/Also Sprach Zarathustra, Op. 30.mp3'] # 36  minutes
# for i in strauss_clips: 
#     get_music_file_duration()

                                                                                             

solfeggio_6min_solo_tones = [my_music_path + '/Solfeggio Tones/963 Hz-fadebell-6sec-60x-stereo.mp3',
                            my_music_path + '/Solfeggio Tones/852 Hz-fadebell-6sec-60x-stereo.mp3',
                            my_music_path + '/Solfeggio Tones/741Hz-fadebell-6sec-60x-stereo.mp3',
                            my_music_path + '/Solfeggio Tones/639 Hz-fadebell-6sec-60x-stereo.mp3',
                            my_music_path + '/Solfeggio Tones/528 Hz-fadebell-6sec-60x-stereo.mp3',
                            my_music_path + '/Solfeggio Tones/432 Hz-fadebell-6sec-60x-stereo.mp3',
                            my_music_path + '/Solfeggio Tones/417Hz-fadebell-6sec-60x-stereo.mp3',
                            my_music_path + '/Solfeggio Tones/396Hz-fadebell--6sec-60x-stereo.mp3',
                            my_music_path + '/Solfeggio Tones/285hz-bell-6sec60x-stereo.mp3',
                            my_music_path + '/Solfeggio Tones/174hz-bell-6sec60x.mp3']
# for i in solfeggio_6min_solo_tones:
#     get_music_file_duration()


earth_tones = [my_music_path + '/Earth Tones/432r-864-1728 Hz-6sec-8min.mp3',
#                         my_music_path + '/Earth Tones/D Project-Throat Chakra Tones-141.27, 282.54, 565.08, 1130.16-24min.mp3',
                        my_music_path + '/Earth Tones/D Project-Throat Chakra Tones-141.27, 282.54, 565.08, 1130.16-36min.mp3',
#                         my_music_path + '/Earth Tones/F Project- Crown Chakra Tones-172.06, 344.12, 688.24, 1376.48-24min.mp3',
                        my_music_path + '/Earth Tones/F Project- Crown Chakra Tones-172.06, 344.12, 688.24, 1376.48-36min.mp3',
                        my_music_path + '/Earth Tones/126.22-378.66-1009.76 Hz-18min.mp3',
                        my_music_path + '/Earth Tones/136.1_272.2-_408.3-FadeBell-12min.mp3',
#                         my_music_path + '/Earth Tones/136.1-FadeBell-12min.mp3',
                        my_music_path + '/Earth Tones/161.82-323.63-647.27-1294.54 Hz-E freq-15min.mp3',
                        my_music_path + '/Earth Tones/192.43-384.87-769.74-1539.47 Hz-G freq-15min.mp3',
                        my_music_path + '/Earth Tones/194.18-388.36-1165.08-earthtones-18min.mp3',
#                         my_music_path + '/Earth Tones/216-432-864-1728 Hz-A freq-10min.mp3',
#                         my_music_path + '/Earth Tones/417r-1251-2085 Harmonic 3rd and 5th Frequencies-6min.mp3',
                        my_music_path + '/Earth Tones/C# Project-136.1, 272.2, 544.4, 1088.8, 2177.6, 4355.2, 8710.4 Hz-24min.mp3',
#                         my_music_path + '/Earth Tones/272.2-FadeBell-12 min.mp3',
#                         my_music_path + '/Earth Tones/396Hz-fadebell-36min.mp3',
#                         my_music_path + '/Earth Tones/396Hz-fadebell-18min.mp3',
#                         my_music_path + '/Earth Tones/408.3-FadeBell-12 min.mp3',
#                         my_music_path + '/Earth Tones/417Hz-fadebell-36min.mp3',
#                         my_music_path + '/Earth Tones/417Hz-fadebell-18min.mp3',
#                         my_music_path + '/Earth Tones/432 Hz-fadebell-36min.mp3',
#                         my_music_path + '/Earth Tones/528 Hz-fadebell-18min.mp3',
#                         my_music_path + '/Earth Tones/639 Hz-fadebell-18min.mp3',
                        my_music_path + '/Earth Tones/86.4-432-1080-2160 Hz.mp3',
                        my_music_path + '/Earth Tones/352, 704, 1408 Hz Thymus Chakra.mp3',
#                         my_music_path + '/Earth Tones/352 Hz Thymus Chakra Tone.mp3',
                        my_music_path + '/Earth Tones/417-1251-2085 Harmonic 3rd and 5th.mp3',
#                         my_music_path + '/Earth Tones/432 Hz-fadebell-18min.mp3',
#                         my_music_path + '/Earth Tones/741Hz-fadebell-18min.mp3',
#                         my_music_path + '/Earth Tones/852 Hz-fadebell-18min.mp3',
#                         my_music_path + '/Earth Tones/963 Hz-fadebell-18min.mp3',
                        my_music_path + '/Earth Tones/528-633.6-422.4-316.8 Hz Earth Tones-12min.mp3',
                        my_music_path + '/CustomTones/528-1584-4752 Harmonic Tones-60min.mp3',
                        my_music_path + '/CustomTones/264-528-1056-2112 Hz Harmonic Tones-60min.mp3',
                        my_music_path + '/CustomTones/164-328-656 Hz Harmonic Tones-60min.mp3',
                        my_music_path + '/CustomTones/528 Hz 60min.mp3',
                        my_music_path + '/CustomTones/432 Hz 60min.mp3',
                         my_music_path + '/CustomTones/216, 432, 1296 Hz 60min steady.mp3',
#                         my_music_path + '/CustomTones/264-528-1584 Hz 60min steady.mp3',
                        my_music_path + '/Seven Chakra Tones/FiveChakraTones-321-432-528-639-852 Hz.mp3']

for i in earth_tones:
    get_music_file_duration()



solfeggio_tones = [my_music_path +'/Solfeggio Tones/23p49 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/126.22-378.66-1009.76 Hz-6secfade-x180.mp3',
                    my_music_path +'/Solfeggio Tones/136.1_272.2-_408.3-FadeBell-6sec-120x.mp3',
                    my_music_path +'/Solfeggio Tones/852 Hz-bell-6sec120x.mp3',
                    my_music_path +'/Solfeggio Tones/852 Hz-fadebell-6sec-60x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/963 Hz-bell-6sec120x.mp3',
                    my_music_path +'/Solfeggio Tones/963 Hz-fadebell-6sec-60x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/136.1_272.2-_408.3-FadeBell-6sec-120x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/136.1-FadeBell-6sec-120x-stereo.mp3',
#                     my_music_path +'/Solfeggio Tones/174-fade-out-.3amp-9secx33.mp3',
#                     my_music_path +'/Solfeggio Tones/174hz-bell-6sec60x.mp3',
                    my_music_path +'/Solfeggio Tones/174hz-bell-6sec-120x.mp3',
                    my_music_path +'/Solfeggio Tones/194.18-388.36-1165.08-earthtones-6secbellx180.mp3',
                    my_music_path +'/Solfeggio Tones/272.2-FadeBell-6sec-120x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/285 and 396 hz-bell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/285hz-bell-6sec60x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/285 Hz-bell-6sec120x.mp3',
                    my_music_path +'/Solfeggio Tones/396 and 528 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/396 and 639 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/396 and 741 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/396 and 963 Hz-FadeBell-7.83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/396 Hz-bell-6sec120x.mp3',
#                     my_music_path +'/Solfeggio Tones/396Hz-fadebell--6sec-60x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/408.3-FadeBell-6sec-120x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/417-1251-2085 Harmonic 3rd and 5th Frequencies.mp3',
#                     my_music_path +'/Solfeggio Tones/417 and 639 Hz-FadeBell-7.83sec-42x.mp3',
#                     my_music_path +'/Solfeggio Tones/417 and 741 Hz-FadeBell-7p83sec-42x.mp3',
#                     my_music_path +'/Solfeggio Tones/417 and 852 Hz-FadeBell-7p83sec-42x.mp3',
#                     my_music_path +'/Solfeggio Tones/417 and 963 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/417 Hz-bell-6sec120x.mp3',
#                     my_music_path +'/Solfeggio Tones/417Hz-fadebell-6sec-60x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/417r-1251-2085 Harmonic 3rd and 5th Frequencies6min.mp3',
                    my_music_path +'/Solfeggio Tones/432 and 528 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/432 Hz-fadebell-6sec-60x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/432r-864-1728 Hz-6sec-8min.mp3',
                    my_music_path +'/Solfeggio Tones/528 and 741 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/528 and 852 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/528 Hz-bell-6sec120x.mp3',
                    my_music_path +'/Solfeggio Tones/528 Hz-fadebell-6sec-60x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/639 and 852 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/639 and 963 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/639 Hz-bell-6sec120x.mp3',
                    my_music_path +'/Solfeggio Tones/639 Hz-fadebell-6sec-60x-stereo.mp3',
                    my_music_path +'/Solfeggio Tones/741 and 963 Hz-FadeBell-7p83sec-42x.mp3',
                    my_music_path +'/Solfeggio Tones/741 Hz-bell-6sec120x.mp3',
                    my_music_path +'/Solfeggio Tones/741Hz-fadebell-6sec-60x-stereo.mp3']
for i in solfeggio_tones:
    get_music_file_duration()


solfeggio_misc = [my_music_path + '/Solfeggio Tones/194.18-388.36-1165.08-earthtones-6secbellx180.mp3',
                    my_music_path + '/Solfeggio Tones/417r-1251-2085 Harmonic 3rd and 5th Frequencies6min.mp3',
                    my_music_path + '/Solfeggio Tones/126.22-378.66-1009.76 Hz-6secfade-x180.mp3',
                    my_music_path + '/Solfeggio Tones/432r-864-1728 Hz-6sec-8min.mp3',
                    my_music_path + '/Solfeggio Tones/417-1251-2085 Harmonic 3rd and 5th Frequencies.mp3']
# for i in solfeggio_misc:
#     get_music_file_duration()


#     get_music_file_duration()


   
chakra_tones =     [my_music_path + '/Seven Chakra Tones/FiveChakraTones-321-432-528-639-852 Hz.mp3',
                             my_music_path +'/Seven Chakra Tones/352, 704, 1408 Hz Thymus Chakra Harmonic Frequency Tones.mp3',
                            my_music_path + '/Seven Chakra Tones/352 Hz Thymus Chakra Frequency Tone.mp3',
                            my_music_path + '/Seven Chakra Tones/352 Hz Thymus Chakra Primary - 1056 Hz and 1769 Hz Harmonic 3rd and 5th Frequency Tone.mp3',
                            my_music_path + '/Seven Chakra Tones/396-1188-1980 Hz Solfeggio Harmonic 3rd and 5thTones-36min.mp3',
                            my_music_path + '/Seven Chakra Tones/417-1251-2085 Hz Solfeggio 3rd and 5th Harmonic Frequency Tones-36min.mp3',
                            my_music_path + '/Seven Chakra Tones/Ajna_221p23 Hz.mp3',
                            my_music_path + '/Seven Chakra Tones/Anahata_136p10 Hz.mp3',
                            my_music_path + '/Seven Chakra Tones/A Project- Seat of Soul  - Svadisthana Chakra Tones-210.42 Hz,420.84 Hz, 841.68 Hz, 1683.36 Hz -x120.mp3',
                            my_music_path + '/Seven Chakra Tones/A Project- Third Eye Chakra Tones-221.23, 442.46, 884.92, 1769.84-x120.mp3',
                            my_music_path + '/Seven Chakra Tones/A Project- Third Eye Chakra Tones-221.23, 442.46, 884.92-120x.mp3',
                            my_music_path + '/Seven Chakra Tones/Brow-221.23-448-852 Hz-6sec-60min.mp3',
                            my_music_path + '/Seven Chakra Tones/C# Project( 136.1, 272.2, 544.4, 1088.8, 2177.6, 4355.2, 8710.4) Hz Stereo @ 6sec x 120.mp3',
                            my_music_path + '/Seven Chakra Tones/C# Project( 136.1, 272.2, 544.4, 1088.8, 2177.6, 4355.2, 8710.4) Hz Stereo @ 6sec x 240-24min.mp3',
                            my_music_path + '/Seven Chakra Tones/C Project- Solar Plexus Chakra Tones-126.22, 252.44, 504.88, 1009.76-x120.mp3',
                            my_music_path + '/Seven Chakra Tones/Crown-172.06-480-963 Hz-6sec-60min.mp3',
                            my_music_path + '/Seven Chakra Tones/Crown Chakra Harmonic FifthsTones.mp3',
                            my_music_path + '/Seven Chakra Tones/D Project-Throat Chakra Tones-141.27, 282.54, 565.08, 1130.16-24min.mp3',
                            my_music_path + '/Seven Chakra Tones/F Project- Crown Chakra Tones-172.06, 344.12, 688.24, 1376.48-24min.mp3',
                            my_music_path + '/Seven Chakra Tones/G Project- Base of Spine Chakra Tones-194.18, 388.36, 776.72 Hz-x120.mp3',
                            my_music_path + '/Seven Chakra Tones/Heart-Thymus 128.43-385.29-642.15 Hz-6secbell-36min.mp3',
                            my_music_path + '/Seven Chakra Tones/Heart-Thymus 136.10-341.3-639 Hz-6sec-36min.mp3',
                            my_music_path + '/Seven Chakra Tones/Manipura_126p22 Hz.mp3',
                            my_music_path + '/Seven Chakra Tones/Muladhara_194p18 Hz.mp3',
                            my_music_path + '/Seven Chakra Tones/Root-194.18-256-396 Hz-6sec-60min.mp3',
                            my_music_path + '/Seven Chakra Tones/Sacral-210.42-288-417 Hz-6sec-60min.mp3',
                            my_music_path + '/Seven Chakra Tones/Sahasrar_172.06 Hz.mp3',
                            my_music_path + '/Seven Chakra Tones/Solar-126.22-320-528 Hz-6sec-60min.mp3',
                            my_music_path + '/Seven Chakra Tones/Svadisthana_210p42 Hz.mp3',
                            my_music_path + '/Seven Chakra Tones/Throat - 141.27, 384, 741 Hz- 6sec-36min.mp3',
                            my_music_path + '/Seven Chakra Tones/Throat - 144.16, 432.48, 720.8 Hz-6sec-36min.mp3',
                            my_music_path + '/Seven Chakra Tones/Thymus-128.43-382-642.15-1027.44 Hz-6sec-60min.mp3',
                            my_music_path + '/Seven Chakra Tones/Vishudda141p27 Hz.mp3']
for i in chakra_tones:
    get_music_file_duration()
    

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
suffix = '.mp3'
suffix_a = '.flac'

def pick_custom_length_track():
    global my_audio_clip
    global my_track
    my_audio_clip = random.choice(custom_length_clips)
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 6)
    if len(clipped_track) > 0:
        this_track = clipped_track[6]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    return my_track
    logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    logger.info(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
    print(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
# pick_custom_length_track()

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
    logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    logger.info(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
    print(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
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
    logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    logger.info(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
    print(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
# pick_long_track()
# logger.info(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
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
    logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    logger.info(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
    print(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
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
    logger.info('The selected track is ' + str(my_track))
    Audio_length = MP3(my_audio_clip)
    musicclip_duration = round(int(Audio_length.info.length/60))
    logger.info(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
    print(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
# pick_x_long_track()


def get_special_track():
    my_special_track = '/home/sels/Music/Audio Clips for Python/Seven Chakra Tones/FiveChakraTones-321-432-528-639-852 Hz.mp3'  #/home/sels/Music/Audio Clips for Python/352, 704, 1408 Hz Thymus Chakra Harmonic Frequency Tones.mp3'  # my_music_path + '/Meditation - Music and Nature/Night Visions.mp3'  # 7  minutes my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Crossing To The Other Side.mp3'  # 4 minutes
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
#     logger.info('The selected track is ' + str(my_track))
#     Audio_length = MP3(my_audio_clip)
#     musicclip_duration = round(int(Audio_length.info.length/60))
#     logger.info(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
#     print(str('For ' + str(my_track) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))




# logger.info('Contents of long_clips list are   ' + str(long_clips))
# logger.info('Contents of regular_clips list are   ' + str(extended_clips))
# logger.info('Contents of short_clips list are   ' + str(short_clips))






# audioclip = AudioFileClip(my_audio_clip)
# logger.info(str(audioclip.duration))
# # new_clip = audioclip.set_duration(400)
# # logger.info(str(new_clip.duration))
# list = long_clips
# # Getting length of list using len() function
# length = len(list)
# i = 0

# while i < length:
#     logger.info(list[i])
#     i += 1

# METHOD 2 from Geeksforgeeks.com
# logger.infos list of files with duration to shell


#     import os
#     path_of_the_directory = my_path + '/Lengthy Audio/'
#     object = os.scandir(path_of_the_directory)
#     logger.info("Files and Directories in '% s':" % path_of_the_directory)
#     for n in object :
#         if n.is_dir() or n.is_file():
#             logger.info(n.name)
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

