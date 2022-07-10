# mandala-py
READ.ME
Master Mandala Maker created and maintained by Leon R Hatton.

Cross-platform capability for Linux and Windows 10. Scripted in Python 3.10, tested and executed using Thonny IDE version 3.2.7 and higher.
The primary python module used is Turtle, created by Wally Feurzeig, Seymour Papert and Cynthia Solomon in 1967.

Master_Mandala_Maker creates mp4 formatted videos from screenshots of images. Containing over 30 unique scripts, it is dependent on seven additional local modules:
t.my_angles.py,  -- outputs angle; 
Timer.py,  -- holds time and timer functions; 
my_splash_screen.py,  -- generates watermark on mandala, title screens, splash screens, end screens; 
my_hues.py, -- outputs custom shades and randomized hues of a given color range; 
File_Scripts.py, -- source of file manipulation and audio, visual and final a/v processing; 
My_template.py, -- provides template for mandala using the Turtle module, and 
audio_clips.py  -- Holds links to audio tracks on local machine.New users have to specify the path to their local audio tracks.
 
Also requires the pip installs of:
open cv-python, 
numpy, 
pyautogui, 
moviepy with ipython notebook, and 
natsort. 
This code first sets up the file environment, then selects an angle as a base template for the mandala.
The code then initiates the video-making process. With each loop of code, .png images are saved. The looped collection of pngs is then sorted sequentially
and processed into an audio-less video track.  The audio track is then added and synced to the video track completing the video creation process. Finally a jpeg image is created after the final loop.  It is stored in a subfolder of the default Pictures folder. So the mandala script outputs both  a video and a full
image for each mandala created.
 ---On 6/22/2022: Successfully added cross-platform capability for Windows 10 and Linux Mint 20. Also upgraded to Python 3.10.5 on both systems to take advantage of the new 'prefixremove' and 'suffixremove' function to better handle renaming the audio files.
     
