# mandala-py
READ.ME

Master Mandala Maker created and maintained by Leon R Hatton. Is a work-in-progress, like all bona fide coding projects.

Cross-platform capability for Linux and Windows 10. Scripted in Python 3.10, tested and executed using Thonny IDE version 4.01 and higher.
The primary python module used is Turtle, created by Wally Feurzeig, Seymour Papert and Cynthia Solomon in 1967.

Master_Mandala_Maker creates mp4 formatted videos from screenshots of images and then a randomly-selected audio clip is picked from my
personal library. Containing over 30 unique scripts, the custom python module "master_mandala_maker.py" is dependent on seven additional local modules:

 1. My_template.py(sets up environment for mandala creation using the Turtle module);
 2. my_angles.py(outputs angle);
 3. File_Scripts.py(source of file manipulation and audio, visual and final a/v processing);
 4. audio_clips.py(contains links to audio tracks on local machine and selects a random track);
 5. Timer.py (holds time and timer functions);
 6. my_hues.py(outputs custom shades and randomized hues of a given color range);
 7. my_splash_screen.py(generates watermark on mandala, title screens, splash screens, end screens)

New users will have to specify the path to their own local audio tracks.

The Thonny app includes a pip gui that can search and install any content in the pip repository. Thonny also ensures that the additional
modules from pip are installed on the correct path.
Thonny can install the following modules required to run the Master Mandala Maker.

 1. open cv-python,
 2. numpy,
 3. pyautogui,
 4. pyscreenshot,
 5. moviepy with ipython notebook
 6. natsort.

scrot is required also, but it is unavailabale in pip. Hence, it has to be installed via apt (Ubuntu).

This code first sets up the file environment, then selects an angle as a base template for the mandala. Then an audio track is randomly selected.
The code then initiates the video-making process. With each loop of code, .png images are saved. The looped collection of .pngs is then sorted sequentially
and processed into an audio-less video track.  The audio track is then added and synced to the video track completing the video creation process. Finally a jpeg image is created after the final loop.  It is stored in a subfolder of the default Pictures folder. So the mandala script outputs both  a video and a full image for each mandala created.

     
