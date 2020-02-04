# TODO: Spectate button opens gotty
import vim
import os
from pypresence import Presence

# Variables to feed into Discord
rp = None           # Discord Client Class
fileType = ''       # File Type
files = ['vim', 'python']

def SetFileType(): # Puts vim '&filetype' variable into fileType
    global fileType
    fileType = vim.eval('&filetype')

def PrintFile(): # DEBUG
    print(fileType)

def DiscordConnect():
    global rp
    rp = Presence('672929723382235136') # Client ID
    rp.connect() # Start Handshake loop
    print("Achievement Get: Discord Connected!")
    
def SetPresence():
    rp.update(
        state = f'This is a stateeeee',
        details = f'Editing a {fileType} file',
        large_image = fileType if fileType in files else 'default',
        large_text = fileType,
        small_image = 'vim',
        small_text = 'Vim'
    )

def ClearPresence():
    rp.clear(pid=os.getpid())
    print("Presence cleared")

