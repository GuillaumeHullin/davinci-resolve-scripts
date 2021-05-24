#!/usr/bin/ python

# Beat Marker Python Script
# Made for Resolve V16.2 free
# Copyright 2020 Guillaume Hullin, www.youtube.com/GuillaumeHullin

### CONFIGUARATION VARIABLES
# FPS of your timeline
fps = 30
# Beats per minutes
bpm = 130
# How many beats per time
time= 4
# Offset the beat by the number of frame 
offset = 20.0
# On which audio track is your sound and which item number is your item
track = 2
item = 1

### END CONFIGURATION

import sys

#sys.path.append("C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules")
sys.path.append("/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules")

import DaVinciResolveScript as dvr_script

try:
    resolve = dvr_script.scriptapp("Resolve")
    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    tl = proj.GetCurrentTimeline()
    mp = proj.GetMediaPool()
    rootfolder = mp.GetRootFolder()
    rootclips = rootfolder.GetClips()
    ms = resolve.GetMediaStorage()
    folder = mp.GetCurrentFolder()
    clips = folder.GetClips()

except:
    print("Open the script file and copy/paste in DVR Console :)")
    sys.exit()

# Get the item of the audio track
tli = tl.GetItemsInTrack("audio", track) 
tli = tli[item]

max = tli.GetDuration()

# Calculate where should be placed the beat marker (return the frameNbr)
def calcBeatFrame(beatNbr):
    global offset
    return (((60.0/bpm)*fps)*beatNbr)+offset

tli.DeleteMarkersByColor('Red')
tli.DeleteMarkersByColor('Yellow')

beat = 0.0
x = 0

while beat < max:
    x += 1
    beat = calcBeatFrame(x)

    if x % time:
        tli.AddMarker(beat, 'Yellow', 'Beat Nbr{}'.format(x) , '', 1.0)
    else:
        tli.AddMarker(beat, 'Red', 'Beat Nbr{}'.format(x) , '', 1.0)

    print 'Beat Nbr{} created at {} frame'.format(x,beat)

print
print 'End of script'