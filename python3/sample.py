# TODO: Spectate button opens gotty
import vim
import os
from pypresence import Presence

# Variables to feed into Discord
rp = None           # Discord Client Class
fileType = ''       # File Type

def SetFileType(): # Puts vim '&filetype' variable into fileType
    global fileType
    fileType = vim.eval('&filetype')
    print(fileType)

def PrintFile(): # DEBUG
    print(fileType)

def DiscordConnect():
    global rp
    rp = Presence('672929723382235136') # Client ID
    rp.connect() # Start Handshake loop
    print("Achievement Get: Discord Connected!")
    
def SetPresence():
    if fileType.lower() in ['vim', 'python']: # Current supported images
        rp.update(state = f'Editing a {fileType} file!', details = 'testing testing', large_image = fileType, small_image = 'vim')

def ClearPresence():
    rp.clear(pid=os.getpid())
    print("Presence cleared")

