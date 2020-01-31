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
  python3 sample.setFileType()
endfunction

function! PrintFile()
  python3 sample.printFile()
endfunction

function! DiscordConnect()
  python3 sample.DiscordConnect()
endfunction

function! SetPresence()
  python3 sample.setPresence()
endfunction

" TODO: Put all functions as args under :rp
" Commands
command! -nargs=0 SetPresence call SetPresence()

" Autocmd group
augroup pythonscripts
  autocmd!
  autocmd FileType * call FileType()
  autocmd VimEnter * call DiscordConnect()
augroup END

let g:vim_presence_loaded = 1
