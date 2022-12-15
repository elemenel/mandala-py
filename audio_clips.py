# Music Clips for merging to video and other projects(audio_clips.py)
import sys
import random
import os
import platform
from moviepy.editor import *
import audio_clips as au
from moviepy.editor import AudioFileClip, ImageClip
from functools import lru_cache
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
import Timer as Tm
# from logging2 import Logger

global my_path, my_music_path, my_audio_clip
if sys.platform.startswith('linux'):
    my_path = '/media/elemen/Inland SSD1'
    my_no_audio_video_path = '/media/elemen/Inland SSD1/no_audio/'
    my_full_vids_video_path = '/media/elemen/Inland SSD1/Full_Vids/'
    my_music_path = '/home/elemen/Music'
    
else:
    my_music_path = 'A:/Music'
    my_path = 'M:'
    my_no_audio_video_path = 'M:/Videos/no_audio/'
    my_full_vids_video_path = 'M:/Videos/Full_Vids/'
    
    
print(my_music_path) 
extra_long_clips = []
long_clips = []
medium_clips = []
short_clips = []

global i
i = 0
# Tm.set_time()
# music_clips  ---Music list

def get_music_file_duration():
    print(str(Tm.my_time))
    Audio_length = MP3(i)
    musicclip_duration = round(int(Audio_length.info.length/60))
    print(str('For ' + str(i) + ',  '  +'The duration of this music clip is   ' + str(musicclip_duration) + '  minutes'))
    print('=================================================================================================')
    if musicclip_duration in range(9, 25, 1):
        extra_long_clips.append(i)
    elif musicclip_duration in range(6, 8, 1): #5.5
        long_clips.append(i)
    elif musicclip_duration in range(3, 5, 1):
        medium_clips.append(i)
    else:
        short_clips.append(i)
    print_clips_list()
        

def print_clips_list():
    print('For this run, the list of short clips is:   ' + str(short_clips))
    print('=================================================================================================================')
    print('For this run, the list of medium clips is:   ' + str(medium_clips))
    print('=================================================================================================================')
    print('For this run, the list of long clips is:   ' + str(long_clips))
    print('=================================================================================================================')
    print('For this run, the list of extra long clips is:   ' + str(extra_long_clips))
    print('=================================================================================================================')
    

strauss_clips = [my_music_path + '/Gerard Schwarz - Strauss Also Sprach Zarathustra; Salome/Four Symphonic Interludes (from Intermizzo).mp3', # 24  minutes
                my_music_path + '/Gerard Schwarz - Strauss Also Sprach Zarathustra; Salome/Dance of the Seven Veils.mp3',  # 10  minutes
                my_music_path + '/Gerard Schwarz - Strauss Also Sprach Zarathustra; Salome/Also Sprach Zarathustra, Op. 30.mp3'] # 36  minutes
# for i in strauss_clips:  # prefix_ac
#     get_music_file_duration()


classical_melodies = [my_music_path + '/Various artists - Dream Melodies Vol.  2 - Classical Symphonies/Haydn- Allegretto, from Symphony No. 100 in G, \'\'Military\'\'.mp3', # 6  minutes
                    my_music_path + '/Various artists - Dream Melodies Vol.  2 - Classical Symphonies/Mozart- Allegro, from Symphony No. 31 in D, \'\'Paris\'\'.mp3', #  7  minutes
                    my_music_path + '/Various artists - Dream Melodies Vol.  2 - Classical Symphonies/Beethoven- Allegretto, from Symphony No. 7 in A.mp3', #  9  minutes
                    my_music_path + '/Various artists - Dream Melodies Vol.  2 - Classical Symphonies/Mozart- Andante, from Symphony No. 35 in D, \'\'Haffner\'\'.mp3', #  6  minutes
                    my_music_path + '/Various artists - Dream Melodies Vol.  2 - Classical Symphonies/Beethoven- Marcia funebre, from Symphony No. 3 in E flat, \'\'Eroica\'\'.mp3', # 16 minutes
                    my_music_path + '/Various artists - Dream Melodies Vol.  2 - Classical Symphonies/Haydn- Andante, from Symphony No. 94 in G, \'\'Surprise\'\'.mp3', #  6  minutes
                    my_music_path + '/Various artists - Dream Melodies Vol.  2 - Classical Symphonies/Mozart- Molto allegro, from Symphony No. 40 in G minor.mp3'] #  7  minutes
for i in classical_melodies:  # prefix_ab
    get_music_file_duration()



new_world_symphony = [my_music_path + '/Dvorak, Antonin - Symphony No 9 From the New World/Larghetto de la serenade pour cordes mi majeur Op. 22.mp3', # 5  minutes
                        my_music_path + '/Dvorak, Antonin - Symphony No 9 From the New World/Allegro con fuoco.mp3', # 11  minutes
#                         my_music_path + '/Dvorak, Antonin - Symphony No 9 From the New World/Scherzo molto vivace.mp3',   7  minutes
                        my_music_path + '/Dvorak, Antonin - Symphony No 9 From the New World/Largo.mp3', # 12  minutes
                        my_music_path + '/Dvorak, Antonin - Symphony No 9 From the New World/Adagio allegro molto.mp3']  # 9  minutes
for i in new_world_symphony:  # prefix_aa
    get_music_file_duration()
    

tchaikovsky_clips = [my_music_path + '/Pjotr Ilyich Tchaikovsky - The Masterpiece Collection Vol. 9/Wedding Dance From \'\'Swan Lake\'\' Suite Op. 20.mp3',   # 2  minutes
                    my_music_path + '/Pjotr Ilyich Tchaikovsky - The Masterpiece Collection Vol. 9/Capriccio Italien Op. 45.mp3',  # 15  minutes
                    my_music_path + '/Pjotr Ilyich Tchaikovsky - The Masterpiece Collection Vol. 9/Waltz From \'\'The Sleeping Beauty\'\'.mp3', # 4  minutes 
                    my_music_path + '/Pjotr Ilyich Tchaikovsky - The Masterpiece Collection Vol. 9/Violin Concerto In D Major Op. 35 - Canzonetta - Adante.mp3', # 6  minutes
                    my_music_path + '/Pjotr Ilyich Tchaikovsky - The Masterpiece Collection Vol. 9/Waltz from Serenade For Strings.mp3',  # 3  minutes
                    my_music_path + '/Pjotr Ilyich Tchaikovsky - The Masterpiece Collection Vol. 9/Piano Concerto No. 1.mp3',  # 4  minutes
                    my_music_path + '/Pjotr Ilyich Tchaikovsky - The Masterpiece Collection Vol. 9/Overture 1812 Op. 49.mp3']  # 15  minutes
# for i in tchaikovsky_clips:  #  prefix_z
#     get_music_file_duration()
    
    
the_spinners = [my_music_path + '/Spinners - The Essentials/Cupid-I\'ve Loved You For A Long Time.mp3',
                my_music_path + '/Spinners - The Essentials/Working My Way Back To You-Forgive Me Girl.mp3',
                my_music_path + '/Spinners - The Essentials/The Rubberband Man.mp3',
                my_music_path + '/Spinners - The Essentials/Games People Play.mp3',
                my_music_path + '/Spinners - The Essentials/Love Don\'t Love Nobody - Pt. 1.mp3',
                my_music_path + '/Spinners - The Essentials/Then Came You - with Dionne Warwicke.mp3',
                my_music_path + '/Spinners - The Essentials/Mighty Love - Pt. 1.mp3',
                my_music_path + '/Spinners - The Essentials/Ghetto Child.mp3',
                my_music_path + '/Spinners - The Essentials/One Of A Kind (Love Affair).mp3',
                my_music_path + '/Spinners - The Essentials/Could It Be I\'m Falling In Love.mp3',
                my_music_path + '/Spinners - The Essentials/How Could I Let You Get Away.mp3',
                my_music_path + '/Spinners - The Essentials/I\'ll Be Around.mp3']
for i in the_spinners:  
    get_music_file_duration()


anthony_hamilton = [my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - I Tried.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - Chyna Black.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton, LaToiya Williams - My First Love.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - Float.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - Lucille.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - Better Days.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - Comin From Where I\'m From.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - I\'m A Mess.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - Charlene.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - Since I Seen\'t You.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - Cornbread, Fish & Collard Greens.mp3',
                    my_music_path + '/Anthony Hamiton - Comin From Where I\'m From/Anthony Hamilton - Mama Knew Love.mp3']
# for i in anthony_hamilton:  
#     get_music_file_duration()




bob_marley = [my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Go Tell It on the Mountain.mp3',  # 3  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Soon Come.mp3',  # 2  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Caution.mp3',  # 2  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - All in One.mp3',  # 3  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - 400 Years.mp3',  # 2  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Brain Washing.mp3',  # 2  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Mr. Brown.mp3',  # 3  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Stand Alone.mp3',  # 2  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - African Herbsman.mp3',  # 2  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Trenchtown Rock.mp3',  # 2  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Soul Almighty.mp3',  # 2  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Rebel\'s Hop.mp3',  # 2  minutes
                my_music_path + '/Bob Marley - Bob Marley Collection/Bob Marley - Jamming.mp3']  # 3  minutes
# for i in bob_marley:  #prefix_v
#     get_music_file_duration()



messiah_clips = [my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Chorus \'Hallelujah!\'.mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Chorus \'His yoke is easy, his burden is light\'.mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Aria \'He shall feed His flock\' (Soprano).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Recitative \'Then shall the eyes of the blind\' (Alto).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Aria \'Rejoice greatly, O daughter of Zion\' (Tenor).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Chorus \'Glory to God in the highest\'.mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Recitative \'There were shepherds abiding in the fields\' (Soprano).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Pifa (Pastoral Symphony).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Chorus \'For unto us a Child is born\'.mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Aria \'The people that walked in darkness\' (Bass).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Accompagnato \'For behold, darkness shall cover\' (Bass).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Chorus \'O thou that tellest good tidings\'.mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Aria \'O thou that tellest good tidings\' (Alto).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Recitative \'Behold, a virgin shall conceive\' (Alto).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Chorus \'And He shall purify\'.mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Aria \'But who may abide the day of His coming\' (Bass).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Accompagnato \'Thus saith the Lord of Hosts\' (Bass).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Chorus \'And the glory of the Lord shall be revealed\'.mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Aria \'Ev\'ry valley shall be exalted\' (Tenor).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Accompagnato \'Comfort ye My people\' (Tenor).mp3',
                my_music_path + '/Oratorio Society of New York - Handel\'s Messiah Highlights/Oratorio Society of New York - Symphony (Grave - Allegro moderato).mp3']
for i in messiah_clips: 
    get_music_file_duration()


soul_ballads = [my_music_path + '/Various artists - Soul Ballads/Teddy Pendergrass - You\'re My Latest, My Greatest Inspiration.mp3',
                my_music_path + '/Various artists - Soul Ballads/Al Jarreau - Let\'s Stay Together.mp3',
                my_music_path + '/Various artists - Soul Ballads/The Delfonics - La-La-Means I Love You.mp3',
                my_music_path + '/Various artists - Soul Ballads/The Stylistics - You Are Everything (Live).mp3',
                my_music_path + '/Various artists - Soul Ballads/Sam & Dave - When Something Is Wrong With My Baby.mp3',
                my_music_path + '/Various artists - Soul Ballads/Percy Sledge - Warm and Tender Love.mp3',
                my_music_path + '/Various artists - Soul Ballads/Wilson Pickett - If You Need Me.mp3',
                my_music_path + '/Various artists - Soul Ballads/Joe Tex - Hold What You\'ve Got.mp3',
                my_music_path + '/Various artists - Soul Ballads/Jerry Butler - For Your Precious Love.mp3',
                my_music_path + '/Various artists - Soul Ballads/The Platters - Only You (And You Alone).mp3']
# for i in soul_ballads:  
#     get_music_file_duration()


hits_of_80 = [my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/The Gap Band - Early In The Morning.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Lionel Richie - Love Will Conquer All.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Atlantic Starr - Circles.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Mica Paris - My One Temptation.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Vanessa Williams - The Right Stuff.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Aretha Franklin - Jump To It.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Stacy Lattisaw With Johnny Gill - Where Do We Go From Here.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Rick James - Give It To Me Baby.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/DeBarge - Rhythm Of The Night.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Quincy Jones & James Ingram - One Hundred Ways.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Jocelyn Brown - Somebody Else\'s Guy.mp3',
                my_music_path + '/Various artists - The Ultimate Jukebox Hits of the 80s - Volume 2/Evelyn \'Champagne\' King - Love Come Down.mp3']
# for i in hits_of_80: 
#     get_music_file_duration()

will_downing = [my_music_path + '/Will Downing - After Tonight/Lover\'s Melody (feat. Roy Ayers).mp3',
                my_music_path + '/Will Downing - After Tonight/God Is So Amazing.mp3',
                my_music_path + '/Will Downing - After Tonight/Fantasy (Spending Time With You).mp3',
                my_music_path + '/Will Downing - After Tonight/After Tonight.mp3',
                my_music_path + '/Will Downing - After Tonight/All I Need Is You (feat. Kirk Whalum).mp3',
                my_music_path + '/Will Downing - After Tonight/After Tonight (Between The Sheets Remix).mp3',
                my_music_path + '/Will Downing - After Tonight/You, Just Can\'t Smile It Away (feat. Kirk Whalum).mp3',
                my_music_path + '/Will Downing - After Tonight/No One Can Love You More (feat. Gerald Albright).mp3',
                my_music_path + '/Will Downing - After Tonight/Satisfy You.mp3',
                my_music_path + '/Will Downing - After Tonight/Will\'s Groove.mp3']
for i in will_downing:  #prefix_q
    get_music_file_duration()

winston_rhodes_resting = [my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Resting In The Arms Of God.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/On My Way To Heaven.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/He\'s Risen.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Freedom.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Walking In The Rain.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/As Time Goes By.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/What\'s This World Coming To.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Rescue Me.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Strolling On The Beach.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Music In The Wind.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Jah-Love Makes Me Glad.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Here, There, Everywhere.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Mellow Chimes.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Crossing To The Other Side.mp3',
                    my_music_path + '/Winston Rhodes - Resting In The Arms Of God/Return To The Motherland.mp3']
for i in winston_rhodes_resting: 
    get_music_file_duration()


gil_scott_heron = [my_music_path + '/Gil Scott-Heron - Reflections/Storm Music.mp3',
                    my_music_path + '/Gil Scott-Heron - Reflections/Grandma\'s Hands.mp3',
                    my_music_path + '/Gil Scott-Heron - Reflections/Is That Jazz.mp3',
                    my_music_path + '/Gil Scott-Heron - Reflections/Morning Thoughts.mp3',
                    my_music_path + '/Gil Scott-Heron - Reflections/Inner City Blues (Poem  The Siege Of New Orleans).mp3',
                    my_music_path + '/Gil Scott-Heron - Reflections/Gun.mp3',
                    my_music_path + '/Gil Scott-Heron - Reflections/B Movie (Intro, Poem, Song).mp3']
# for i in gil_scott_heron:  #prefix_o
#     get_music_file_duration()

alicia_keys = [my_music_path + '/Alicia Keys - As I Am/Sure looks good to me.mp3',
                my_music_path + '/Alicia Keys - As I Am/Tell you something [Nana\'s reprise].mp3',
                my_music_path + '/Alicia Keys - As I Am/Prelude to a kiss.mp3',
                my_music_path + '/Alicia Keys - As I Am/Where do we go from here.mp3',
                my_music_path + '/Alicia Keys - As I Am/I need you.mp3',
                my_music_path + '/Alicia Keys - As I Am/Teenage love affair.mp3',
                my_music_path + '/Alicia Keys - As I Am/The thing about love.mp3',
                my_music_path + '/Alicia Keys - As I Am/Wreckless love.mp3',
                my_music_path + '/Alicia Keys - As I Am/Lesson learned [Feat John Mayer].mp3',
                my_music_path + '/Alicia Keys - As I Am/Like you\'ll never see me again.mp3',
                my_music_path + '/Alicia Keys - As I Am/Superwoman.mp3',
                my_music_path + '/Alicia Keys - As I Am/Go ahead.mp3',
                my_music_path + '/Alicia Keys - As I Am/As I am [Intro].mp3']
for i in alicia_keys:  #prefix_n
    get_music_file_duration()

sense_of_serenity = [my_music_path + '/Sense of Serenity - Ocean Breezes/Water Dance.mp3',  #  3  minutes
                    my_music_path + '/Sense of Serenity - Ocean Breezes/Song Of The Seagull.mp3',  # 3  minutes
                    my_music_path + '/Sense of Serenity - Ocean Breezes/Smooth Sailing.mp3',  # 4  minutes
                    my_music_path + '/Sense of Serenity - Ocean Breezes/Silver Waves.mp3',  # 3  minutes
                    my_music_path + '/Sense of Serenity - Ocean Breezes/Sea of Dreams.mp3',  # 4  minutes
                    my_music_path + '/Sense of Serenity - Ocean Breezes/Peaceful Waters.mp3',  # 4  minutes
                    my_music_path + '/Sense of Serenity - Ocean Breezes/Moonstone Beach.mp3',   # 3  minutes
                    my_music_path + '/Sense of Serenity - Ocean Breezes/Ocean Breezes.mp3',  # 4  minutes
                    my_music_path + '/Sense of Serenity - Ocean Breezes/Eternal Tides.mp3',  #4  minutes
                    my_music_path + '/Sense of Serenity - Ocean Breezes/Cool Mist.mp3']  # 3  minutes
for i in sense_of_serenity:  #prefix_m
    get_music_file_duration()

kenya_rhodes = [my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - The Trial.mp3',  # 2  minutes
                my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Strange Food.mp3',  # 2  minutes
                my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Women Of Wonder.mp3',  # 2  minutes
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Turn.mp3',  #  3  minutes
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Pass Me Not.mp3',  # 4  minutes
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Waiting on You.mp3',  # 4  minutes
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Under Me.mp3',  # 4  minutes
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - When I Get To Heaven.mp3']  # 5  minutes
for i in kenya_rhodes:
    get_music_file_duration() #prefix
    
winston_rhodes = [my_music_path + '/Winston Rhodes - Jubilee/On A Heavenly Journey.mp3',  #  2  minutes
                my_music_path + '/Winston Rhodes - Jubilee/I Never Knew.mp3',  # 3  minutes
                my_music_path + '/Winston Rhodes - Jubilee/Thank God I\'m Forgiven.mp3',  # 3  minutes
                my_music_path + '/Winston Rhodes - Jubilee/Heading to Zion.mp3',  # 4  minutes
                my_music_path + '/Winston Rhodes - Jubilee/Trav\'lin On The Tracks Of Life.mp3',  # 4  minutes
                my_music_path + '/Winston Rhodes - Jubilee/Life\'s Storms.mp3',  # 4  minutes
                my_music_path + '/Winston Rhodes - Jubilee/Yes I\'m Still Here Lord.mp3',  # 4  minutes
                my_music_path + '/Winston Rhodes - Jubilee/Jubilee.mp3',  # 4  minutes
                my_music_path + '/Winston Rhodes - Jubilee/On The Hallelujah Trail.mp3',  # 5  minutes
                my_music_path + '/Winston Rhodes - Jubilee/His Majesty, God.mp3',  # 5  minutes
                my_music_path + '/Winston Rhodes - Jubilee/Music Still Blowing In The Wind.mp3', #  6  minutes
                my_music_path + '/Winston Rhodes - Jubilee/A Rasta Man\'s Prayer.mp3',  #  6  minutes
                my_music_path + '/Winston Rhodes - Jubilee/Spread Your Tender Mercy Over me.mp3',  # 6  minutes
                my_music_path + '/Winston Rhodes - Jubilee/Drink From The Living Water.mp3']  # 6  minutes
for i in winston_rhodes: #prefix_a
    get_music_file_duration()

    
spa_style = [my_music_path + '/Spa Style - Refresh/At Peace.mp3',  # 5  minutes
                my_music_path + '/Spa Style - Refresh/Song of the Angels.mp3',  # 1  minute
                my_music_path + '/Spa Style - Refresh/Reverie.mp3',  # 5  minutes
                my_music_path + '/Spa Style - Refresh/On the Water.mp3',  # 6  minutes
                my_music_path + '/Spa Style - Refresh/In Paradise.mp3',  # 3  minutes
                my_music_path + '/Spa Style - Refresh/Like a Swan.mp3']  # 5  minutes
for i in spa_style:
    get_music_file_duration()

marvin_gaye = [my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - God Is Love.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - What\'s Happening Brother.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Wholy Holy.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Mercy Mercy Me (The Ecology).mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Flyin\' High (In the Friendly Sky).mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - What\'s Going On.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Save the Children.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Inner City Blues (Make Me Wanna Holler).mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Right On.mp3']
for i in marvin_gaye:  #prefix_c
    get_music_file_duration()

meditation_music = [my_music_path + '/Meditation - Music and Nature/Transcend.mp3',  #  4  minutes
                    my_music_path + '/Meditation - Music and Nature/The Heart Of Reiki.mp3',  # 62  minutes
                    my_music_path + '/Meditation - Music and Nature/Northern Lights.mp3',  # 15  minutes
                    my_music_path + '/Meditation - Music and Nature/Eternal Chi.mp3',  # 10  minutes
                    my_music_path + '/Meditation - Music and Nature/Earth.mp3',  # 9  minutes
                    my_music_path + '/Meditation - Music and Nature/Sapphire Blue (Indian Head Massage).mp3',  # 60  minutes
                    my_music_path + '/Meditation - Music and Nature/Relaxation & Meditation With Music & Nature.mp3',  # 59  minutes
                    my_music_path + '/Meditation - Music and Nature/Daybreak- Sunrise.mp3',  # 7  minutes
                    
                    my_music_path + '/Meditation - Music and Nature/Water Pearls.mp3',  # 3  minutes
                    my_music_path + '/Meditation - Music and Nature/Low Tide - Silent Paradise.mp3',  # 5  minutes
                    my_music_path + '/Meditation - Music and Nature/Evening Song.mp3',  # 3  minutes
                    my_music_path + '/Meditation - Music and Nature/Silent River Landscape.mp3',  # 4  minutes
                    my_music_path + '/Meditation - Music and Nature/Sparkling Water.mp3',  #  4  minutes
                    my_music_path + '/Meditation - Music and Nature/River Of Life.mp3',  # 4  minutes
                    my_music_path + '/Meditation - Music and Nature/Morning.mp3',  # 3  minutes
                    my_music_path + '/Meditation - Music and Nature/Silent Walk.mp3',  # 5  minutes
                    my_music_path + '/Meditation - Music and Nature/Thunder and Rain.mp3',  # 4  minutes
                    my_music_path + '/Meditation - Music and Nature/Moonlight Shadows.mp3',  # 4  minutes
                    my_music_path + '/Meditation - Music and Nature/Night Visions.mp3',  # 7  minutes
                    my_music_path + '/Meditation - Music and Nature/Nature Awakening.mp3',  # 4  minutes
                    my_music_path + '/Meditation - Music and Nature/Morning Prelude.mp3']  #  4  minutes
for i in meditation_music:  #prefix_d
    get_music_file_duration()

peter_tosh = [my_music_path + '/Peter Tosh - Super Hits/Why Must I Cry.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Burial.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Brand New Second Hand.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/African.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Get Up, Stand Up.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Whatcha Gonna Do.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Equal Rights.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Stepping Razor.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Downpressor Man.mp3']
#                     my_music_path + '/Peter Tosh - Super Hits/Legalize It.mp3']
# for i in peter_tosh:  #prefix_e
#     get_music_file_duration()


classical_clips =  [my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Tchaikovsky - Romeo and Juliet Fantasy Overture.mp3', # 2  minutes
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Mozart - Romanze from Eine Kleine Nachtmusik.mp3',  # 5  minutes
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Bach - Air from Suite No. 3 in D.mp3',  # 5  minutes
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Holst - Venus (Bringer of Peace) from the Planets.mp3',  # 4  minutes
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Beethoven - Adagio Sostenuto Moonlight Sonata.mp3',  # 5  minutes
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Debussy - Clair de Lune.mp3',  # 4  minutes
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Borodin - Polovetsian Dance No. 2 from Prince Igor.mp3',  #  2  minutes
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Rimsky-Korsakov - Scheherazade.mp3',  # 2  minutes
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Pachelbel - Canon in D.mp3',  # 4  minutes
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Grieg - Morning Mood from Peer Gynt Suite.mp3']  # 4  minutes
for i in classical_clips:  #prefix_f
    get_music_file_duration()

yanni_clips = [my_music_path + '/Yanni - Tribute/Yanni - Nightingale.mp3',  #  5  minutes
                    my_music_path + '/Yanni - Tribute/Yanni - Waltz In 7\'8.mp3',  #  5  minutes
                    my_music_path + '/Yanni - Tribute/Yanni - Southern Exposure.mp3',  #  6  minutes
                    my_music_path + '/Yanni - Tribute/Yanni - Love Is All.mp3',  #  5  minutes
                    my_music_path + '/Yanni - Tribute/Yanni - Prelude.mp3',  # 2  minutes
                    my_music_path + '/Yanni - Tribute/Yanni - Tribute.mp3',  # 6  minutes
                    my_music_path + '/Yanni - Tribute/Yanni - Dance With A Stranger.mp3',  # 6  minutes
                    my_music_path + '/Yanni - Tribute/Yanni - Renegade.mp3',  # 7  minutes
                    my_music_path + '/Yanni - Tribute/Yanni - Adagio In C Minor.mp3',  # 3  minutes
                    my_music_path + '/Yanni - Tribute/Yanni - Deliverance.mp3']  # 3  minutes
for i in yanni_clips:  
    get_music_file_duration()


stevie_wonder = [my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - A Time To Love (feat. India. Arie).mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Positivity (feat. Aisha Morris).mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Can\'t Imagine Love Without You.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - So What The Fuss.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Shelter In The Rain.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - True Love.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Tell Your Heart I Love You.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Passionate Raindrops.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - My Love Is On Fire.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - How Will I Know (feat. Aisha Morris).mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Please Don\'t Hurt My Baby.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - From The Bottom Of My Heart.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Moon Blue.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Sweetest Somebody I Know.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - If Your Love Cannot Be Moved (feat. Kim Burrell).mp3']
for i in stevie_wonder: 
    get_music_file_duration()

india_arie = [my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - This Too Shall Pass.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - I Choose.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - (Outro) Learning.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Better People.mp3',
#                 my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Great Grandmother.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - I Am Not My Hair.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Summer.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Wings Of Forgiveness.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - India\'Song.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - (Interlude) Living.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - There\'s Hope.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Private Party.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Good Mourning.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - The Heart Of The Matter.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - These Eyes.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - (Intro) Loving.mp3']
for i in india_arie:  #prefix_i
    get_music_file_duration()

the_whispers = [my_music_path + '/The Whispers - Song Book Volume 1/My, My, My.mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/I Love You Babe.mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/Exhale (Shoop Shoop).mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/All In Good Time.mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/You\'re Making Me High.mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/Soon As I Get Home.mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/Can We Talk.mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/Two Occasions.mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/For The Cool In You.mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/Whip Appeal.mp3',
                my_music_path + '/The Whispers - Song Book Volume 1/Seven Whole Days.mp3']
# for i in the_whispers:  #prefix_l
#     get_music_file_duration()

roberta_flack = [my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/The First Time Ever I Saw Your Face.mp3',
                my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/Killing Me Softly With His Song.mp3',
#                 my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/Jesse.mp3',
#                 my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/Why Don\'t You Move In With Me.mp3',
#                 my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/They Call It Stormy Monday.mp3',
                my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/Feel Like Makin\' Love.mp3',
#                 my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/Some Gospel According To Matthew.mp3',
#                 my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/Sweet Georgia Brown.mp3',
#                 my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/There Is A River.mp3',
                my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/The Closer I Get To You.mp3']
# for i in roberta_flack:  #prefix_k
#     get_music_file_duration()

anita_baker = [my_music_path + '/Anita Baker - The Best of Anita Baker/It\'s Been You (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/I Apologize (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Body and Soul (radio edit).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Talk to Me (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Fairy Tales (edit).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Lead Me Into Love (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Just Because (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Good Love.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Giving You the Best That I Got (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Ain\'t No Need to Worry (single version) (with The Winans).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/No One in the World.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Same Ole Love (365 Days a Year).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/06 - Anita Baker - You Bring Me Joy.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Caught Up in the Rapture (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Sweet Love.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/No More Tears.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/You\'re the Best Thing Yet.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Angel (single version).mp3']
# for i in anita_baker:  #prefix_j
#     get_music_file_duration()

#Selections for extended modules (Greater than 4 minutes)
extended_clips = [my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Pass Me Not.mp3',
                  my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Waiting on You.mp3',
                  my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Under Me.mp3',
                  my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - When I Get To Heaven.mp3',
                  my_music_path + '/Winston Rhodes - Jubilee/Heading to Zion.mp3',
                  my_music_path + '/Winston Rhodes - Jubilee/Drink From The Living Water.mp3',
                  my_music_path + '/Spa Style - Refresh/At Peace.mp3',
                  my_music_path + '/Spa Style - Refresh/Reverie.mp3',
                  my_music_path + '/Spa Style - Refresh/On the Water.mp3',
                  my_music_path + '/Spa Style - Refresh/Like a Swan.mp3',
                  my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Save the Children.mp3',
                  my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Inner City Blues (Make Me Wanna Holler).mp3',
                  my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Right On.mp3',  
                  my_music_path + '/Meditation - Music and Nature/Nature Awakening.mp3',  
                  my_music_path + '/Meditation - Music and Nature/Morning Prelude.mp3',
                  my_music_path + '/Meditation - Music and Nature/Night Visions.mp3',
                  my_music_path + '/Peter Tosh - Super Hits/Equal Rights.mp3',
                  my_music_path + '/Peter Tosh - Super Hits/Stepping Razor.mp3',
                  my_music_path + '/Peter Tosh - Super Hits/Downpressor Man.mp3',
                  my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Mozart - Romanze from Eine Kleine Nachtmusik.mp3',
                  my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Debussy - Clair de Lune.mp3',
                  my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Pachelbel - Canon in D.mp3',
                  my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Grieg - Morning Mood from Peer Gynt Suite.mp3',
                  my_music_path + '/Yanni - Tribute/Yanni - Nightingale.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Waltz In 7\'8.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Southern Exposure.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Love Is All.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Prelude.mp3',
                  my_music_path + '/Yanni - Tribute/Yanni - Tribute.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Dance With A Stranger.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Renegade.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Deliverance.mp3',
                  my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - From The Bottom Of My Heart.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Moon Blue.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - Sweetest Somebody I Know.mp3',
                    my_music_path + '/Stevie Wonder - A Time To Love/Stevie Wonder - If Your Love Cannot Be Moved (feat. Kim Burrell).mp3',
                    my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Wings Of Forgiveness.mp3',
                   my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - India\'Song.mp3',
                    my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Good Mourning.mp3',
                   my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - The Heart Of The Matter.mp3',
                   my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - These Eyes.mp3',
                  my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - This Too Shall Pass.mp3',
                  my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/The First Time Ever I Saw Your Face.mp3',
                   my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/Killing Me Softly With His Song.mp3',
                 my_music_path + '/Roberta Flack - The Soul Of Roberta Flack In Concert/Feel Like Makin\' Love.mp3',
                 my_music_path + '/Anita Baker - The Best of Anita Baker/It\'s Been You (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/I Apologize (single version).mp3',
                 my_music_path + '/Anita Baker - The Best of Anita Baker/Fairy Tales (edit).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Lead Me Into Love (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Just Because (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Good Love.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Ain\'t No Need to Worry (single version) (with The Winans).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/No One in the World.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Same Ole Love (365 Days a Year).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/06 - Anita Baker - You Bring Me Joy.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Caught Up in the Rapture (single version).mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Sweet Love.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/No More Tears.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/You\'re the Best Thing Yet.mp3',
                my_music_path + '/Anita Baker - The Best of Anita Baker/Angel (single version).mp3']
# for i in extended_clips:
#     get_music_file_duration()  

# extended_clips.append(long_clips)
# print(extended_clips)
 

                              
                  
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

                   


suffix = '.mp3'
suffix_a = '.flac'


'''
This script removes directory path and extension from clip, leaving the file name only
'''
def pick_medium_track():
    global my_audio_clip
    global my_track
    my_audio_clip = random.choice(medium_clips)
    print(my_audio_clip)
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 5)
    print('The clipped_track value is  ' + str(clipped_track))
    if len(clipped_track) > 0:
        this_track = clipped_track[5]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    print('The selected track is ' + str(my_track))    


def pick_extended_track():
    global my_audio_clip
    global my_track
    my_audio_clip = random.choice(long_clips) #extended_clips or long_clips
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 5)
    if len(clipped_track) > 0:
        this_track = clipped_track[5]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    print(my_track)
    
def pick_short_track():
    global my_audio_clip
    global my_track
    my_audio_clip = random.choice(short_clips) #extended_clips or long_clips
    ch = '/'
    clipped_track = my_audio_clip.split(ch, 5)
    if len(clipped_track) > 0:
        this_track = clipped_track[5]
    if suffix in this_track:
        my_track = this_track.removesuffix(suffix)
    else:
        my_track = this_track.removesuffix(suffix_a)
    print('The selected track is ' + str(my_track))        
 
  


      

# print('Contents of long_clips list are   ' + str(long_clips))
# print('Contents of regular_clips list are   ' + str(regular_clips))
# print('Contents of short_clips list are   ' + str(short_clips))






# audioclip = AudioFileClip(my_audio_clip)
# print(str(audioclip.duration))
# # new_clip = audioclip.set_duration(400)
# # print(str(new_clip.duration))
# list = long_clips
# # Getting length of list using len() function
# length = len(list)
# i = 0

# while i < length:
#     print(list[i])
#     i += 1

# METHOD 2 from Geeksforgeeks.com
# Prints list of files with duration to shell


#     import os
#     path_of_the_directory = my_path + '/Lengthy Audio/'
#     object = os.scandir(path_of_the_directory)
#     print("Files and Directories in '% s':" % path_of_the_directory)
#     for n in object :
#         if n.is_dir() or n.is_file():
#             print(n.name)
#             get_duration()
#            
#     object.close()
