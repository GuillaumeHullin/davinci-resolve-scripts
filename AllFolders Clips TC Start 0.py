#!/usr/bin/ python

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

x = 0
y = 0
def resetTimecodeClips( clips ):
    global x
    global y

    for i in clips:
        GetClipName = (clips[i].GetClipProperty("Clip Name"))["Clip Name"]
        GetStartTC = (clips[i].GetClipProperty("Start TC"))["Start TC"]
        x += 1
        if GetStartTC != "00:00:00;00":
            clips[i].SetClipProperty("Start TC", "00:00:00:00")
            print GetClipName
            y += 1    
    
    return

def processFolder ( folder):
    mp.SetCurrentFolder(folder)
    folder = mp.GetCurrentFolder()
    clips = folder.GetClips()
    resetTimecodeClips(clips)
    subfolders = folder.GetSubFolders(folder)
    for s in subfolders:
        print subfolders[s].GetName()
        processFolder ( subfolders[s] )
    
    return

mp.SetCurrentFolder(rootfolder)
folder = mp.GetCurrentFolder()
clips = folder.GetClips()
processFolder( folder )

print
print 'End of script'
print 'Number of clip found:'
print x
print 'Number of "timecode start" modify:'
print y