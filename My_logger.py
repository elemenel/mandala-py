import logging





#     formatter = logging.Formatter( '%(asctime)s  |  %(name)s%; (levelname)s:  |  %(message)s  |',   datefmt='%m/%d/%Y %I:%M:%S%p')
#     consoleHandler.setFormatter(formatter)
#     fileHandler.setFormatter(formatter)


my_filename = '/home/sels/Modules/MandalaMaker/Logs/t.my_filename.log'
my_project = 'My Project'

# Universal Logger
global logger
global formatter, fileHandler, consoleHandler
logger = logging.getLogger(my_project) # Initialize global logger
fileHandler = logging.FileHandler(my_filename)
fileHandler.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
logger.setLevel(logging.INFO)
logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)
#     formatter = logging.Formatter( '%(asctime)s  |  %(name)s%; (levelname)s:  |  %(message)s  |',   datefmt='%m/%d/%Y %I:%M:%S%p')
#     consoleHandler.setFormatter(formatter)
#     fileHandler.setFormatter(formatter)

def startup_script():
    global my_filename
    global logger
    global formatter, fileHandler, consoleHandler, my_project
    my_filename = f.my_work_dir + '/MandalaMaker/Logs/' + my_project + '_' + t.my_key +  '.log'
   
    logger = logging.getLogger(my_project)
    fileHandler = logging.FileHandler(my_filename)
    fileHandler.setLevel(logging.INFO)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    logger.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)
#     formatter = logging.Formatter( '%(asctime)s  |  %(name)s%; (levelname)s:  |  %(message)s  |',   datefmt='%m/%d/%Y %I:%M:%S%p')
#     consoleHandler.setFormatter(formatter)
#     fileHandler.setFormatter(formatter)
    logger.info('Starting  ' + my_project)
    logger.info('This is ' + my_project + ' code')

def make_folder():
    logger.info('Setting up directories and files for video production')
    t.my_angle = a.i_angle_auto[a.i]
    t.my_str = my_project + '    featuring   ' + str( t.my_angle) + '    Degree Angles,   with   '  + str(au.my_track)
    t.my_mandala_name = my_project + '_' + str(t.my_angle) + '_' + str(au.my_track)
    logger.info('Folder name is   ' + str(t.my_mandala_name))
    f.make_png_folder()
    os.chdir(f.loc_thumb + t.my_mandala_name)
    turtle.title(t.my_str)
    logger.info('Presenting  ' + t.my_str)


def stage_video():
    f.save_final_thumb()
    logger.info(' Starting video creation....')
    turtle.setup(5,5)
    f.set_vid_env()
    logger.info('Starting merger of video and audio clips....')
    f.sync_av()
    logger.info('Making of mandala completed.')
    logger.info('Stopping  ' + t.my_str + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('****************************************************************************')
    reset_all()
    
    
    

def finalize():
    logger.info('************************************************************************')
    logger.info('Stopping ' + my_project + ' by Leon Hatton on  ' + str(Tm.my_time))
    logger.info('Finalizing scripts to sync all files and folders')
    logger.info('Minimizing turtle screen to observe screen and read shell output')
    turtle.setup(5,5) # Minimized turtle window to observe screen and read shell output
    logger.info('Moving files to appropriate folders')
    f.move_all() # Moves files to appropriate locations
    logger.info('Video .mp4 files have been moved to /Videos/')
    logger.info('Image .png files have been moved to /Thumbs/Output/')
    logger.info('Image .jpg files have been moved to /home/elemen/Pictures/Mandala Final Thumbs/')
    logger.info('Pics have been moved to Pictures folder')
    logger.info('================================================================================')
    f.sync_mandala_folders()  # Sync video and script folders backups
    logger.info('Folders and files have been synced and backed up')
    logger.warning('Shutting down this module and resetting logger')
    logger.handlers.clear()
    reset_all()

