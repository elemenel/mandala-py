# Music Clips for merging to video and other projects

import random
import os
import platform
from moviepy.editor import *
import audio_clips as au
from moviepy.editor import AudioFileClip, ImageClip

my_os = platform.system()
if my_os == 'Linux':
    my_path = '/media/elemen/Inland SSD'
    
else:
    my_path = 'E:'

# music_clips  ---Music list


relaxing_tones = [my_path + '/Audio Clips for Python/infinitely-Ambient-Music.mp3',
                            my_path +'/Audio Clips for Python/Farm.mp3',
                            my_path +'/Audio Clips for Python/Brahms - Cradle Song (1868).ogg',
                            my_path +'/Audio Clips for Python/Meydan-Elk.mp3',
                            my_path +'/Audio Clips for Python/Meydan-Away.mp3',
                            my_path +'/Audio Clips for Python/Evening-Improvisation-with-Ethera.mp3',
                            my_path +'/Audio Clips for Python/Calm-and-Peaceful.mp3',
                            my_path +'/Audio Clips for Python/alex-productions-ambient-music-nature.mp3',
                            my_path +'/Audio Clips for Python/scott-buckley-reverie.mp3',
                            my_path +'/Audio Clips for Python/Otjanbird-Pt.-II.mp3',
                            my_path +'/Audio Clips for Python/melody-of-nature-main.mp3',
                            my_path +'/Audio Clips for Python/Spatium-Calm-Ambient-Music.mp3',
                            my_path +'/Audio Clips for Python/Heart-Of-The-Ocean.mp3',
                            my_path +'/Audio Clips for Python/sb_adriftamonginfinitestars.mp3',
                            my_path +'/Audio Clips for Python/sb_aurora.mp3',
                            my_path +'/Audio Clips for Python/Sunset-Landscape.mp3',
                            my_path +'/Audio Clips for Python/purrple-cat-lullaby.mp3',
                            my_path +'/Audio Clips for Python/Awake.mp3',
                           my_path +'/Audio Clips for Python/purrple-cat-green-tea.mp3',
                           my_path +'/Audio Clips for Python/Arnor.mp3',
                           my_path +'/Audio Clips for Python/a-promise.mp3',
                            my_path +'/Audio Clips for Python/Winter.mp3',
                            my_path +'/Audio Clips for Python/Embrace.mp3']


classical_clips =[my_path + '/Audio Clips for Python/A Midsummer Night\'s Dream - Intermezzo.ogg',
                my_path +'/Audio Clips for Python/A Midsummer Night\'s Dream - Nocturne.ogg',
                my_path +'/Audio Clips for Python/A Midsummer Night\'s Dream - Scherzo.ogg',
                my_path +'/Audio Clips for Python/A Midsummer Night\'s Dream - Wedding March.ogg',
                my_path +'/Audio Clips for Python/Beethoven 9th Symphony - excerpt.mp3',
#                 my_path +'/Audio Clips for Python/Beethoven Symphony 7 II.mp3',
#                 my_path +'/Audio Clips for Python/Beethoven Symphony 7 IV.mp3',
                my_path +'/Audio Clips for Python/Bizet - L\'Arlesienne-Intermezzo.ogg',
                my_path +'/Audio Clips for Python/Bizet - Les Toreadors, from Carmen (1875).ogg',
                my_path +'/Audio Clips for Python/Brahms - Cradle Song (1868).ogg',
                my_path +'/Audio Clips for Python/Delibes - Notturno, from Coppelia (1870).ogg',
                my_path +'/Audio Clips for Python/Dvorák, Budapest Strings - Humoresque no 7, B. 187 (Op. 101).ogg',
                my_path +'/Audio Clips for Python/Edvard Grieg, Solveig\'s Song from Peer Gynt.ogg',
                my_path +'/Audio Clips for Python/Felix Mendelssohn,  Wedding March, from A Midsummers Night Dream.ogg',
                my_path +'/Audio Clips for Python/Grieg - Morning, from Peer Gynt.ogg',
                my_path +'/Audio Clips for Python/Jean Sibelius - Karelia Suite, Op. 11 - Alla marcia.mp3',
                my_path +'/Audio Clips for Python/Jean Sibelius - Lemminkainen\'s Return, Op. 22, No. 4.mp3',
                my_path +'/Audio Clips for Python/Massenet, Budapest Philharmonic - Méditation from the opera Thaïs.ogg',
                my_path +'/Audio Clips for Python/Ode to Joy - Cooper Cannell.mp3',
                my_path +'/Audio Clips for Python/Piano Concerto no. 1 in B‐flat minor, op. 23.ogg',
                my_path +'/Audio Clips for Python/Richard Strauss, Hungarian State Orchestra - Opening Fanfare - Also Sprach Zarathustra, Op. 30.ogg',
                my_path +'/Audio Clips for Python/Richard Wagner - Festival March from Tannhauser.mp3',
                my_path +'/Audio Clips for Python/Richard Wagner - Liebestod (Love-Death) from Tristan und Isolde.mp3',
                my_path +'/Audio Clips for Python/Richard Wagner - Prelude to Act III of Lohengrin.mp3',
                my_path +'/Audio Clips for Python/Richard Wagner - The Ride of the Valkyries from Die Walkure.mp3',
                my_path + '/Audio Clips for Python/Schubert, Ave Maria.ogg',
                my_path + '/Audio Clips for Python/Tchaikovsky_Sym5_III.mp3',
                my_path + '/Audio Clips for Python/Wagner - Entrance of the Gods.mp3',
                my_path + '/Audio Clips for Python/Wagner - Ride of the Valkyries.ogg',
                my_path + '/Audio Clips for Python/Waltz From Serenade for Strings.ogg',
                my_path + '/Audio Clips for Python/Waltz From The Sleeping Beauty.ogg',
                my_path + '/Audio Clips for Python/Wedding Dance From “Swan Lake” Suite op. 20.ogg',
                my_path +'/Audio Clips for Python/Ludwig von Beethoven - Piano Concerto No. 3 in C Major, Opus 37, Allegro.mp3',
                 my_path +'/Audio Clips for Python/Ludwig von Beethoven - Piano Concerto No. 3 in C Major, Opus 37, Largo.mp3',
                 my_path +'/Audio Clips for Python/Ludwig von Beethoven - Beethoven - Piano Concerto in E Flat (1784) The Lost Concerto- 3 Rondo allegretto.mp3',
                 my_path +'/Audio Clips for Python/Ludwig van Beethoven - Piano Concerto No. 2 in B Flat Major, Opus 19, Rondo.mp3',
                 my_path +'/Audio Clips for Python/Ludwig van Beethoven - Piano Concerto No. 2 in B Flat Major, Opus 19, Adagio.mp3',
                 my_path +'/Audio Clips for Python/Ludwig van Beethoven - Piano Concerto No. 1 in C Major, Opus 15, Rondo.mp3',
                 my_path +'/Audio Clips for Python/Jascha Heifetz - Brahms Violin Concerto - 2 Adagio.mp3',
                 my_path +'/Audio Clips for Python/Jascha Heifetz - Beethoven Violin Concerto - 3 Rondo Allegretto.mp3',
                 my_path +'/Audio Clips for Python/Jascha Heifetz - Brahms Violin Concerto - 3 Allegro giocoso, ma non troppo vivace.mp3',
                 my_path +'/Audio Clips for Python/Jascha Heifetz - Beethoven Violin Concerto - 2 Larghetto.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Nebukadnezar Fangernes kor (Va, pensiero).mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Gymnopedie nr. 3 (ork. af Debussy).mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Figaros bryllup Porgi, amor.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Kinderszenen Traumerei.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Violinkoncert i D-dur (anden sats).mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Klaverkoncert nr. 1 i b-mol (anden sats).mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Dyrenes karneval Svanen.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Trompetkoncert i Es-dur (anden sats).mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Suite nr.3 i D-dur, Air.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Requiem Sanctus.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Klaverkvintet i A-dur, Forellen (anden sats).mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Xerxes Largo.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Appalachian Spring Praludium.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Koanga LaCalinda.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Eine kleine Nachtmusik (forste sats).mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Madama Butterfly Nynnekoncert.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Porgy and Bess Summertime.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Recuerdos de la Alhambra.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Symfoni nr. 6 Pastoralesymfonien (femte sats).mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Furst Igor Polovetserdanse.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Sange fra Auvergne Bailero.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Nocturne i Es-dur.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - De fire arstider Sommeren.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Pigen med horharet.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Arabesque No.1.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Pictures at an Exhibition The Old Castle.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Serenade for Strings in E Minor, Opus 20 Second Movement.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Orpheus and Eurydice Dance of the Blessed Spirits.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Fantasia para un Gentilhombre (For Guitar and Orchestra) First Movement.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Cantata BMV 208, Where Sheep May Safely Graze.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Clarinet Concerto Second Movement.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Peer Gynt Suite No.1 Prelude (Morning).mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Florida Suite By the River.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Thais Meditation.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Bagatelle in A Minor, Fur Elise.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Pavane, Opus 50.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Salut damour.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Goyescas The Beauty and the Nightingale.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Romeo And Juliet Fantasy Overture.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Symphony No.3 in F Major, Opus 90 Third Movement.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Double Violin Concerto in D Minor, BWV 1062 Second Movement.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Pelleas et Melissande Sicilienne.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Liebestraume No.3 in A-Flat.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - LElisir Damore Una furtiva lagrima.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - The Marriage of Figaro Voi che sapete.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - The Planets Venus, the Bringer of Peace.mp3',
                 my_path +'/Audio Clips for Python/In Classical Mood - Porgy And Bess Bess You Is My Woman Now.mp3']
#                  my_path +'/Audio Clips for Python/Gerard Schwarz - Strauss Dance of the Seven Veils.mp3']

 

jubilee_clips  = [my_path + '/Audio Clips for Python/A Rasta Man\'s Prayer.ogg',
#                 my_path + '/Audio Clips for Python/Drink From The Living Water.ogg',
                my_path + '/Audio Clips for Python/Freedom.ogg',
                my_path + '/Audio Clips for Python/Heading To Zion.ogg',
                my_path + '/Audio Clips for Python/His Majesty, God!.ogg',
                my_path + '/Audio Clips for Python/I Never Knew.ogg',
                my_path + '/Audio Clips for Python/\'Jubilee\'!.ogg',
                my_path + '/Audio Clips for Python/Life\'s Storms.ogg',
                my_path + '/Audio Clips for Python/Music Still Blowing In The Wind.ogg',
                my_path + '/Audio Clips for Python/On A Heavenly Journey.ogg',
                my_path + '/Audio Clips for Python/On The Hallelujah Trail.ogg',
                my_path + '/Audio Clips for Python/Spread Your Tender Mercy Over Me.ogg',
                my_path + '/Audio Clips for Python/Thank God I\'m Forgiven.ogg',
                my_path + '/Audio Clips for Python/Trav\'lin On The Tracks of Life.ogg',
                my_path + '/Audio Clips for Python/Yes I\'m Still Here Lord.ogg']





jazz_rb_clips = [my_path + '/Audio Clips for Python/The Drifters - Please Stay.ogg',
                my_path + '/Audio Clips for Python/The Drifters - This Magic Moment.ogg',
                my_path + '/Audio Clips for Python/The Drifters - Up On The Roof.ogg',
                my_path + '/Audio Clips for Python/The Drifters - There Goes My Baby.ogg',
                my_path + '/Audio Clips for Python/The Drifters - Save The Last Dance For Me.ogg',
                my_path + '/Audio Clips for Python/The Drifters - On Broadway.ogg',
                my_path + '/Audio Clips for Python/The Drifters - Under The Boardwalk.ogg',
                my_path + '/Audio Clips for Python/Fabolous - Breathe.mp3',
                my_path + '/Audio Clips for Python/Jerry Butler - Gypsy Woman.mp3',
                my_path + '/Audio Clips for Python/John Coltrane - My Favorite Things.mp3',
                my_path + '/Audio Clips for Python/Jennifer Hudson - Where You At.mp3',
                my_path + '/Audio Clips for Python/Downpresser Scrolls of the Prophet- Peter Tosh.mp3',
                my_path + '/Audio Clips for Python/Maxwell - Pretty Wings.mp3',
                my_path + '/Audio Clips for Python/R. Kelly - I Believe I Can Fly.mp3',
                my_path + '/Audio Clips for Python/Pharoah Sanders - The Creator Has A Masterplan (Edit).mp3',
                my_path + '/Audio Clips for Python/Cameo - Candy.mp3',
                my_path + '/Audio Clips for Python/Marvin Gaye_What\'s Going On.mp3',
                my_path + '/Audio Clips for Python/Jill Scott-Love_Rain_(Coffee_Shop_Mix).mp3',
                my_path + '/Audio Clips for Python/Fugees_Everything_Is_Everything.mp3',
                my_path + '/Audio Clips for Python/Sam_Cooke_-_Bring_It_On_Home_To_Me.mp3',
                my_path + '/Audio Clips for Python/The Whispers-And_The_Beat_Goes_On.mp3',
                my_path + '/Audio Clips for Python/Teena Marie_I_Need_Your_Lovin.mp3',
                my_path + '/Audio Clips for Python/Shabaka_Mr.Jackson.mp3',
                my_path + '/Audio Clips for Python/MaryJBlige-No One Will Do.mp3',
                my_path + '/Audio Clips for Python/Heart_Attack_[Explicit].mp3',
                my_path + '/Audio Clips for Python/Bottoms_Up_(feat__Nicki_Minaj).mp3',
                my_path + '/Audio Clips for Python/African_Spirit.mp3',
                my_path + '/Audio Clips for Python/Shabaka_See_Dem_A_Come.mp3',
                my_path + '/Audio Clips for Python/Shabaka_Thy_Will_Be_Done.mp3',
                my_path + '/Audio Clips for Python/African_Rock.mp3 ',
                my_path + '/Audio Clips for Python/See Dem A Come II (Remix).mp3',
                my_path + '/Audio Clips for Python/India.Arie - Wings Of Forgiveness.mp3',
                my_path + '/Audio Clips for Python/Shabaka - Thy Will Be Done.mp3']






tribal_winds = [my_path + '/Audio Clips for Python/Joseph Fire Crow - Creator\'s Prayer.ogg',
                my_path + '/Audio Clips for Python/I Never Knew.ogg',
                my_path + '/Audio Clips for Python/William Gutierrez - Song for Grandfather.ogg',
                my_path + '/Audio Clips for Python/R. Carlos Nakai & William Eaton - Covenants Shared.ogg',
                my_path + '/Audio Clips for Python/Fernando Cellicion - Eagle Dance Song.ogg',
                my_path + '/Audio Clips for Python/Kevin Locke - Lakota Prayer.ogg',
                my_path + '/Audio Clips for Python/Andrew Vasquez - Eagle\'s Journey.ogg',
                my_path +  '/Audio Clips for Python/Kevin Locke - Medicine of the Meadowlark.ogg',
                my_path + '/Audio Clips for Python/Bryan Akipa - First Flute Song.ogg',
                my_path + '/Audio Clips for Python/Andrew Vasquez - Memory of Earth Mother.ogg',
                my_path + '/Audio Clips for Python/Wind In My Mind.ogg',
                my_path + '/Audio Clips for Python/First Flight.ogg',
                my_path + '/Audio Clips for Python/Along the River.ogg',
                my_path + '/Audio Clips for Python/Memory of Earth Mother.ogg',
                my_path + '/Audio Clips for Python/First Flute.ogg',
                my_path + '/Audio Clips for Python/Medicine of the Meadowlark.ogg',
                my_path + '/Audio Clips for Python/Eagle\'s Journey.ogg',
                my_path + '/Audio Clips for Python/Lakota Prayer.ogg',
                my_path + '/Audio Clips for Python/Eagle Dance Song.ogg',
                my_path + '/Audio Clips for Python/Covenants Shared.ogg',
                my_path + '/Audio Clips for Python/Song For Grandfather.ogg',
                my_path + '/Audio Clips for Python/Circle of Life.ogg',
                my_path + '/Audio Clips for Python/Creator\'s Prayer.ogg',
                my_path + '/Audio Clips for Python/Sacred Spirit - Chants and Dances of the Native American  - .mp3']


select_clips = [ my_path + '/Audio Clips for Python/Downpresser Scrolls of the Prophet- Peter Tosh.mp3',
                my_path + '/Audio Clips for Python/I Never Knew.ogg',
                my_path + '/Audio Clips for Python/Ave_Maria.mp3', 
                my_path + '/Audio Clips for Python/Classical-Beethoven Symphony 7 III.mp3',
                my_path + '/Audio Clips for Python/India.Arie - Wings Of Forgiveness.mp3',
#                 my_path + '/Audio Clips for Python/Drink From The Living Water.ogg',
                my_path + '/Audio Clips for Python/Classical-Richard Wagner - Track 10.mp3',
                my_path + '/Audio Clips for Python/Freedom.ogg',
                my_path + '/Audio Clips for Python/Kevin Locke - Lakota Prayer.ogg',
                my_path + '/Audio Clips for Python/Classical-Wagner - Entrance of the Gods.mp3',
                my_path + '/Audio Clips for Python/Classical-Wagner - Parsifal (III) - Good Friday Music.mp3',
                my_path + '/Audio Clips for Python/Classical-Wagner - Ride of the Valkyries.ogg',
                my_path + '/Audio Clips for Python/Heading To Zion.ogg',
                my_path + '/Audio Clips for Python/His Majesty, God!.ogg',
               my_path + '/Audio Clips for Python/Classical-Rimsky-Korsakov-Scheherazade-II_sample.mp3',
                my_path + '/Audio Clips for Python/Classical-Rimsky-Korsakov-Scheherazade-III_sample.mp3',
                my_path + '/Audio Clips for Python/Classical-Rimsky-Korsakov-Scheherazade-I_sample.mp3',
                my_path + '/Audio Clips for Python/Classical-Johann Strauss II, Tales From The Vienna Woods_sample.ogg',
                my_path + '/Audio Clips for Python/1812 Overture, op. 49_sample.ogg',
                my_path +'/Audio Clips for Python/Classical-Tchaikovsky - Piano Concerto No. 1 in B flat minor, 1st movement_sample.ogg',
                my_path + '/Audio Clips for Python/Classical-Smetana - The Moldau (1875)_sample.ogg',
                my_path +'/Audio Clips for Python/Classical-Tchaikovsky - Marche Slave, Op. 31 (1876)_sample.ogg',
                my_path + '/Audio Clips for Python/Classical-J. STRAUSS II The Blue Danube-Waltz_sample.ogg',
                my_path + '/Audio Clips for Python/Classical-A Midsummer Night\'s Dream - Overture_sample.ogg',
                my_path + '/Audio Clips for Python/Classical-Richard Wagner - Dawn and Siegfried\'s Rhine Journey from Gotterdammerung_sample.mp3',
                my_path + '/Audio Clips for Python/Classical-Richard Wagner - Overture to Rienzi_sample.mp3',
                my_path + '/Audio Clips for Python/Classical-Richard Wagner - Prelude to Act I of Die Meistersinger_sample.mp3',
                my_path + '/Audio Clips for Python/Classical-Tchaikovsky_Sym5_I_sample.mp3',
                my_path + '/Audio Clips for Python/Classical-Richard Wagner - from Tristan und Isolde.mp3']

total_clips = [my_path + '/Audio Clips for Python/A Midsummer Night\'s Dream - Intermezzo.ogg',
                    my_path + '/Audio Clips for Python/A Midsummer Night\'s Dream - Nocturne.ogg',
                    my_path + '/Audio Clips for Python/A Midsummer Night\'s Dream - Scherzo.ogg',
                    my_path + '/Audio Clips for Python/A Midsummer Night\'s Dream - Wedding March.ogg',
                    my_path + '/Audio Clips for Python/A Rasta Man\'s Prayer.ogg',
                    my_path + '/Audio Clips for Python/African_Rock.mp3',
                    my_path + '/Audio Clips for Python/African_Spirit.mp3',
                    my_path + '/Audio Clips for Python/Along the River.ogg',
                    my_path + '/Audio Clips for Python/Andrew Vasquez - Eagle\'s Journey.ogg',
                    my_path + '/Audio Clips for Python/Andrew Vasquez - Memory of Earth Mother.ogg',
                    my_path + '/Audio Clips for Python/Ave_Maria.mp3',
                    my_path + '/Audio Clips for Python/Beethoven 9th Symphony - excerpt.mp3',
                    my_path + '/Audio Clips for Python/Beethoven Symphony 7 II.mp3',
                    my_path + '/Audio Clips for Python/Beethoven Symphony 7 IV.mp3',
                    my_path + '/Audio Clips for Python/Bizet - L\'Arlesienne-Intermezzo.ogg',
                    my_path + '/Audio Clips for Python/Bizet - Les Toreadors, from Carmen (1875).ogg',
                    my_path + '/Audio Clips for Python/Bottoms_Up_(feat__Nicki_Minaj).mp3',
                    my_path + '/Audio Clips for Python/Brahms - Cradle Song (1868).ogg',
                    my_path + '/Audio Clips for Python/Bryan Akipa - First Flute Song.ogg',
                    my_path + '/Audio Clips for Python/Cameo - Candy.mp3',
                    my_path + '/Audio Clips for Python/Circle of Life.ogg',
                    my_path + '/Audio Clips for Python/Covenants Shared.ogg',
                    my_path + '/Audio Clips for Python/Creator\'s Prayer.ogg',
                    my_path + '/Audio Clips for Python/Delibes - Notturno, from Coppelia (1870).ogg',
                    my_path + '/Audio Clips for Python/Downpresser Scrolls of the Prophet- Peter Tosh.mp3',
#                     my_path + '/Audio Clips for Python/Drink From The Living Water.ogg',
                    my_path + '/Audio Clips for Python/Dvorák, Budapest Strings - Humoresque no 7, B. 187 (Op. 101).ogg',
                    my_path + '/Audio Clips for Python/Eagle Dance Song.ogg',
                    my_path + '/Audio Clips for Python/Eagle\'s Journey.ogg',
                    my_path + '/Audio Clips for Python/Edvard Grieg, Solveig\'s Song from Peer Gynt.ogg',
                    my_path + '/Audio Clips for Python/Felix Mendelssohn,  Wedding March, from A Midsummers Night Dream.ogg',
                    my_path + '/Audio Clips for Python/Felix Mendelssohn, Budapest Philharmonic - Wedding March, from \'A Midsummer\'s Night Dream,\' Op. 61.ogg',
                    my_path + '/Audio Clips for Python/Fernando Cellicion - Eagle Dance Song.ogg',
                    my_path + '/Audio Clips for Python/First Flight.ogg',
                    my_path + '/Audio Clips for Python/First Flute.ogg',
                    my_path + '/Audio Clips for Python/Freedom.ogg',
                    my_path + '/Audio Clips for Python/Fugees_Everything_Is_Everything.mp3',
#                     my_path + '/Audio Clips for Python/Gerard Schwarz - Strauss Dance of the Seven Veils.mp3',
                    my_path + '/Audio Clips for Python/Grieg - Morning, from Peer Gynt.ogg',
                    my_path + '/Audio Clips for Python/Heading To Zion.ogg',
                    my_path + '/Audio Clips for Python/His Majesty, God!.ogg',
                    my_path + '/Audio Clips for Python/I Never Knew.ogg',
                    my_path + '/Audio Clips for Python/In Classical Mood - Appalachian Spring Praludium.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Arabesque No.1.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Bagatelle in A Minor, Fur Elise.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Cantata BMV 208, Where Sheep May Safely Graze.mp3',
#                     my_path + '/Audio Clips for Python/In Classical Mood - Clarinet Concerto Second Movement.mp3',
#                     my_path + '/Audio Clips for Python/In Classical Mood - De fire arstider Sommeren.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Double Violin Concerto in D Minor, BWV 1062 Second Movement.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Dyrenes karneval Svanen.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Eine kleine Nachtmusik (forste sats).mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Fantasia para un Gentilhombre (For Guitar and Orchestra) First Movement.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Figaros bryllup Porgi, amor.mp3',
#                     my_path + '/Audio Clips for Python/In Classical Mood - Florida Suite By the River.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Furst Igor Polovetserdanse.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Goyescas The Beauty and the Nightingale.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Gymnopedie nr. 3 (ork. af Debussy).mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Kinderszenen Traumerei.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Klaverkoncert nr. 1 i b-mol (anden sats).mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Klaverkvintet i A-dur, Forellen (anden sats).mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Koanga LaCalinda.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - LElisir Damore Una furtiva lagrima.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Liebestraume No.3 in A-Flat.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Madama Butterfly Nynnekoncert.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Nebukadnezar Fangernes kor (Va, pensiero).mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Nocturne i Es-dur.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Orpheus and Eurydice Dance of the Blessed Spirits.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Pavane, Opus 50.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Peer Gynt Suite No.1 Prelude (Morning).mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Pelleas et Melissande Sicilienne.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Pictures at an Exhibition The Old Castle.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Pigen med horharet.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Porgy And Bess Bess You Is My Woman Now.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Porgy and Bess Summertime.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Recuerdos de la Alhambra.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Requiem Sanctus.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Romeo And Juliet Fantasy Overture.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Salut damour.mp3',
#                     my_path + '/Audio Clips for Python/In Classical Mood - Sange fra Auvergne Bailero.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Serenade for Strings in E Minor, Opus 20 Second Movement.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Suite nr.3 i D-dur, Air.mp3',
#                     my_path + '/Audio Clips for Python/In Classical Mood - Symfoni nr. 6 Pastoralesymfonien (femte sats).mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Symphony No.3 in F Major, Opus 90 Third Movement.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Thais Meditation.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - The Marriage of Figaro Voi che sapete.mp3',
#                     my_path + '/Audio Clips for Python/In Classical Mood - The Planets Venus, the Bringer of Peace.mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Trompetkoncert i Es-dur (anden sats).mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Violinkoncert i D-dur (anden sats).mp3',
                    my_path + '/Audio Clips for Python/In Classical Mood - Xerxes Largo.mp3',
                    my_path + '/Audio Clips for Python/India.Arie - Wings Of Forgiveness.mp3',
                    my_path + '/Audio Clips for Python/Jascha Heifetz - Beethoven Violin Concerto - 2 Larghetto.mp3',
                    my_path + '/Audio Clips for Python/Jascha Heifetz - Beethoven Violin Concerto - 3 Rondo Allegretto.mp3',
                    my_path + '/Audio Clips for Python/Jascha Heifetz - Brahms Violin Concerto - 2 Adagio.mp3',
                    my_path + '/Audio Clips for Python/Jascha Heifetz - Brahms Violin Concerto - 3 Allegro giocoso, ma non troppo vivace.mp3',
                    my_path + '/Audio Clips for Python/Jean Sibelius - Karelia Suite, Op. 11 - Alla marcia.mp3',
                    my_path + '/Audio Clips for Python/Jean Sibelius - Lemminkainen\'s Return, Op. 22, No. 4.mp3',
                    my_path + '/Audio Clips for Python/Jennifer Hudson - Where You At.mp3',
                    my_path + '/Audio Clips for Python/Jerry Butler - Gypsy Woman.mp3',
                    my_path + '/Audio Clips for Python/Jill Scott-Love_Rain_(Coffee_Shop_Mix).mp3',
                    my_path + '/Audio Clips for Python/Joseph Fire Crow - Creator\'s Prayer.ogg',
                    my_path + '/Audio Clips for Python/Kevin Locke - Lakota Prayer.ogg',
                    my_path + '/Audio Clips for Python/Kevin Locke - Medicine of the Meadowlark.ogg',
                    my_path + '/Audio Clips for Python/Lakota Prayer.ogg',
                    my_path + '/Audio Clips for Python/Life\'s Storms.ogg',
#                     my_path + '/Audio Clips for Python/Ludwig van Beethoven - Piano Concerto No. 1 in C Major, Opus 15, Rondo.mp3',
#                     my_path + '/Audio Clips for Python/Ludwig van Beethoven - Piano Concerto No. 2 in B Flat Major, Opus 19, Adagio.mp3',
#                     my_path + '/Audio Clips for Python/Ludwig van Beethoven - Piano Concerto No. 2 in B Flat Major, Opus 19, Rondo.mp3',
#                     my_path + '/Audio Clips for Python/Ludwig von Beethoven - Beethoven - Piano Concerto in E Flat (1784) The Lost Concerto- 3 Rondo allegretto.mp3',
#                     my_path + '/Audio Clips for Python/Ludwig von Beethoven - Piano Concerto No. 3 in C Major, Opus 37, Allegro.mp3',
#                     my_path + '/Audio Clips for Python/Ludwig von Beethoven - Piano Concerto No. 3 in C Major, Opus 37, Largo.mp3',
                    my_path + '/Audio Clips for Python/Marvin Gaye_What\'s Going On.mp3',
                    my_path + '/Audio Clips for Python/MaryJBlige-No One Will Do.mp3',
                    my_path + '/Audio Clips for Python/Massenet, Budapest Philharmonic - Méditation from the opera Thaïs.ogg',
                    my_path + '/Audio Clips for Python/Maxwell - Pretty Wings.mp3',
                    my_path + '/Audio Clips for Python/Medicine of the Meadowlark.ogg',
                    my_path + '/Audio Clips for Python/Meditation - Sacred Spirit - Chants And Dances Of The Native.mp3',
                    my_path + '/Audio Clips for Python/Memory of Earth Mother.ogg',
                    my_path + '/Audio Clips for Python/Music Still Blowing In The Wind.ogg',
                    my_path + '/Audio Clips for Python/Ode to Joy - Cooper Cannell.mp3',
                    my_path + '/Audio Clips for Python/Offenbach, The Tales of Hoffman.ogg',
                    my_path + '/Audio Clips for Python/On A Heavenly Journey.ogg',
                    my_path + '/Audio Clips for Python/On The Hallelujah Trail.ogg',
                    my_path + '/Audio Clips for Python/On_The_Ocean.mp3',
                    my_path + '/Audio Clips for Python/Piano Concerto no. 1 in B‐flat minor, op. 23.ogg',
                    my_path + '/Audio Clips for Python/R. Carlos Nakai & William Eaton - Covenants Shared.ogg',
#                     my_path + '/Audio Clips for Python/Richard Wagner - Festival March from Tannhauser.mp3',
#                     my_path + '/Audio Clips for Python/Richard Wagner - Liebestod (Love-Death) from Tristan und Isolde.mp3',
                    my_path + '/Audio Clips for Python/Richard Wagner - Prelude to Act III of Lohengrin.mp3',
                    my_path + '/Audio Clips for Python/Richard Wagner - The Ride of the Valkyries from Die Walkure.mp3',
                    my_path + '/Audio Clips for Python/Sacred Spirit - Chants and Dances of the Native American  - .mp3',
                    my_path + '/Audio Clips for Python/Sam_Cooke_-_Bring_It_On_Home_To_Me.mp3',
                    my_path + '/Audio Clips for Python/Schubert, Ave Maria.ogg',
                    my_path + '/Audio Clips for Python/See Dem A Come II (Remix).mp3',
                    my_path + '/Audio Clips for Python/Shabaka - Thy Will Be Done.mp3',
                    my_path + '/Audio Clips for Python/Shabaka_Mr.Jackson.mp3',
                    my_path + '/Audio Clips for Python/Shabaka_See_Dem_A_Come.mp3',
                    my_path + '/Audio Clips for Python/Song For Grandfather.ogg',
                    my_path + '/Audio Clips for Python/Spread Your Tender Mercy Over Me.ogg',
                    my_path + '/Audio Clips for Python/Tchaikovsky_Sym5_III.mp3',
                    my_path + '/Audio Clips for Python/Teena Marie_I_Need_Your_Lovin.mp3',
                    my_path + '/Audio Clips for Python/Thank God I\'m Forgiven.ogg',
                    my_path + '/Audio Clips for Python/The Drifters - On Broadway.ogg',
                    my_path + '/Audio Clips for Python/The Drifters - Please Stay.ogg',
                    my_path + '/Audio Clips for Python/The Drifters - Save The Last Dance For Me.ogg',
                    my_path + '/Audio Clips for Python/The Drifters - There Goes My Baby.ogg',
                    my_path + '/Audio Clips for Python/The Drifters - This Magic Moment.ogg',
                    my_path + '/Audio Clips for Python/The Drifters - Under The Boardwalk.ogg',
                    my_path + '/Audio Clips for Python/The Drifters - Up On The Roof.ogg',
                    my_path + '/Audio Clips for Python/The Whispers-And_The_Beat_Goes_On.mp3',
                    my_path + '/Audio Clips for Python/Tom Mauchahty-Ware - Circle of Life.ogg',
                    my_path + '/Audio Clips for Python/Trav\'lin On The Tracks of Life.ogg',
                    my_path + '/Audio Clips for Python/Wagner - Entrance of the Gods.mp3',
                    my_path + '/Audio Clips for Python/Wagner - Ride of the Valkyries.ogg',
                    my_path + '/Audio Clips for Python/Waltz From Serenade for Strings.ogg',
                    my_path + '/Audio Clips for Python/Waltz From The Sleeping Beauty.ogg',
                    my_path + '/Audio Clips for Python/Wedding Dance From “Swan Lake” Suite op. 20.ogg',
                    my_path + '/Audio Clips for Python/William Gutierrez - Song for Grandfather.ogg',
                    my_path + '/Audio Clips for Python/Wind In My Mind.ogg',
                    my_path + '/Audio Clips for Python/Yes I\'m Still Here Lord.ogg']

long_clips = [my_path + '/Lengthy Audio/Smetana - The Moldau (1875).ogg',
                    my_path + '/Lengthy Audio/John Coltrane - My Favorite Things.mp3',
                    my_path + '/Lengthy Audio/Tchaikovsky_Sym5_I.mp3',
                    my_path + '/Lengthy Audio/Capriccio Italien, op. 45.ogg',
                    my_path + '/Lengthy Audio/1812 Overture, op. 49.ogg',
                    my_path + '/Lengthy Audio/Tchaikovsky - 1812 Overture, op. 49.ogg',
                    my_path + '/Lengthy Audio/Richard Wagner - Prelude to Act I of Die Meistersinger.mp3',
                    my_path + '/Lengthy Audio/Richard Wagner - Overture to Rienzi.mp3',
                    my_path + '/Lengthy Audio/Richard Wagner - Dawn and Siegfried\'s Rhine Journey from Gotterdammerung.mp3',
                    my_path + '/Lengthy Audio/Richard Wagner - Overture to The Flying Dutchmen.mp3',
                    my_path + '/Lengthy Audio/J. STRAUSS II The Blue Danube-Waltz.ogg',
                    my_path + '/Lengthy Audio/Tchaikovsky - Marche Slave, Op. 31 (1876).ogg',
                    my_path + '/Lengthy Audio/Tchaikovsky - Piano Concerto No. 1 in B flat minor, 1st movement (excerpt) (1875).ogg',
                    my_path + '/Lengthy Audio/A Midsummer Night\'s Dream - Overture.ogg',
                    my_path + '/Lengthy Audio/Overture The Hebrides - Fingal\'s Cave.ogg',
                    my_path + '/Lengthy Audio/Johann Strauss II, Tales From The Vienna Woods.ogg',
                    my_path + '/Lengthy Audio/Tchaikovsky,Excerpt from 1st movement of Piano Concerto No. 1 in B-flat minor, Op. 23.ogg',
                    my_path + '/Lengthy Audio/Marche Slave, op. 31.ogg',
                    my_path + '/Lengthy Audio/Rimsky-Korsakov-Scheherazade-I.mp3',
                    my_path + '/Lengthy Audio/Rimsky-Korsakov-Scheherazade-III.mp3',
                    my_path + '/Lengthy Audio/Rimsky-Korsakov-Scheherazade-II.mp3',
                    my_path + '/Lengthy Audio/Tchaikovsky_Sym5_IV.mp3',
                    my_path + '/Lengthy Audio/Tchaikovsky_Sym5_II.mp3',
                    my_path + '/Lengthy Audio/Drink From The Living Water_resample.ogg',
                    my_path + '/Lengthy Audio/New World Symphony.mp3',
                    my_path + '/Lengthy Audio/Beethoven Symphony 7 III.mp3',
                    my_path + '/Lengthy Audio/Beethove Symphony 7 I.mp3',
                    my_path + '/Lengthy Audio/Wagner - Parsifal (III) - Good Friday Music.mp3',
                    my_path + '/Lengthy Audio/Pharoah Sanders - The Creator Has A Masterplan (Edit).mp3',
                    my_path + '/Lengthy Audio/Classical Selection-Wagner.mp3',
                    my_path + '/Lengthy Audio/Richard Wagner - Track 10.mp3',
                    my_path + '/Lengthy Audio/Beethoven 7th Symphony - Allegretto.mp3',
                    my_path + '/Lengthy Audio/Rachmaninoff - Piano Concerto 2 - excerpt.mp3',
                    my_path + '/Lengthy Audio/Jean Sibelius - Finlandia, Op. 26.mp3']

# Selections by Genre
# To select a single clip, select one from above and paste it below and uncomment
# all_tracks = [my_path + '/Lengthy Audio/John Coltrane - My Favorite Things.mp3']
              

# global all_clips
# Uncomment to Select Clips from All Sources
# all_tracks = classical_clips #+ jazz_rb_clips + jubilee_clips  + tribal_winds   #  select music_clips add as needed for other clips

#  Uncomment to Select Winston Rhodes Music Only
# all_tracks = jubilee_clips

# Uncomment to select classical clips only
# all_tracks = classical_clips

#Select a specified list? Just copy and paste the selection(s) from the above sets into the select_clips set.
all_tracks = relaxing_tones + [my_path + '/Audio Clips for Python/Schubert, Ave Maria.ogg',
       my_path + '/Audio Clips for Python/Wagner - Entrance of the Gods.mp3',
       my_path + '/Audio Clips for Python/Meditation - Sacred Spirit - Chants And Dances Of The Native.mp3',
       my_path + '/Audio Clips for Python/India.Arie - Wings Of Forgiveness.mp3',
       my_path + '/Audio Clips for Python/In Classical Mood - Cantata BMV 208, Where Sheep May Safely Graze.mp3',
       my_path + '/Audio Clips for Python/Drink From The Living Water.ogg',
       my_path + '/Audio Clips for Python/I Never Knew.ogg',
       my_path + '/Audio Clips for Python/Joseph Fire Crow - Creator\'s Prayer.ogg',
       my_path + '/Audio Clips for Python/Kevin Locke - Lakota Prayer.ogg',
       my_path + '/Audio Clips for Python/Kevin Locke - Medicine of the Meadowlark.ogg',
       my_path + '/Audio Clips for Python/Jean Sibelius - Lemminkainen\'s Return, Op. 22, No. 4.mp3',
       my_path + '/Audio Clips for Python/Jennifer Hudson - Where You At.mp3',
       my_path + '/Lengthy Audio/A Midsummer Night\'s Dream - Overture.ogg',
       my_path + '/Lengthy Audio/Overture The Hebrides - Fingal\'s Cave.ogg',                        
       my_path + '/Audio Clips for Python/Jerry Butler - Gypsy Woman.mp3']
       
#                                
                               
                            

# Uncomment to select Jazz_RB clips only
# all_tracks = jazz_rb_clips

# Uncomment to select long clips only
# all_tracks = long_clips

def pick_track():
    global my_audio_clip
    global my_track
#     random.shuffle(all_tracks)
    my_audio_clip = random.choice(all_tracks)
    prefix = my_path + '/Audio Clips for Python/'
    prefix_a = my_path + '/Lengthy Audio/'
    suffix = '.mp3'
    suffix_a = '.ogg'
    if  suffix_a in my_audio_clip:
        this_track = my_audio_clip.removesuffix(suffix_a)
        my_track = this_track.removeprefix(prefix)

    elif prefix_a in my_audio_clip:
        my_track = this_track.removeprefix(prefix_a)
   
                      
    else:
        this_track = my_audio_clip.removesuffix(suffix)
        my_track = this_track.removeprefix(prefix)
#         my_track = this_track.removeprefix(prefix_a)
    print(my_audio_clip)
    print(my_track)
# pick_track()







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

    import os
    path_of_the_directory = my_path + '/Lengthy Audio/'
    object = os.scandir(path_of_the_directory)
    print("Files and Directories in '% s':" % path_of_the_directory)
    for n in object :
        if n.is_dir() or n.is_file():
            print(n.name)
            get_duration()
            print('====================================')
    object.close()

# file_duration()



        




  
              
