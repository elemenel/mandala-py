"""Custom_Video_Processing.py"""

import moviepy.editor as mp
from moviepy.editor import *
from moviepy.editor import (
    AudioFileClip,
    ImageClip,
    VideoFileClip,
    concatenate_videoclips,
)
from moviepy.video.io.VideoFileClip import VideoFileClip
import time
import Timer as Tm
import My_logger as Lg
import shutil as sh
import os
import glob
import random

global new_fps

# Assign correct system path for cross-platform capability
# global my_work_dir
if sys.platform.startswith("linux"):
    my_home_dir = "/home/sels/"
    my_work_dir = "/home/sels/Modules/MandalaMaker/"
    my_log_dir = "/home/sels/Modules/MandalaMaker/Logs/"
    my_video_path = "/home/sels/Videos/"
    my_no_audio_video_path = f"{my_video_path}/no_audio"
    my_full_vids_video_path = f"{my_video_path}Full_Vids"
    my_audio_path = "/home/sels/Music/Audio Clips for Python/"
    my_git_path = "/home/sels/Git/"
    my_mandala_pics_path = "/media/sels/My_Media/Videos/Pictures/Mandala Final Thumbs/"
    my_thumbs_path = "/home/sels/Thumbs/"
    my_server_folder = my_home_dir + "Videos/Full_Vids/"
    my_final_thumbs_path = "/home/sels/Pictures/Final Thumbs/"
    my_shared_drive = "/home/sels/sambashare/"
    concatenate_directory = "/home/sels/Videos/do_concatenate"
    concatenated_directory = "/home/sels/Videos/concatenated/"

else:
    my_work_dir = "D:/"
    my_no_audio_video_path = "D:/"
    my_full_vids_video_path = "D:/"
    my_audio_path = "D:/"
    my_git_path = "D:/"
    my_home_dir = "C:/"






def clear_do_concatenate_files():
    import os
    import glob
    

    # specify the directory you want to delete from
    directory = "/home/sels/Videos/do_concatenate/"

    # use glob to match the pattern '*.mp4'
    files = glob.glob(os.path.join(directory, "*.mp4"))

    # use a loop to delete each file
    for file in files:
        try:
            os.remove(file)
            #             print(f"Deleted {file}")
            Lg.logger.info(f"Deleted {file}")
        except OSError as e:
            print(f"Error: {e.strerror} - {e.filename}.")
            Lg.logger.info(f"Error: {e.strerror} - {e.filename}.")
    Lg.logger.info(
        "All files in the concatenate_directory have been deleted, and the directory is ready for new content"
    )


# clear_do_concatenate_files()







# Use to concatenate two videos
def concatenate_my_videos():
    print(f"Starting concatenate_my_videos")
    Lg.logger.info(f"Starting concatenate_my_videos")
    # Paths to the two video files
    clip1 = VideoFileClip(
        "/home/sels/Videos/Full_Vids/(1)3278 degrees-Sirius Mandala-432 bell-155.52, 259.2, 648, 972 Hz-240434143.mp4"
    )
    clip2 = VideoFileClip(
        "/home/sels/Videos/Full_Vids/(1)3278 degrees-Gradiant Mandala-172.8,259.2,432,691.2 Hz-240433740.mp4"
    )
    clip3 = VideoFileClip(
        "/home/sels/Videos/Full_Vids/(1)3278 degrees-Durable Mandala-417_bell-83.4-667.2-1000.8 Hz FifthHarmonics-240432519.mp4"
    )
    clip4 = VideoFileClip(
        "/home/sels/Videos/Full_Vids/(1)3278 degrees-Influence_Mandala-432 bell-155.52, 259.2, 648, 972 Hz-240434016.mp4"
    )
    clip5 = VideoFileClip(
        "/home/sels/Videos/Full_Vids/(1)3278 degrees-Resonance Mandala-852_bell-170.4-1022.4-1363.2 Hz FifthHarmonics-240431046.mp4"
    )
    clip6 = VideoFileClip(
        "/home/sels/Videos/Full_Vids/(1)3278 degrees-Intense Mandala-396_bell-79.4-633.6-950.4 Hz FifthHarmonics-240435618.mp4"
    )
    clip7 = VideoFileClip(
        "/home/sels/Videos/Full_Vids/(1)3278 degrees-Brave Mandala-852_bell-170.4-1022.4-1363.2 Hz FifthHarmonics-240432937.mp4"
    )
    clip8 = VideoFileClip(
        "/home/sels/Videos/Full_Vids/(1)3278 degrees-Prosper_Mandala-417_bell-83.4-667.2-1000.8 Hz FifthHarmonics-240430902.mp4"
    )
    clip9 = VideoFileClip(
        "/home/sels/Videos/Full_Vids/(1)3278 degrees-Effective Mandala-396_bell-79.4-633.6-950.4 Hz FifthHarmonics-240434200.mp4"
    )
#     clip2 = VideoFileClip(
#         "/media/sels/Productions/Videos/no_audio/Breathing Yin-Yang angles with 264-528-1056-2112 Hz Harmonic Tones-60min-232293914.mp4"
#     )
    # Merge the two files together using concatenation
    final_clip = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9])
    # Write and save the new file to desired location
    final_clip.write_videofile(
        "/home/sels/Videos/Mixing Folder/Nine Expressions of 3278 Degrees.mp4"
    )
    print(f"Completed concatentate_my_videos")
    Lg.logger.info(f"Completed concatenate_my_videos")


# concatenate_my_videos()

"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
# Use to concatenate all videos in a directory


def concatenate_videos(concatenate_folder, concatenated_video):
    import os
    import subprocess
   
    concatenate_folder = '/home/sels/Videos/do_concatenate/'
    concatenated_video = '/home/sels/Videos/concatenated/output.mp4'
#     video_files = [f for f in os.listdir(concatenate_folder) if f.endswith(".mp4")]
       # Sort files by filename (assuming numerical order)
    video_files = sorted(os.listdir("."), key=os.path.getctime)
    Lg.logger.info("Sorting completed, starting file merge...")
    # Get all .mp4 files in the directory
    video_files = [os.path.join(concatenate_folder, f) for f in os.listdir(concatenate_folder) if f.endswith(".mp4")]

 
    with open("files.txt", "w") as file_list:
        for file in video_files:
            file_list.write(f"file '{os.path.join(concatenate_folder, file)}'\n")
    subprocess.call(
        f"ffmpeg  -y -f concat -safe 0 -i files.txt -c copy {concatenated_video}",
        shell=True,
    )
    os.remove("files.txt")
    clear_do_concatenate_files()
    Lg.logger.info(f"Concatenation process completed!")
   
    
    


concatenate_videos('/home/sels/Videos/do_concatenate/', '/home/sels/Videos/concatenated/output.mp4') #'/home/sels/Videos/do_concatenate/',  '/home/sels/Videos/concatenated/output.mp4')
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
#  https://www.geeksforgeeks.org/moviepy-assigning-audio-clip-to-video-file/
# Used by Master Mandala maker to generate videos with sound by merging audio clips to video clips
def add_av():
    video_file_name = "/home/sels/Videos/concatenated/output.mp4"
    audio_clip = "/home/sels/Music/Audio Clips for Python/All_clips/528, 1584, 176, 52.8 Hz Steady-60min.mp3"
    composite_video_file_name = "/home/sels/Videos/concatenated/Seven Various Mandalas featuring 1215 Degrees Angles with 528 Hz and Harmonic Tones.mp4"
#     av_start_time = timer()
    Tm.set_time()
    Lg.logger.info(f"Custom_Video_Processing:Starting sync_av() @ {Tm.this_time}")
    Lg.logger.info(f"Custom_Video_Processing:Merging Video with Audio...")
    os.chdir(my_video_path)
    new_video = "__temp__.mp4"
    Lg.logger.info(f"Custom_Video_Processing:Folder name is {video_file_name}")
    
#     os.makedirs(f"/home/sels/Videos/do_concatenate/{t.folder_name}", exist_ok=True)
    Lg.logger.info(f"Custom_Video_Processing:File Name is {video_file_name}")
    videoclip = VideoFileClip(f"{video_file_name}")
    audioclip = AudioFileClip(f"{audio_clip}")
    audioclip = audioclip.set_duration(
        videoclip.duration + 1
    )  # Adjust the audio duration here '+6' is default
    Lg.logger.info(
        f"FileScripts:The duration of this audio clip is {audioclip.duration / 60:.2f} minutes"
    )
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(f"{composite_video_file_name}")
   
sync_av() 













def do_my_file_merge():
    

    # Define input and output directories
    input_dir = concatenate_directory
    output_file = f"{concatenated_directory}output.mp4"

    # Get all .mp4 files in the directory
    video_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".mp4")]

    # Sort files by filename (assuming numerical order)
    video_files = sorted(os.listdir("."), key=os.path.getctime)
  

    # Create a list of VideoFileClip objects
    clips = [VideoFileClip(f) for f in video_files]

    # Concatenate the clips
    final_clip = concatenate_videoclips(clips)

    # Write the final clip to the output file
    final_clip.write_videofile(output_file)

    print("Files concatenated successfully!")

# do_my_file_merge()



def do_my_file_merge_a():
    
    # Define directory and output file, but sorts accurately
    directory = concatenate_directory
    output_file = f"{concatenated_directory}merged.mp4"

    # Get all mp4 files in the directory
    video_files = [f for f in os.listdir(directory) if f.endswith(".mp4")]

    # Sort the files (assuming numeric order in filenames)
    video_files.sort()

    # Create clips and concatenate them
    clips = []
    for file in video_files:
        clip = VideoFileClip(os.path.join(directory, file))
        clips.append(clip)

    final_clip = concatenate_videoclips(clips)

    # Write the final clip to the output file
    final_clip.write_videofile(output_file)

    print("Files concatenated successfully!")

# do_my_file_merge_a()











global new_fps


def change_frame_rate():
    global new_fps
    print(f"Starting change_frame_rate")
    Lg.logger.info(f"Starting change_frame_rate")
    # Load the video clip
    clip = VideoFileClip(
        "/home/sels/Videos/Mixing Folder/Double-Breath Color-Changing Yin-Yang.mp4"
    )
    print(f"FPS = {clip.fps} fps")
    Lg.logger.info(f"FPS = {clip.fps} fps")
    # Set the desired frame rate
    new_fps = clip.fps * 5
    print(f"New FPS = {new_fps} fps")
    Lg.logger.info(f"New frame rate: {new_fps} fps")
    # Change the frame rate of the clip
    new_clip = clip.set_fps(new_fps)
    new_clip.write_videofile(
        f"/home/sels/Videos/Mixing Folder/Double-Breath Color-Changing Yin-Yang at {new_fps} .mp4"
    )
    print(f"Completed change_frame_rate")
    Lg.logger.info(f"Completed change_frame_rate")


# change_frame_rate()


# Append 1/2 of video to produce a full picture ending instead of a blank screen
def end_with_full_image():
    print(f"Starting end_with_full_image")
    Lg.logger.info(f"Starting end_with_full_image")
    # Get path of clip
    clip = VideoFileClip(
        f"/home/sels/Videos/Mixing Folder/Double-Breath Color-Changing Yin-Yang at {new_fps} .mp4"
    )
    duration = clip.duration
    print(f"Duration: {duration / 60} minutes")
    Lg.logger.info(f"Duration:  {duration/60} minutes")
    print(f"3/4 Duration: {duration /60 *.74}  minutes")
    Lg.logger.info(f"3/4 Duration:  {duration/60 * .74} minutes")
    three_quarter_clip = clip.subclip(0, clip.duration * 0.74)
    full_clip = concatenate_videoclips([clip, three_quarter_clip])
    full_clip.write_videofile(
        f"/home/sels/Videos/Mixing Folder/Double-Breath Color-Changing Yin-Yang at {new_fps} with full image .mp4"
    )
    print(f"Completed end_with_full_image")
    Lg.logger.info(f"Completed end-with_full_image")


# end_with_full_image()


# Use this to manually match a video clip to an audio clip to create a composite.
# Long Duration mp4 to be stripped of shorter audio and then mated with a longer audio
# '/home/sels/Videos/Mandalas/Mystical Mandala by Leon Hatton v.230783807 -r.48002    featuring   680.5    Degree Angles,   with   396 and 852 Hz-FadeBell-7.83sec-42x.mp4' #9.59 minutes
# '/home/sels/Videos/Mandalas/Mystical Mandala by Leon Hatton v.230775214 -r.48002    featuring   408.29999999999995    Degree Angles,   with   Solfeggio_174_bell.mp4' # 9.59 minutes
# '/home/sels/Videos/Mandalas/Mystical Mandala by Leon Hatton v.230763759 -r.48002    featuring   136.1    Degree Angles,   with   396 and 963 Hz-FadeBell-7.83sec-42x.mp4' # 9.59 minutes

#  Long Duration clips with no audio and need long audio to be added, using  make_my_movie script
# A. '/media/sels/My_Media/Videos/no_audio/Brave Mandala Extended v.230645327_308.57142699999997_528 and 852 Hz-FadeBell-7p83sec-42x.mp4' # Successfuly completed and published to YouTube on 3/17/2023
# B = '/media/sels/My_Media/Videos/no_audio/Mystical Mandala by Leon Hatton v.230783807 -r.48002_680.5_396 and 852 Hz-FadeBell-7.83sec-42x.mp4' # Composite created with # 1 on 3/20/2023
# C '/media/sels/My_Media/Videos/no_audio/Mystical Mandala by Leon Hatton v.230775214 -r.48002_408.29999999999995_Solfeggio_174_bell.mp4'
# D. '/media/sels/My_Media/Videos/no_audio/Mystical Mandala by Leon Hatton v.230763759 -r.48002_136.1_396 and 963 Hz-FadeBell-7.83sec-42x.mp4'
# 03-23-2023
# D = '/media/sels/My_Media/Videos/no_audio/Majestic Mandala Extended v.230825258_300.0_639 Hz-bell-6sec120x.mp4'
# C = '/media/sels/My_Media/Videos/no_audio/Majestic Mandala Extended v.230825413_1188.0_741 Hz-bell-6sec120x.mp4'
# A ='/media/sels/My_Media/Videos/no_audio/Majestic Mandala Extended v.230825033_792.0_417 Hz-bell-6sec120x.mp4'
# B = '/media/sels/My_Media/Videos/no_audio/Majestic Mandala Extended v.230820642_396.0_396 Hz-bell-6sec120x.mp4'
#   Y = '/media/sels/My_Media/Videos/no_audio/Joyous Mandala v.231423327-r.67128_150.0_285hz-bell-6sec60x-stereo.mp4'
# F = '/home/sels/Videos/no_audio/Awesome Mandala-(7)1124, 2248, 3372, 4496, 5620, 6744, 7868 angles-Audio-396Hz-fadebell-18min-232755617.mp4'
# FZ = "/home/sels/Videos/no_audio/(1)8080 degrees-Courage Mandala-639 and 852 Hz-FadeBell-7p83sec-42x-233241814.mp4"
Fx = '/home/sels/Videos/concatenated/Seven Various Mandalas featuring 1215 Degrees Angles with 528 Hz and Harmonic Tones.mp4'
# Long Duration Audio Clips
# all_earth_tones = glob.glob(f'/home/sels/Music/Audio Clips for Python/36Min/*.mp3')


# Randomly select an audio clip
def pick_new_audio():
    global my_new_clip, my_music_clip
    suffix = ".mp3"
    all_earth_tones = glob.glob(
        f"/home/sels/Music/Audio Clips for Python/All_clips/*.mp3"
    )
#     my_music_clip = random.choice(all_earth_tones)\
    my_music_clip = '/home/sels/Music/Audio Clips for Python/All_clips/528, 1584, 176, 52.8 Hz Steady-60min.mp3'
    ch = "/"
    clipped_track = my_music_clip.split(ch, 6)
    if len(clipped_track) > 0:
        this_track = clipped_track[6]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    my_new_clip = my_track
    return my_new_clip
    Lg.logger.info(f"The selected audio clip is {my_new_clip}")


pick_new_audio()


def make_my_movie():
    Lg.logger.info("Starting make_my_movie()......................")
    global my_video, my_audio
    my_key = str(Tm.date_time)
    pick_new_audio()
    my_title = f"Simple Mandala-462,1156 Degrees"
    my_new_title = f"{my_title}-{my_new_clip}"
    Lg.logger.info(f"my_title is: {my_new_title}")
    my_str = f"{my_new_title}-{Tm.project_time}"
    Lg.logger.info(f"my_str  is: {my_str}")
    folder_name = f"/home/sels/Videos/Special/{my_str}"
    os.makedirs(f"{folder_name}", exist_ok=True)
    Lg.logger.info(f"Folder name is: {folder_name}")
    Lg.logger.info(f"File Name is: {my_str}")
    # Paste full video path (from no_audio library)
    my_video = Fx  # C #A # B
    os.chdir(f"{folder_name}")
    new_video = "__temp__.mp4"
    videoclip = VideoFileClip(my_video)
    Lg.logger.info(f"videoclip duration is {videoclip.duration / 60:2f} minutes")
    audioclip = AudioFileClip(my_music_clip)
    audioclip = audioclip.set_duration(videoclip.duration + 6)
    Lg.logger.info(f"my_music_clip is {my_music_clip}")
    Lg.logger.info(f"my_new_clip is {my_new_clip}")
    Lg.logger.info(
        f"The duration of this audio clip is {audioclip.duration / 60:.2f} minutes"
    )
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    Lg.logger.info(
        f"new_audioclip duration is {new_audioclip.duration /60:.2f} minutes"
    )
    processed_video = f"{my_title}-{my_new_clip}.mp4"
    Lg.logger.info(f"Processed video is {processed_video}")
    videoclip.write_videofile(f"{my_full_vids_video_path}{processed_video}")
    Lg.logger.info(
        f"The duration of this new video is {videoclip.duration / 60:.2f} minutes"
    )
    Lg.logger.info(
        f"The running of this module, make_my_movie, has successfully completed @ {Tm.my_time}"
    )
    os.chdir("/home/sels/Modules/")
    time.sleep(3)
    Lg.logger.info(
        "===================================================================="
    )
# make_my_movie()


""" Future - set audio clip to match video and vice versa as needed
    clip_duration = videoclip.duration+6
    audioclip = AudioFileClip("huru.wav").set_duration(clip_duration)
    new_audioclip = CompositeAudioClip([audioclip])
    clip = clip.set_audio(new_audioclip)
    video = CompositeVideoClip([clip, txt_clip]).set_duration(clip_duration)

"""

"""This section will test the functionality of various sort function to try to speed up the sort time."""
# Use glob
import glob
import os
from PIL import Image

my_directory = "/home/sels/Thumbs/Mystical Mandala-(1)[909] degrees angles-Audio-36Min/Sacral-210.42-288-417 Hz-6sec-60min-232870811"


def sort_pngs_with_glob(directory):
    png_images = glob.glob(os.path.join(directory, ".png"))
    png_images.sort(key=os.path.getctime)
    for png_image in png_images:
        os.rename(png_image, os.path.join(directory, os.path.basename(png_image)))
    Lg.logger.info("Glob sort completed")


# sort_pngs_with_glob(my_directory)


def sort_pngs_with_pillow(directory):
    png_images = [
        os.path.join(directory, f) for f in os.listdir(directory) if f.endswith("png")
    ]
    png_images.sort(key=lambda f: os.path.getctime(f))
    for png_image in png_images:
        image = Image.open(png_image)
        image.save(png_image)
    Lg.logger.info("Directory sort with Pillow completed")


# sort_pngs_with_pillow(my_directory)


def collect_splash_screens():
    import os
    import shutil

    Lg.logger.info("Moving splash screen images to Splash Screen backup folder")
    path = "/home/sels/MandalaBackup/Modules/MandalaMaker"
    for filename in os.listdir(path):
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            origin = path
            destination = "/home/sels/MandalaBackup/Modules/SplashScreens"
            endswith_ = ".jpeg"
            [
                shutil.move(os.path.join(origin, i), os.path.join(destination, i))
                for i in os.listdir(origin)
                if i.endswith(endswith_)
            ]

    Lg.logger.info(
        f"Sync of MandalaMaker SplashScreens  folders completed successfully @ {Tm.my_time}"
    )


# collect_splash_screens()

