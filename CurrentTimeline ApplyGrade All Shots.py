# On which audio track is your sound and which item number is your item
track = 1
# DRX file
drx = '/Users/guillaume/Pictures/Stabilize_1.1.1.drx'
### END CONFIGURATION

# Setting up stabilizer mode to "translation"
# Do this before doing ANY color grading!
# 1- Go to the color tab
# 2- Set one clip to "translation"
# 3- Stabilize
# 4- Clear tracking point (button above stabilize)
# 5- Grab a still of the clip
# 6- Export the still
# 7- Copy/paste the DPR file in the configuration variable of the the script
# 8- Run the script in the console with Py2

import sys

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
tli = tl.GetItemsInTrack("video", track) 

print tl.ApplyGradeFromDRX(drx, 0, tli) 

print
print 'End of script'