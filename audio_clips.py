# Music Clips for merging to video and other projects

import random
import os
import platform
from moviepy.editor import *
import audio_clips as au
from moviepy.editor import AudioFileClip, ImageClip
from functools import lru_cache

global my_path, my_music_path
my_path = '/media/elemen/Inland SSD1'
my_music_path = '/home/elemen/Music'

# music_clips  ---Music list

kenya_rhodes = [my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - The Trial.mp3',
                my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Strange Food.mp3',
                my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Women Of Wonder.mp3',
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Turn.mp3',
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Pass Me Not.mp3',
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Waiting on You.mp3',
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - Under Me.mp3',
               my_music_path +'/Kenya Rhodes - Pass Me Not/Kenya Rhodes - When I Get To Heaven.mp3']

winston_rhodes = [my_music_path + '/Winston Rhodes - Jubilee/On A Heavenly Journey.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/I Never Knew.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/Thank God I\'m Forgiven.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/Heading to Zion.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/Trav\'lin On The Tracks Of Life.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/Life\'s Storms.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/Yes I\'m Still Here Lord.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/Jubilee.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/On The Hallelujah Trail.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/His Majesty, God.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/Music Still Blowing In The Wind.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/A Rasta Man\'s Prayer.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/Spread Your Tender Mercy Over me.mp3',
                my_music_path + '/Winston Rhodes - Jubilee/Drink From The Living Water.mp3']

spa_style = [my_music_path + '/Spa Style - Refresh/At Peace.mp3',
                my_music_path + '/Spa Style - Refresh/Song of the Angels.mp3',
                my_music_path + '/Spa Style - Refresh/Reverie.mp3',
                my_music_path + '/Spa Style - Refresh/On the Water.mp3',
                my_music_path + '/Spa Style - Refresh/In Paradise.mp3',
                my_music_path + '/Spa Style - Refresh/Like a Swan.mp3']

marvin_gaye = [my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - God Is Love.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - What\'s Happening Brother.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Wholy Holy.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Mercy Mercy Me (The Ecology).mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Flyin\' High (In the Friendly Sky).mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - What\'s Going On.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Save the Children.mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Inner City Blues (Make Me Wanna Holler).mp3',
                my_music_path + '/Marvin Gaye - What\'s Going On/Marvin Gaye - Right On.mp3']

meditation_music = [my_music_path + '/Meditation - Music and Nature/Water Pearls.mp3',
                    my_music_path + '/Meditation - Music and Nature/Morning.mp3',
                    my_music_path + '/Meditation - Music and Nature/Nature Awakening.mp3',
                    my_music_path + '/Meditation - Music and Nature/Evening Song.mp3',
                    my_music_path + '/Meditation - Music and Nature/Morning Prelude.mp3',
                    my_music_path + '/Meditation - Music and Nature/River Of Life.mp3',
                    my_music_path + '/Meditation - Music and Nature/Moonlight Shadows.mp3',
                    my_music_path + '/Meditation - Music and Nature/Thunder and Rain.mp3',
                    my_music_path + '/Meditation - Music and Nature/05 - unknown artist - Silent River Landscape.mp3',
                    my_music_path + '/Meditation - Music and Nature/Sparkling Water.mp3',
                    my_music_path + '/Meditation - Music and Nature/Low Tide - Silent Paradise.mp3',
                    my_music_path + '/Meditation - Music and Nature/Silent Walk.mp3',
                    my_music_path + '/Meditation - Music and Nature/Daybreak- Sunrise.mp3',
                    my_music_path + '/Meditation - Music and Nature/Night Visions.mp3']


peter_tosh = [my_music_path + '/Peter Tosh - Super Hits/Why Must I Cry.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Burial.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Brand New Second Hand.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/African.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Get Up, Stand Up.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Whatcha Gonna Do.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Equal Rights.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Stepping Razor.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Downpressor Man.mp3',
                    my_music_path + '/Peter Tosh - Super Hits/Legalize It.mp3']


classical_clips =  [my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Tchaikovsky - Romeo and Juliet Fantasy Overture.mp3',
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Mozart - Romanze from Eine Kleine Nachtmusik.mp3',
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Bach - Air from Suite No. 3 in D.mp3',
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Holst - Venus (Bringer of Peace) from the Planets.mp3',
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Beethoven - Adagio Sostenuto Moonlight Sonata.mp3',
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Debussy - Clair de Lune.mp3',
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Borodin - Polovetsian Dance No. 2 from Prince Igor.mp3',
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Rimsky-Korsakov - Scheherazade.mp3',
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Pachelbel - Canon in D.mp3',
                    my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/Grieg - Morning Mood from Peer Gynt Suite.mp3']

yanni_clips = [my_music_path + '/Yanni - Tribute/Yanni - Nightingale.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Waltz In 7\'8.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Southern Exposure.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Love Is All.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Prelude.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Tribute.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Dance With A Stranger.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Renegade.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Adagio In C Minor.mp3',
                    my_music_path + '/Yanni - Tribute/Yanni - Deliverance.mp3']


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

india_arie = [my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - This Too Shall Pass.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - I Choose.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - (Outro) Learning.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Better People.mp3',
                my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/India.Arie - Great Grandmother.mp3',
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


all_tracks = india_arie #+ stevie_wonder + yanni_clips + classical_clips + peter_tosh + spa_style + kenya_rhodes + winston_rhodes +  marvin_gaye + meditation_music            


def pick_track():
    global my_audio_clip
    global my_track
# Confirm existence of all clips in the all_tracks list
    my_audio_clip = random.choice(all_tracks)
    prefix = my_music_path +'/Kenya Rhodes - Pass Me Not/'
    prefix_a = my_music_path + '/Winston Rhodes - Jubilee/' 
    prefix_b = my_music_path + '/Spa Style - Refresh/'
    prefix_c = my_music_path + '/Marvin Gaye - What\'s Going On/'
    prefix_d = my_music_path + '/Meditation - Music and Nature/'
    prefix_e = my_music_path + '/Peter Tosh - Super Hits/'
    prefix_f = my_music_path + '/Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/'
    prefix_g = my_music_path + '/Yanni - Tribute/'
    prefix_h = my_music_path + '/Stevie Wonder - A Time To Love/'
    prefix_i = my_music_path + '/India.Arie - Testimony - Vol. 1, Life & Relationship/'
       
    suffix = '.mp3'
    
    
    if suffix  and prefix in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix) #.mp3
        my_track = this_track.removeprefix(prefix) #  ''/Kenya Rhodes - Pass Me Not/'
        print(this_track)
        print(my_track)

    elif suffix  and prefix_a in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix)#.mp3
        my_track = this_track.removeprefix(prefix_a) # '/Winston Rhodes - Jubilee/'
        print(this_track)
        print(my_track)

    elif suffix  and prefix_b in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix)#.mp3
        my_track = this_track.removeprefix(prefix_b)  #'/Spa Style - Refresh/Spa Style -/
        print(this_track)
        print(my_track)

    elif suffix  and prefix_c in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix)#.mp3
        my_track = this_track.removeprefix(prefix_c) # '/Marvin Gaye - What\'s Going On/'
        print(this_track)
        print(my_track)
        
    elif suffix and prefix_e in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix)#.mp3
        my_track = this_track.removeprefix(prefix_e) # '/Peter Tosh - Super Hits/'
        print(this_track)
        print(my_track)
        
    elif suffix and prefix_f in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix)#.mp3
        my_track = this_track.removeprefix(prefix_f) # 'Various artists - Relaxing with the Classics (London Symphony Orchestra, Don Jackson)/'
        print(this_track)
        print(my_track)
        
    elif suffix and prefix_g in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix)#.mp3
        my_track = this_track.removeprefix(prefix_g) # '/Yanni - Tribute/'
        print(this_track)
        print(my_track)
        
    elif suffix and prefix_h in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix)#.mp3
        my_track = this_track.removeprefix(prefix_h) # '/Stevie Wonder - A Time To Love/'
        print(this_track)
        print(my_track)
        
        
    elif suffix and prefix_i in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix)#.mp3
        my_track = this_track.removeprefix(prefix_i) # '/India.Arie - Testimony - Vol. 1, Life & Relationship/'
        print(this_track)
        print(my_track)     
        
        
    else:
        this_track = my_audio_clip.removesuffix(suffix)  #.mp3
        my_track = this_track.removeprefix(prefix_d)  #'/Meditation - Music and Nature/'
        print(this_track)
        print(my_track)
   
#  Test to confirm audio path
# pick_track()
# print(prefix_g)




# print(my_audio_clip)
# print(my_track)

# audioclip = AudioFileClip(my_audio_clip)
# # print(str(audioclip.duration))
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
def file_duration():
    import audioread

    # function to convert the information into
    # some readable format
    def duration_detector(length):
        hours = length // 3600 # calculate in hours
        length %= 3600
        mins = length // 60 # calculate in minutes
        length %= 60
        seconds = length # calculate in seconds

        return hours, mins, seconds


    def get_duration():
        # f is the fileobject being created
        with audioread.audio_open(n) as f:
            # totalsec contains the length in float
            totalsec = f.duration
            hours, mins, seconds = duration_detector(int(totalsec))
            print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))

#     import os
#     path_of_the_directory = my_path + '/Lengthy Audio/'
#     object = os.scandir(path_of_the_directory)
#     print("Files and Directories in '% s':" % path_of_the_directory)
#     for n in object :
#         if n.is_dir() or n.is_file():
#             print(n.name)
#             get_duration()
#             print('====================================')
#     object.close()

# file_duration()
