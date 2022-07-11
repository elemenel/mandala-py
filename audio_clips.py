# Music Clips for merging to video and other projects

import random
import os
import platform
from moviepy.editor import *
import audio_clips as au
from moviepy.editor import AudioFileClip, ImageClip

my_os = platform.system()
if my_os == 'Linux':
    my_path = '/media/elemen/Garage/'
else:
    my_path = 'E:/'

# music_clips  ---Music list

classical_clips = [my_path + 'Audio Clips for Python/Classical-Waltz From The Sleeping Beauty.ogg',
                    my_path + 'Audio Clips for Python/Classical-Wedding Dance From Swan Lake.ogg',
#                     my_path + 'Audio Clips for Python/Classical-1812 Overture, op. 49.ogg',
#                    my_path + 'Audio Clips for Python/Classical-A Midsummer Night\'s Dream - Intermezzo.ogg',
                    my_path + 'Audio Clips for Python/Classical-A Midsummer Night\'s Dream - Nocturne.ogg',
                    my_path + 'Audio Clips for Python/Classical-A Midsummer Night\'s Dream - Overture.ogg',
                    my_path + 'Audio Clips for Python/Classical-A Midsummer Night\'s Dream - Scherzo.ogg',
                    my_path + 'Audio Clips for Python/Classical-A Midsummer Night\'s Dream - Wedding March.ogg',
                    my_path + 'Audio Clips for Python/Classical-Ave_Maria.mp3',
                    my_path + 'Audio Clips for Python/Classical-Beethoven 7th Symphony - Allegretto.mp3',
                    my_path + 'Audio Clips for Python/Classical-Beethoven 9th Symphony - excerpt.mp3',
                    my_path + 'Audio Clips for Python/Classical-Beethoven Symphony 7 I.mp3',
                    my_path + 'Audio Clips for Python/Classical-Beethoven Symphony 7 II.mp3',
                    my_path + 'Audio Clips for Python/Classical-Beethoven Symphony 7 III.mp3',
                    my_path + 'Audio Clips for Python/Classical-Beethoven Symphony 7 IV.mp3',
                    my_path + 'Audio Clips for Python/Classical-Bizet - L\'Arlesienne-Intermezzo.ogg',
                    my_path + 'Audio Clips for Python/Classical-Bizet - Les Toreadors, from Carmen.ogg',
                    my_path + 'Audio Clips for Python/Classical-Brahms - Cradle Song.ogg',
                    my_path + 'Audio Clips for Python/Classical-Capriccio Italien, op. 45.ogg',
                    my_path + 'Audio Clips for Python/Classical-Classical Selection-Wagner.mp3',
                    my_path + 'Audio Clips for Python/Classical-Delibes - Notturno, from Coppelia.ogg',
                    my_path + 'Audio Clips for Python/Classical-Dvorák, Budapest Strings - Humoresque no 7.ogg',
                    my_path + 'Audio Clips for Python/Classical-Edvard Grieg, Solveig\'s Song from Peer Gynt.ogg',
                    my_path + 'Audio Clips for Python/Classical-Grieg - Morning, from Peer Gynt.ogg',
                    my_path + 'Audio Clips for Python/Classical-J. STRAUSS II The Blue Danube-Waltz.ogg',
                    my_path + 'Audio Clips for Python/Classical-Jean Sibelius - Finlandia, Op. 26.mp3',
                    my_path + 'Audio Clips for Python/Classical-Jean Sibelius - Karelia Suite, Op. 11 - Alla marcia.mp3',
                    my_path + 'Audio Clips for Python/Classical-Jean Sibelius - Lemminkainen\'s Return, Op. 22, No. 4.mp3',
                    my_path + 'Audio Clips for Python/Classical-Johann Strauss II, Tales From The Vienna Woods.ogg',
                    my_path + 'Audio Clips for Python/Classical-Massenet, Budapest Philharmonic - Méditation from the opera Thaïs.ogg',
                    my_path + 'Audio Clips for Python/Classical-Mendelssohn, Wedding March, from A Midsummers Night Dream.ogg',
                    my_path + 'Audio Clips for Python/Classical-New World Symphony.mp3',
                    my_path + 'Audio Clips for Python/Classical-Ode to Joy - Cooper Cannell.mp3',
                    my_path + 'Audio Clips for Python/Classical-Offenbach, The Tales of Hoffman.ogg',
                    my_path + 'Audio Clips for Python/Classical-Overture The Hebrides - Fingal\'s Cave.ogg',
                    my_path + 'Audio Clips for Python/Classical-Rachmaninoff - Piano Concerto 2 - excerpt.mp3',
                    my_path + 'Audio Clips for Python/Classical-Richard Strauss,  Opening Fanfare - Also Sprach Zarathustra.ogg',
                    my_path + 'Audio Clips for Python/Classical-Richard Wagner - Dawn and Siegfried\'s Rhine Journey from Gotterdammerung.mp3',
                    my_path + 'Audio Clips for Python/Classical-Richard Wagner - Festival March from Tannhauser.mp3',
                    my_path + 'Audio Clips for Python/Classical-Richard Wagner - Liebestod (Love-Death) from Tristan und Isolde.mp3',
                    my_path + 'Audio Clips for Python/Classical-Richard Wagner - Overture to Rienzi.mp3',
                    my_path + 'Audio Clips for Python/Classical-Richard Wagner - Overture to The Flying Dutchmen.mp3',
                    my_path + 'Audio Clips for Python/Classical-Richard Wagner - Prelude to Act I of Die Meistersinger.mp3',
                    my_path + 'Audio Clips for Python/Classical-Richard Wagner - Prelude to Act III of Lohengrin.mp3',
                    my_path + 'Audio Clips for Python/Classical-Richard Wagner - The Ride of the Valkyries from Die Walkure.mp3',
                    my_path + 'Audio Clips for Python/Classical-Richard Wagner - Track 10.mp3',
                    my_path + 'Audio Clips for Python/Classical-Rimsky-Korsakov-Scheherazade-I.mp3',
                    my_path + 'Audio Clips for Python/Classical-Rimsky-Korsakov-Scheherazade-II.mp3',
                    my_path + 'Audio Clips for Python/Classical-Rimsky-Korsakov-Scheherazade-III.mp3',
                    my_path + 'Audio Clips for Python/Classical-Schubert, Ave Maria.ogg',
                    my_path + 'Audio Clips for Python/Classical-Smetana - The Moldau (1875).ogg',
                    my_path + 'Audio Clips for Python/Classical-Tchaikovsky - 1812 Overture, op. 49.ogg',
                    my_path + 'Audio Clips for Python/Classical-Tchaikovsky - Marche Slave, Op. 31 (1876).ogg',
                    my_path + 'Audio Clips for Python/Classical-Tchaikovsky - Piano Concerto No. 1 in B flat minor, 1st movement.ogg',
                    my_path + 'Audio Clips for Python/Classical-Tchaikovsky_Sym5_I.mp3',
                    my_path + 'Audio Clips for Python/Classical-Tchaikovsky_Sym5_II.mp3',
                    my_path + 'Audio Clips for Python/Classical-Tchaikovsky_Sym5_III.mp3',
                    my_path + 'Audio Clips for Python/Classical-Tchaikovsky_Sym5_IV.mp3',
                    my_path + 'Audio Clips for Python/Classical-Violin Concerto in D major.ogg',
                    my_path + 'Audio Clips for Python/Classical-Wagner - Entrance of the Gods.mp3',
                    my_path + 'Audio Clips for Python/Classical-Wagner - Parsifal (III) - Good Friday Music.mp3',
                    my_path + 'Audio Clips for Python/Classical-Wagner - Ride of the Valkyries.ogg',
                    my_path + 'Audio Clips for Python/Classical-Waltz From Serenade for Strings.ogg']


jubilee_clips  = [my_path + 'Audio Clips for Python/A Rasta Man\'s Prayer.ogg',
                my_path + 'Audio Clips for Python/Drink From The Living Water.ogg',
                my_path + 'Audio Clips for Python/Freedom.ogg',
                my_path + 'Audio Clips for Python/Heading To Zion.ogg',
                 my_path + 'Audio Clips for Python/His Majesty, God!.ogg',
                my_path + 'Audio Clips for Python/I Never Knew.ogg',
                my_path + 'Audio Clips for Python/\'Jubilee\'!.ogg',
                my_path + 'Audio Clips for Python/Life\'s Storms.ogg',
                my_path + 'Audio Clips for Python/Music Still Blowing In The Wind.ogg',
                my_path + 'Audio Clips for Python/On A Heavenly Journey.ogg',
                my_path + 'Audio Clips for Python/On The Hallelujah Trail.ogg',
                my_path + 'Audio Clips for Python/Spread Your Tender Mercy Over Me.ogg',
                my_path + 'Audio Clips for Python/Thank God I\'m Forgiven.ogg',
                my_path + 'Audio Clips for Python/Trav\'lin On The Tracks of Life.ogg',
                my_path + 'Audio Clips for Python/Yes I\'m Still Here Lord.ogg']





jazz_rb_clips = [my_path + 'Audio Clips for Python/The Drifters - Please Stay.ogg',
                my_path + 'Audio Clips for Python/The Drifters - This Magic Moment.ogg',
                my_path + 'Audio Clips for Python/The Drifters - Up On The Roof.ogg',
                my_path + 'Audio Clips for Python/The Drifters - There Goes My Baby.ogg',
                my_path + 'Audio Clips for Python/The Drifters - Save The Last Dance For Me.ogg',
                my_path + 'Audio Clips for Python/The Drifters - On Broadway.ogg',
                my_path + 'Audio Clips for Python/The Drifters - Under The Boardwalk.ogg',
                my_path + 'Audio Clips for Python/Fabolous - Breathe.mp3',
                my_path + 'Audio Clips for Python/Jerry Butler - Gypsy Woman.mp3',
                my_path + 'Audio Clips for Python/John Coltrane - My Favorite Things.mp3',
#                 my_path + 'Audio Clips for Python/On The Ocean.mp3 ',  
                my_path + 'Audio Clips for Python/Jennifer Hudson - Where You At.mp3',
                my_path + 'Audio Clips for Python/Downpresser Scrolls of the Prophet- Peter Tosh.mp3',
                my_path + 'Audio Clips for Python/Maxwell - Pretty Wings.mp3',   
                my_path + 'Audio Clips for Python/R. Kelly - I Believe I Can Fly.mp3',
                my_path + 'Audio Clips for Python/Pharoah Sanders - The Creator Has A Masterplan (Edit).mp3',
                my_path + 'Audio Clips for Python/Cameo - Candy.mp3',
                my_path + 'Audio Clips for Python/Marvin Gaye_What\'s Going On.mp3',    
                my_path + 'Audio Clips for Python/Jill Scott-Love_Rain_(Coffee_Shop_Mix).mp3',
                my_path + 'Audio Clips for Python/Fugees_Everything_Is_Everything.mp3',
                my_path + 'Audio Clips for Python/Sam_Cooke_-_Bring_It_On_Home_To_Me.mp3',
                my_path + 'Audio Clips for Python/The Whispers-And_The_Beat_Goes_On.mp3',
                my_path + 'Audio Clips for Python/Teena Marie_I_Need_Your_Lovin.mp3',
                my_path + 'Audio Clips for Python/Shabaka_Mr.Jackson.mp3',
                my_path + 'Audio Clips for Python/MaryJBlige-No One Will Do.mp3',
                my_path + 'Audio Clips for Python/Heart_Attack_[Explicit].mp3',
                my_path + 'Audio Clips for Python/Bottoms_Up_(feat__Nicki_Minaj).mp3',
                my_path + 'Audio Clips for Python/African_Spirit.mp3',
                my_path + 'Audio Clips for Python/Shabaka_See_Dem_A_Come.mp3',
                my_path + 'Audio Clips for Python/Shabaka_Thy_Will_Be_Done.mp3',
                my_path + 'Audio Clips for Python/African_Rock.mp3 ',  
                my_path + 'Audio Clips for Python/See Dem A Come II (Remix).mp3',
                my_path + 'Audio Clips for Python/India.Arie - Wings Of Forgiveness.mp3',
                my_path + 'Audio Clips for Python/Shabaka - Thy Will Be Done.mp3']  
    
    
    
    
          

tribal_winds = [my_path + 'Audio Clips for Python/Joseph Fire Crow - Creator\'s Prayer.ogg',
                my_path + 'Audio Clips for Python/Tom Mauchahty-Ware - Circle of Life.ogg',
                my_path + 'Audio Clips for Python/William Gutierrez - Song for Grandfather.ogg',
                my_path + 'Audio Clips for Python/R. Carlos Nakai & William Eaton - Covenants Shared.ogg',
                my_path + 'Audio Clips for Python/Fernando Cellicion - Eagle Dance Song.ogg',
                my_path + 'Audio Clips for Python/Kevin Locke - Lakota Prayer.ogg',
                my_path + 'Audio Clips for Python/Andrew Vasquez - Eagle\'s Journey.ogg',
                my_path +  'Audio Clips for Python/Kevin Locke - Medicine of the Meadowlark.ogg',
                my_path + 'Audio Clips for Python/Bryan Akipa - First Flute Song.ogg',
                my_path + 'Audio Clips for Python/Andrew Vasquez - Memory of Earth Mother.ogg',
                my_path + 'Audio Clips for Python/Wind In My Mind.ogg',
                my_path + 'Audio Clips for Python/First Flight.ogg',
                my_path + 'Audio Clips for Python/Along the River.ogg',
                my_path + 'Audio Clips for Python/Memory of Earth Mother.ogg',
                my_path + 'Audio Clips for Python/First Flute.ogg',
                my_path + 'Audio Clips for Python/Medicine of the Meadowlark.ogg',
                my_path + 'Audio Clips for Python/Eagle\'s Journey.ogg',
                my_path + 'Audio Clips for Python/Lakota Prayer.ogg',
                my_path + 'Audio Clips for Python/Eagle Dance Song.ogg',
                my_path + 'Audio Clips for Python/Covenants Shared.ogg',
                my_path + 'Audio Clips for Python/Song For Grandfather.ogg',
                my_path + 'Audio Clips for Python/Circle of Life.ogg',
                my_path + 'Audio Clips for Python/Creator\'s Prayer.ogg',
                my_path + 'Audio Clips for Python/Sacred Spirit - Chants and Dances of the Native American  - .mp3'] 
    
    
select_clips = [my_path + 'Audio Clips for Python/Classical-Overture The Hebrides - Fingal\'s Cave.ogg',
                my_path + 'Audio Clips for Python/Classical-Richard Wagner - Prelude to Act III of Lohengrin.mp3',
                my_path + 'Audio Clips for Python/Classical-Richard Wagner - Dawn and Siegfried\'s Rhine Journey from Gotterdammerung.mp3',
                my_path + 'Audio Clips for Python/Classical-Richard Wagner - Festival March from Tannhauser.mp3',
                my_path + 'Audio Clips for Python/Classical-Richard Wagner - Liebestod (Love-Death) from Tristan und Isolde.mp3',
                my_path + 'Audio Clips for Python/Classical-Richard Wagner - Overture to Rienzi.mp3',
                my_path + 'Audio Clips for Python/Classical-Richard Wagner - Overture to The Flying Dutchmen.mp3',
                my_path + 'Audio Clips for Python/Downpresser Scrolls of the Prophet- Peter Tosh.mp3',
                my_path + 'Audio Clips for Python/I Never Knew.ogg',
                my_path + 'Audio Clips for Python/Classical-Beethoven Symphony 7 III.mp3',
                my_path + 'Audio Clips for Python/India.Arie - Wings Of Forgiveness.mp3',
                my_path + 'Audio Clips for Python/Drink From The Living Water.ogg',
                my_path + 'Audio Clips for Python/Classical-Richard Wagner - Track 10.mp3',
                my_path + 'Audio Clips for Python/Freedom.ogg',
                my_path + 'Audio Clips for Python/Classical-Wagner - Entrance of the Gods.mp3',
                my_path + 'Audio Clips for Python/Classical-Wagner - Parsifal (III) - Good Friday Music.mp3',
                my_path + 'Audio Clips for Python/Classical-Wagner - Ride of the Valkyries.ogg',
                my_path + 'Audio Clips for Python/Heading To Zion.ogg',
                my_path + 'Audio Clips for Python/His Majesty, God!.ogg',
                my_path + 'Audio Clips for Python/R. Kelly - I Believe I Can Fly.mp3',
                my_path + 'Audio Clips for Python/Marvin Gaye_What\'s Going On.mp3', 
                my_path + 'Audio Clips for Python/Sacred Spirit - Chants and Dances of the Native American  - .mp3'] 
                
                
    
    
    

# Selections by Genre


# global all_clips
# Uncomment to Select Clips from All Sources
# all_tracks = classical_clips #+ jazz_rb_clips + jubilee_clips  + tribal_winds   #  select music_clips add as needed for other clips

#  Uncomment to Select Winston Rhodes Music Only
# all_tracks = jubilee_clips 

# Uncomment to select classical clips only
# all_tracks = classical_clips

#Select a specified list? Just copy and paste the selection(s) from the above sets into the select_clips set.
all_tracks = select_clips

# Uncomment to select Jazz_RB clips only
# all_tracks = jazz_rb_clips

def pick_track():
    global my_audio_clip
    global my_track
    random.shuffle(all_tracks)
    my_audio_clip = random.choice(all_tracks)
   #     my_track = my_audio_clip.lstrip(my_path + 'Audio Clips for Python/')
    prefix = my_path + 'Audio Clips for Python/'
    suffix = '.mp3'
    suffix_a = '.ogg'
    if  suffix_a in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix_a)
    else:
        this_track = my_audio_clip.removesuffix(suffix)
    my_track = this_track.removeprefix(prefix)
       
pick_track()



print(my_audio_clip)
print(my_track)



        




  
              