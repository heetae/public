# Python packages

## Pyproj

### Install
- Install
```bash
pip install pyproj
```
- Run following command in `python`
```python
import pyproj
pyproj.test()
```
or in `bash`
```bash
python -c "import pyproj; pyproj.test()"
```
It should be like this:
```bash
14 items had no tests:
    pyproj
    pyproj.Geod
    pyproj.Geod.fwd
    pyproj.Geod.inv
    pyproj.Proj
    pyproj.Proj.__call__
    pyproj.Proj.is_geocent
    pyproj.Proj.is_latlong
    pyproj.Proj.to_latlong
    pyproj._convertback
    pyproj._copytobuffer
    pyproj._copytobuffer_return_scalar
    pyproj._dict2string
    pyproj.test
4 items passed all tests:
  18 tests in pyproj.Geod.__new__
  12 tests in pyproj.Geod.npts
  25 tests in pyproj.Proj.__new__
  23 tests in pyproj.transform
78 tests in 18 items.
78 passed and 0 failed.
Test passed.
```
# Bash packages

## Vim

### Edit evironment setting

Add following command in `~/.vimrc`

```
set number
set ai                  " auto indenting
set history=100         " keep 100 lines of history
set ruler               " show the cursor position
syntax on               " syntax highlighting
colo desert
set hlsearch            " highlight the last searched term
filetype plugin on      " use the file type plugins

" When editing a file, always jump to the last cursor position
autocmd BufReadPost *
\ if ! exists("g:leave_my_cursor_position_alone") |
\ if line("'\"") > 0 && line ("'\"") <= line("$") |
\ exe "normal g'\"" |
\ endif |
\ endif
```

## R
When error messega like
```
During startup - Warning messages:
1: Setting LC_CTYPE failed, using "C"
2: Setting LC_COLLATE failed, using "C"
3: Setting LC_TIME failed, using "C"
4: Setting LC_MESSAGES failed, using "C"
5: Setting LC_PAPER failed, using "C"
[R.app GUI 1.50 (6126) x86_64-apple-darwin9.8.0]

WARNING: You're using a non-UTF8 locale, therefore only ASCII characters will work. Please read R for Mac OS X FAQ (see Help) section 9 and adjust your system preferences accordingly. [History restored from /Users/nemo/.Rapp.history]
```

open Terminal
write and run
```bash
defaults write org.R-project.R force.LANG en_US.UTF-8
```
close Terminal
Start R

## LaTeX
Visit [https://tug.org/mactex/](https://tug.org/mactex/) and install the package.

## SKIM
### Install
- Download and install from the [website](http://skim-app.sourceforge.net)

### User setting in [Preferences]-[Sync]
![](http://i.imgur.com/VbfLrco.png)

#### Realtime auto-refresh
- Ensble `Check for file changes`

#### Indicator
1. Choose preferred Tex editor in Preset roll down menu
2. Shift+Ctrl+click

## Latexmk
### User setting
#### Change the default pdf application to SKIM
- Add command in `~/.latexmkrc`
```bash
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
$pdf_previewer = 'open -a skim';
$clean_ext = 'bbl rel %R-blx.bib %R.synctex.gz';
```
- Compiling
```bash
latexmk -pvc -pdf filename.tex
```

[source](http://stackoverflow.com/questions/7899845/emacs-synctex-skim-how-to-correctly-set-up-syncronization-none-of-the-exi)