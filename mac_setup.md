
- Softwares(#Softwares)

#Softwares
##X-code

1. Install `Xcode` from `Mac App Store`
2. Install Command Line Tools 
```bash
xcode-select --install
```
(`Homebrew` will also automatically install **Command Line Tools** for Xcode.)

3. Accept Xcode Licence
```bash
sudo xcodebuild
```

##Homebrew

- `Homebrew` is a package manager for Mac OS X that can install a large number of packages. Simply, it is like `apt-get` in Linux system. 
- To install it simply launch a terminal and enter:
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
- Update check
```bash
brew update
```
- Status check
```bash
brew doctor
```
>위 명령어를 실행하면, homebrew 자동진단기능이 실행되며, homebrew 가 정상적으로 작동하기 위해 사용자가 수행해야 할 일을 지시해줍니다. 예를 들면, xQuartz 를 최신버젼으로 업그레이드 하라고 하던가, 또는 ‘brew *’ 를 실행해라 라는 형태로 구체적인 지침을 내려줍니다. python.org 에서 다운받은 python이 설치되어있는 경우 ‘/Library/…’ 에 설치되어있는 python 은 충돌을 야기할 수 있으니 삭제하라는 경고문이 발생합니다.

- Install **VIM** at first to edit a file in Terminal.
- In Home directory, make `~/.bash_profile` file with
```
export PATH=/usr/local/bin:$PATH
```
>위 명령어는 PATH 라는 변수에 /usr/local/bin:$PATH 를 할당하는 bash 명령어로 뒤에 붙은 :$PATH 는 기존의 PATH 를 뒤에 붙인다는 뜻입니다. 따라서 /usr/local/bin 폴더가 가장 우선순위가 높아지게 됩니다. brew 를 이용해 설치된 python 은 이 위치에 심볼릭링크가 형성되서 우선순위를 높게 해 주셔야 기본적인 실행이 가능합니다.


- Reload profile
```bash
source ~/.bash_profile
```

> Homebrew names the executable python2 so that you can still run the system Python via the executable python. [ref](http://python-docs.readthedocs.io/en/latest/starting/install/osx.html)
```bash
$ python -V   # system Python interpreter
$ python2 -V  # Homebrew installed Python 2 interpreter
$ python3 -V  # Homebrew installed Python 3 interpreter (if installed)
```

## Python 2.x
- Install
```bash
brew install python
```

## Python 3.x
- Install
```bash
brew install python3
```

## Python modules
*Use `pip` for *Python 2.x* and `pip3` for *Python 3.x* *

### Numpy
```bash
pip install numpy
```

### Scipy
```bash
brew install gcc #Scipy설치를 위한 사전 모듈. 이전에는 gfortran-이제는 gcc.
pip install scipy
```
### Matplotlib
```bash
brew install libpng
brew install freetype
pip install matplotlib
```

### Basemap
- Prerequirements (install what is missing)
```bash
brew install matplotlib
brew install numpy
brew install geos
brew install proj
pip install seaborn
```
- Download source file from
`https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/` [Link](https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/)

- Add Bash profile
```
export GEOS_DIR=/usr/local/Cellar/geos/3.6.2/
```

- Reload Bash profile
```bash
source ~/.bash_profile
```

- Go to Basemap directory and run
```bash
python setup.py install
```

- And test in `Python`
```python
import mpl_toolkits.basemap as bm
from mpl_toolkits.basemap import Basemap
```
- To test, `cd` to the `examples` directory and run `python simpletest.py`. To run all the examples (except those that have extra dependencies or require an internet connection), `execute python run_all.py`.

### Pyproj

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


### geopandas

- Install command
```bash
pip install geopandas
```

### shapely

- install command [ref](https://pypi.python.org/pypi/Shapely)
```bash
pip install shapely==1.6b2
```

### iPython
- Install in `Terminal`
```bash
pip install ipython[all]
```
- This `[all]` option will download and install IPython and its main optional dependencies:
	- jinja2, needed for the notebook
	- sphinx, needed for nbconvert
	- pyzmq, needed for IPython’s parallel computing features, qt console and notebook
	- pygments, used by nbconvert and the Qt console for syntax highlighting
	- tornado, needed by the web-based notebook
	- nose, used by the test suite
	- readline (on OS X) or pyreadline (on Windows), needed for the terminal

- *[Optional]* If an error occurs with the message `OSError: [Errno 13] Permission denied: '/usr/local/man'`, make the missing directoty and give the proper permission.
```bash
sudo mkdir -p /usr/local/man
sudo chown -R "$USER:admin" /usr/local/man
```
- To run IPython’s test suite, use the iptest command:
```bash
iptest
```

### pyenv
- Install in `Terminal`
```bash
brew install pyenv
```

## Jupyter notebook 

### Install Jupyter
- As an existing Python user, you may wish to install Jupyter using Python’s package manager, `pip`, instead of Anaconda. [Ref](https://jupyter.readthedocs.io/en/latest/install.html)

- First, ensure that you have the latest `pip`; older versions may have trouble with some dependencies:
```bash
pip install --upgrade pip
```
- Then install the Jupyter Notebook using:
```bash
pip install jupyter
```
(Use `pip3` if using legacy >Python 3.3)

### Kernel management
- Check the current Kernels
```bash
$ jupyter kernelspec list
Available kernels:
  python2    /usr/local/share/jupyter/kernels/python2
  $
```
- Add new kernels for Python 3 ([ref](http://antilibrary.org/1483))
```bash
python3 -m pip install ipykernel
python3 -m ipykernel install --user
```
- Check the current Kernels again
```bash
$ jupyter kernelspec list
Available kernels:
  python3    /Users/heetae/Library/Jupyter/kernels/python3
  python2    /usr/local/share/jupyter/kernels/python2
```
- Now, you are good to go and see two Kernels in Jupyter.

- other ways [1](http://blog.nacyot.com/articles/2015-05-08-jupyter-multiple-pythons/)

## VIM

- Install command
```bash
brew install macvim
```

- Add following command in `~/.vimrc` to customize

```
set number
set spell               " auto spell check
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
## Sublime Text
### Sepll checker by Google
- See [Google spell checker](https://github.com/noahcoad/google-spell-check/)
- Download and copy files to the packages folder of your `Sublime Text`. You can go via `Sublime Text`-`Preferences`-`Browse Packages...` menu.
- Copy files in the `User` folder. In my case, the location is `~/Library/Application Support/Sublime Text 3/Packages/User`
- Restart `Sublime Text`


## Gephi

### Gephi install
- Visit [http://gephi.org](http://gephi.org) and install
- Reference: [https://gephi.org/users/install/](https://gephi.org/users/install/)

### Error solusion regarding Java
- Currently, Java does not need to be installed separately.
>The current stable version of Gephi will only run with Java 7 or 8. On Mac OS X, Java is bundled with the application so it doesn't have to be installed separately. On Windows and Linux, the system must be equipped with Java. 
>[from https://gephi.org/users/requirements/](https://gephi.org/users/requirements/)

- If following error occurs, before install `Gephi`, install `Java Development Kit (JDK)`.
![Error](http://i.imgur.com/uvJ3Rw2.png)
![Image](http://i.imgur.com/ntbPQhi.png)

- `Gephi` supports Version 1.6.x and bofore(2017 now). Check your Java version if you already installed `Java`.
```bash
java -version
```
- You can install Java 1.6.x version from Apple website [http://support.apple.com/kb/DL1572?viewlocale=ko_KR](http://support.apple.com/kb/DL1572?viewlocale=ko_KR)
![image](http://i.imgur.com/lp9SiO3.png)

- If it does not run, add path command
```bash
jdkhome="/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home"
```
in `/Applications/Gephi.app/Contents/Resources/gephi/etc/gephi.conf`



## xQuartz
- Download the latest version from [http://xquartz.macosforge.org/landing/](http://xquartz.macosforge.org/landing/)
or install in Terminal
```bash
brew cask install xquartz
```

## Gnuplot
### Install with options 
- `XQuartz` required. Install `xQuartz` first.
- Use ==brew== rather than ==port==
```bash
brew install gnuplot --with-aquaterm --with-cairo --with-x11
```

##QGIS

### Standard install
- Download the package and install all frameworks included in order at [http://www.kyngchaos.com/software/qgis](http://www.kyngchaos.com/software/qgis)
- `Matplotlib`, `Numpy`, `GDAL` must be installed previously. (Included in the package.)

### When error occurs
- Follow the order and install what is missing (version can be changed)
	- `GDAL_Complete-1.10.dmg` at [http://www.kyngchaos.com/software/frameworks](http://www.kyngchaos.com/software/qgis)
	- `FreeType_Framework-2.4.10-1.dmg` at [http://www.kyngchaos.com/software/frameworks](http://www.kyngchaos.com/software/frameworks)
	- `matplotlib-1.3.0-3.dmg` at [http://www.kyngchaos.com/software/python](http://www.kyngchaos.com/software/python)
	- `QGIS-2.0.1-4-Lion.dmg` at [http://www.kyngchaos.com/software/qgis](http://www.kyngchaos.com/software/qgis)

- Error can occur even though you already installed, e.g., `Matplotlib`. Then, just reinstall the package following the order.


## LaTex environment
### LaTeX (MacTEX)
- Visit [https://tug.org/mactex/](https://tug.org/mactex/) and install the package.

### SKIM
- Download and install from the [http://skim-app.sourceforge.net](http://skim-app.sourceforge.net)

- User setting in [Preferences]-[Sync]
![](http://i.imgur.com/VbfLrco.png)
- **Realtime auto-refresh**: Ensble `Check for file changes`
- Choose preferred Tex editor in `Preset` roll down menu
- `Shift+Ctrl+click`: Call the sentnce at the editor

### Latexmk
- (User setting: Change the default pdf application of MAC OS to `SKIM`)Net necessary 
- Add command in `~/.latexmkrc`
```
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
$pdf_previewer = 'open -a skim';
$clean_ext = 'bbl rel %R-blx.bib %R.synctex.gz';
```
- Compiling command
```bash
latexmk -pvc -pdf filename.tex
```
[Ref.](http://stackoverflow.com/questions/7899845/emacs-synctex-skim-how-to-correctly-set-up-syncronization-none-of-the-exi)

## R
- Download from [https://www.r-project.org](https://www.r-project.org)
- When error comes as
```bash
During startup - Warning messages:
1: Setting LC_CTYPE failed, using "C"
2: Setting LC_COLLATE failed, using "C"
3: Setting LC_TIME failed, using "C"
4: Setting LC_MESSAGES failed, using "C"
5: Setting LC_PAPER failed, using "C"
[R.app GUI 1.50 (6126) x86_64-apple-darwin9.8.0]
WARNING: You're using a non-UTF8 locale, therefore only ASCII characters will work. Please read R for Mac OS X FAQ (see Help) section 9 and adjust your system preferences accordingly. [History restored from /Users/nemo/.Rapp.history]
```

- then open `Terminal` and run
```bash
defaults write org.R-project.R force.LANG en_US.UTF-8
```

# *Mac OS customize*
## Shortcut for input language

In [System Preferences]-[Keyboard]-[Shortcut] 

-[Input Source]
- Select the previous input source: `^Space (Deactivate)`
- Select next source in Input menu: `⌘Space (Activate)`

-[Spotlight]
- Show Spolight search: `^Space`
- Show Finder search window: `^⌥Space`

In [System Preferences]-[Siri]
- Keyboard Shortcut: `Off`
- To prevent delay
- [Ref](macnews.tistory.com/4609)

## NTFS accessibility

### Tuxera (Paied Third Party App, for Toshiba HDD users)

- [Download Package file (for Sierra)](https://www.tuxera.com/mac/toshiba/tuxerantfs_toshiba_2016.1_2016-11-11_050024.dmg) ([Ref](http://www.jycommunications.co.kr/bbs/board.php?bo_table=6_3&wr_id=17&page=0), Check if newer version is available.)
- Connect Toshiba External HDD
- Run the package
- Restart your Mac

### Fuse (Free method by terminal)

#### Install Fuse
- Requires `Homebrew`. Install it if your Mac does not have it installed.
- Download and install the latest release of FUSE for macOS from [http://osxfuse.github.io](http://osxfuse.github.io). 
or by `brew install Caskroom/cask/osxfuse`. You will need at least version 3.0.
- Install NTFS-3G ([Ref](https://github.com/osxfuse/osxfuse/wiki/NTFS-3G))
```bash
brew install ntfs-3g
```
- Disable System Integrity Protection (SIP) in Recovery Mode (Press `⌘Command`+`R` after rebooting) by
```bash
csrutil disable
```
- Reboot and run commands ([Ref 1](https://www.howtogeek.com/236055/how-to-write-to-ntfs-drives-on-a-mac/), [Ref 2](https://gist.github.com/bjorgvino/f24e5c079b92f921b765) 
```bash
sudo mv /sbin/mount_ntfs /sbin/mount_ntfs.original
sudo ln -s /usr/local/sbin/mount_ntfs /sbin/mount_ntfs
```
- After all, enable SIP again in recovery mode.
```bash
csrutil enable
```

#### Uninstall Fuse
- To undo your changes and uninstall everything, you’ll need to first disable System Integrity Protection. After you do, run the following commands:
```bash
sudo rm /sbin/mount_ntfs
sudo mv /sbin/mount_ntfs.original /sbin/mount_ntfs
brew uninstall ntfs-3g
```
Verified with ls -l /sbin/mount_ntfs*

## Change Dock hiding
### Speed of animation

- To make the Dock instantly leap back into view when it’s needed, rather than slide,
```bash
defaults write com.apple.dock autohide-time-modifier -int 0;killall Dock
```

- if you’d like the animation for the dock to reappear to last for a split-second,
```bash
defaults write com.apple.dock autohide-time-modifier -float 0.7;killall Dock
```
the number like `0.7` will decide the speed.

- To revert back to the default sliding effect
```bash
defaults delete com.apple.dock autohide-time-modifier;killall Dock
```

### Delay time
- This option will remove the delay since it is '0'.
```bash
defaults write com.apple.Dock autohide-delay -float 0 && killall Dock
```

- To revert back to the default delay
```bash
defaults delete com.apple.Dock autohide-delay && killall Dock
```

## Keyboard plist change
### Disable Rootless
1. Reboot and press key `Command + R` while it is rebooting to activate recovery mode
2. Run `Terminal` from `Utility`
3. Run in the terminal
```bash
csrutil disable
```

### Copy plist file
4. Copy `Keyboard-en.plist` to 
`/System/Library/Input Methods/PressAndHold.app/Contents/PlugIns/PAH_Extension.appex/Contents/Resources/` (High Sierra)

### Enable Rootless
5. Reboot and enable
```bash
csrutil enable
```

## SSH and VNC port change
### Change port numbers
1. Open the terminal window

2. Enter:
```bash
sudo nano /etc/services
```

3. Enter the root password, it will open the ‘services’ file. Be careful to avoid modify anything else.

4. Press `Ctrl+W` and search "`ssh`".

5. You will find to lines assigned to port 22. Something like this:
> ssh	22/udp	# SSH Remote Login Protocol
ssh	22/tcp	# SSH Remote Login Protocol

6. Change the number 22 in both cases to 2222 or whaterver the port you want to use.

7. Press `Ctrl+X` and then enter `Y` to accept saving the file.

8. Do the same for VNC

### Reload SSH
Now we need to restart SSH. 

9. Enter the following command to stop it:
```bash
sudo launchctl unload /System/Library/LaunchDaemons/ssh.plist
```

10. Now enter the following command to start SSH again:
```bash
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist
```

That’s it, you must be ready to go. 
You can verify if is working by trying to access locally, just enter:
```bash
ssh localhost -p 2222
```
