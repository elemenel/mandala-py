# import os
# import subprocess
# 
# def trim_mp3_files(directory):
#     """Trims all MP3 files in the given directory to 3 minutes."""
# 
#     for root, _, files in os.walk(directory):
#         for filename in files:
#             if filename.endswith(".mp3"):
#                 file_path = os.path.join(root, filename)
#                 try:
#                     duration = get_mp3_duration(file_path)
#                     if duration > 180:  # Check if longer than 3 minutes
#                         start_time = 0
#                         end_time = 180
#                         trim_command = f"ffmpeg -i {file_path} -ss {start_time} -to {end_time} -c copy trimmed_{filename}"
#                         subprocess.run(trim_command, shell=True, check=True)
#                         print(f"Trimmed {filename} to 3 minutes.")
#                     else:
#                         print(f"Skipping {filename} as it's already 3 minutes or shorter.")
#                 except subprocess.CalledProcessError as e:
#                     print(f"Error trimming {filename}: {e}")
#                 except ValueError:
#                     print(f"Error determining duration of {filename}")
# 
# def get_mp3_duration(file_path):
#     """Gets the duration of an MP3 file in seconds."""
# 
#     probe_command = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {file_path}"
#     output = subprocess.check_output(probe_command, shell=True)
#     return float(output)
# 
# # if __name__ == "__main__":
# #     directory = "/home/sels/Music/Audio Clips for Python/All_clips/"  # Replace with the actual directory path
# #     trim_mp3_files(directory)


'*********************************************************************************************************************************************************************'

# 
# import os
# from pydub import AudioSegment
# import ffmpeg
# 
# def trim_mp3s(input_dir, output_dir):
#     """Trims MP3 files in the input directory to 3 minutes and saves them to the output directory."""
#     input_dir = "/home/sels/Music/Audio Clips for Python/All_clips/"
#     output_dir = "/home/sels/Music/Audio Clips for Python/three_min_for_usb/"
#     os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
# 
#     for filename in os.listdir(input_dir):
#         if filename.endswith(".mp3"):
#             full_input_path = os.path.join(input_dir, filename)
#             full_output_path = os.path.join(output_dir, filename)
# 
#             try:
#                 # Load the MP3 file
#                 sound = AudioSegment.from_mp3(full_input_path)
# 
#                 # Trim to 3 minutes (180 seconds)
#                 trimmed_sound = sound[:180000]  # 180 seconds * 1000 milliseconds/second
# 
#                 # Save the trimmed file
#                 trimmed_sound.export(full_output_path, format="mp3")
# 
#                 print(f"Trimmed {filename} and saved to {output_dir}")
# 
#             except Exception as e:
#                 print(f"Error processing {filename}: {e}")
# # 
# # Example usage:
# input_dir = "/home/sels/Music/Audio Clips for Python/All_clips/"
# output_dir = "/home/sels/Music/Audio Clips for Python/three_min_for_usb/"
# trim_mp3s(input_dir, output_dir)

'''
**Explanation:**

1. **Import necessary libraries:**
   - `os` for working with file paths and directories.
   - `pydub` for audio manipulation.

2. **Define the `trim_mp3s` function:**
   - Takes two arguments: `input_dir` (the directory containing the MP3 files) and `output_dir` (the directory to store the trimmed files).
   - Creates the output directory if it doesn't exist using `os.makedirs()`.
   - Iterates through the files in the input directory.
   - Checks if the file has the ".mp3" extension.
   - Constructs the full input and output paths using `os.path.join()`.
   - Loads the MP3 file using `AudioSegment.from_mp3()`.
   - Trims the audio to 3 minutes (180 seconds) using slicing.
   - Saves the trimmed audio to the output directory using `export()`.
   - Prints a success message.
   - Handles any potential errors using a `try-except` block.

3. **Example usage:**
   - Sets the `input_directory` and `output_directory` variables to the desired paths.
   - Calls the `trim_mp3s` function to perform the trimming.
'''




from pydub import AudioSegment

import ffprobe

# Open an mp3 file 
song = AudioSegment.from_file("/home/sels/Music/Audio Clips for Python/24Min/432_base.mp3") #, format="mp3") 
audioclip = AudioFileClip(song)
new_audioclip = audioclip.set_duration(audioclip.duration - 21000)
new_audioclip = ("/home/sels/Music/Audio Clips for Python/24Min/first_three_minutes.mp3", format="mp3")
# pydub does things in milliseconds 
three_minutes = 180 * 1000
  
# song clip of 10 seconds from starting 
first_three_minutes = song[:three_minutes] 
  
# save file 
first_three_minutes.export("/home/sels/Music/Audio Clips for Python/24Min/first_three_minutes.mp3", format="mp3")
new_audioclip.
print("New Audio file is created and saved") 