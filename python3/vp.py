# TODO: Spectate button opens gotty
import vim
import os
import time
import subprocess

from pypresence import Presence

def DiscordRunning():
    # TODO: Simplify with Grep. Trying to put it all in the list below breaks it
    psout = subprocess.Popen(['ps', '-e'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    stdout,stderr = psout.communicate()

    # Decoding `byte` to `str`
    Procs = stdout.decode('utf-8')

    # If Discord is in processes
    if Procs.find("Discord") != -1:
        return True
    else:
        return False

# Variables to feed into Discord
hasDiscord = DiscordRunning()  # True if Discord is running
rp = None                      # Discord Client Class
fileType = ''                  # File Type
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

def vprint(args):
    print(f'vim-presence: {args}')

def FileType(): # Puts vim '&filetype' variable into fileType
    global fileType
    fileType = vim.eval('&filetype')

def DiscordConnect():
    # PRECONDITIONS: Discord is running and timeout didn't fire
    if hasDiscord:
        global rp
        rp = Presence('672929723382235136') # Client ID
        rp.connect() # Start Handshake loop

def SetPresence():
    rp.update(
        state = modes[vim.eval('mode()')],
        details = f'Editing a {fileType} file!',
        large_image = fileType if fileType in files else 'default',
        large_text = fileType,
        small_image = 'vim',
        small_text = 'Vim',
        #party_size = [int(vim.eval('line(".")')), int(vim.eval('line("$")'))] # May create issue of long player list
        #party_size = [1,5] # TEST WITH RYAN LATER
        start = time.time()
    )
    vprint('status set!')

def ClearPresence():
    rp.clear(pid=os.getpid())
    vprint('Discord Presence cleared!')

def EndDiscord():
    if hasDiscord:
        rp.close()

def Help():
    vprint('TODO: Help command')

cmdKey = {
        'set'  : SetPresence,
        'clear': ClearPresence,
        'help' : Help
        }

def CmdHandler(arg=None):
    if arg is None:
        print('vim-presence version 0.0.69. Use `:Vp help` for a list of commands')

    elif hasDiscord == False:
        vprint("Can't run commands as Discord doesn't appear to be running!")

    elif (type(arg)) == str and arg.lower() in cmdKey: 
        cmdKey[arg.lower()]() # Run subcommand
    else:
        print(type(arg))
        vprint('Unrecognized command. Use `:Vp help` for a list.')

