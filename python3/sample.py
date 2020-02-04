# TODO: Spectate button opens gotty
import vim
import os
from pypresence import Presence

# Variables to feed into Discord
rp = None           # Discord Client Class
fileType = ''       # File Type
files = ['go', 'java', 'javascript', 'python', 'vim'] # Current supported icons

modes = {
    'n': 'NORMAL',
    'v': 'VISUAL',
    'V': 'V-LINE',
    'CTRL-V': 'V-BLOCK',
    's': 'SELECT',
    'S': 'S-LINE',
    'CTRL-S': 'S-BLOCK',
    'i': 'INSERT',
    'R': 'REPLACE'
}

def SetFileType(): # Puts vim '&filetype' variable into fileType
    global fileType
    fileType = vim.eval('&filetype')

#def PrintFile(): # DEBUG
#    print(fileType)

def DiscordConnect():
    global rp
    rp = Presence('672929723382235136') # Client ID
    rp.connect() # Start Handshake loop
    #print("Achievement Get: Discord Connected!")

def SetPresence():
    rp.update(
        state = modes[vim.eval('mode()')],
        details = f'Editing a {fileType} file!',
        large_image = fileType if fileType in files else 'default',
        large_text = fileType if fileType in files else 'File!',
        small_image = 'vim',
        small_text = 'Vim',
        #party_size = [int(vim.eval('line(".")')), int(vim.eval('line("$")'))]
        party_size = [1,5] # TEST WITH RYAN LATER
    )

def ClearPresence():
    rp.clear(pid=os.getpid())
    print("Presence cleared")

def Help():
    print("TODO: Help command")

cmdKey = {
        'set'  : SetPresence,
        'clear': ClearPresence,
        'help' : Help
        }

def CmdHandler(arg):
    if arg.lower() in cmdKey:
        cmdKey[arg.lower()]()
    else:
        print('vim-presence: Unrecognized command. Use `:vp help` for a list.')

