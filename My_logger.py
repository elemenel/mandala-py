import logging
import sys
import datetime

#Assign correct system path for cross-platform capability

if sys.platform.startswith('linux'):
    my_home_dir = '/home/sels/'
    my_work_dir = '/home/sels/Modules/MandalaMaker/'
    my_log_dir = '/home/sels/Modules/MandalaMaker/Logs/'
    my_video_path = '/home/sels/Videos/'
    no_audio_vids = '/home/sels/Videos/no_audio/'
    my_full_vids = '/home/sels/Videos/Full_Vids/'
    my_audio_path = '/home/sels/Music/Audio Clips for Python/'
    my_git_path = '/home/sels/Git/elemenel/'
    my_mandala_pics_path = '/media/sels/My_Media/Videos/Pictures/Mandala Final Thumbs/'
    my_thumbs = '/home/sels/Thumbs/'
    final_thumbs = '/home/sels/Pictures/Final Thumbs/'
    my_shared_drive = f'/home/sels/sambashare/Logs/my_filename_{datetime.datetime.now()}.log'
    
    my_backup_drive = '/media/sels/Backup/'
    my_audio_backup_folder = '/media/sels/Backup/AudioClipsPython/'
    concatenate_candidates = '/home/sels/Videos/concatenate_candidates/'
    do_concatenate_folder = '/home/sels/Videos/do_concatenate/'
    my_filename = f'/home/sels/Modules/MandalaMaker/Logs/my_filename_{datetime.datetime.now()}.log'
else:
    my_work_dir = 'D:/'
    no_audio_vids = 'D:/'
    my_full_vids = 'D:/Videos/Full_Vids/'
    my_audio_path = 'D:/Music/Audio Clips for Python/'
    my_git_path = 'D:/Git/'
    my_home_dir = 'C:/'
    my_log_dir = 'D:/Logs/'
    my_video_path = '/D:/Videos/'
    no_audio_vids = 'D:/Videos/no_audio/'
    my_mandala_pics_path = 'D:/Pictures/Mandala Final Thumbs/'
    my_thumbs = 'D:/Pictures/Thumbs/'
    my_shared_drive = 'Y:/sambashare/'
    my_filename = 'D:\MandalaMaker Modules\MandalaMaker\MandalaMaker\Logs/my_filename.log'
        
global my_project
my_project = 'My Project'

# Universal Logger
global logger
global formatter, fileHandler, consoleHandler
logger = logging.getLogger(my_project) # Initialize global logger

fileHandler = logging.FileHandler(my_filename)
fileHandler = logging.FileHandler(my_shared_drive)
fileHandler.setLevel(logging.INFO)
fileHandler.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.setLevel(logging.INFO)
logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

logger.info(f'Logger has been initialized')
    
