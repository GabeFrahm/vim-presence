if !has('python3')
  echo 'you must have vim built with python3 support to support vim-presence'
  finish
endif

if exists('g:vim_presence_loaded')
  finish
endif

" Saving plugin directory into a variable
let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim

# Setup path for vim and prepare for importing python file
pluginDir = vim.eval('s:plugin_root_dir')
pythonDir = normpath(join(pluginDir, '..', 'python3'))
sys.path.insert(0, pythonDir)

import sample
EOF

" Functions
function! FileType()
  py3 sample.SetFileType()
endfunction

function! PrintFile()
  py3 sample.PrintFile()
endfunction

function! DiscordConnect()
  py3 sample.DiscordConnect()
endfunction

function! SetPresence()
  py3 sample.SetPresence()
endfunction

function! ClearPresence()
  py3 sample.ClearPresence()
endfunction

" TODO: Put all functions as args under :rp (ex: :rp set, :rp clear)
" Commands
command! -nargs=0 SetPresence call SetPresence()
command! -nargs=0 ClearPresence call ClearPresence()

" TODO: Work on python cmd handler
command! -nargs=1 Vp py3 sample.CmdHandler(<f-args>) 

" Autocmd group
augroup pythonscripts
  autocmd!
  autocmd FileType * call FileType()
  autocmd VimEnter * call DiscordConnect()
  autocmd VimLeave * py3 sample.rp.close()
augroup END

let g:vim_presence_loaded = 1
