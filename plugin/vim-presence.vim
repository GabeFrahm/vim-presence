" Checks -------------
if !has('python3')
  echo 'you must have vim built with python3 support to support vim-presence'
  finish
endif

if exists('g:vim_presence_loaded')
  finish
endif

" Set plugin dir -----
let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim

# Setup path for vim and prepare for importing python file
pluginDir = vim.eval('s:plugin_root_dir')
pythonDir = normpath(join(pluginDir, '..', 'python3'))
sys.path.insert(0, pythonDir)

import vp
EOF

" Functions: EDIT, redundant. Call py3 vp.*function name*

" Command handler ----
command! -nargs=? Vp py3 vp.CmdHandler(<f-args>)

" Autocmds -----------
augroup pythonscripts
  autocmd!
  autocmd FileType * py3 vp.FileType()
  autocmd VimEnter * py3 vp.DiscordConnect()
  autocmd VimLeave * py3 vp.rp.close()
augroup END

let g:vim_presence_loaded = 1
