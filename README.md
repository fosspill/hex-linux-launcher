# hex-linux-launcher

Table of Contents
=================

   * [hex-linux-launcher](#hex-linux-launcher)
      * [Requirements](#requirements)
      * [How to install](#how-to-install)
      * [Dependency installation](#dependency-installation)
         * [Ubuntu/Debian based](#ubuntudebian-based)
         * [Arch based](#arch-based)
      * [Current status](#current-status)
      * [WHY ARE THE VERSION NUMBERS SO CONFUSING](#WHY-ARE-THE-VERSION-NUMBERS-SO-CONFUSING)


<img src="https://i.imgur.com/aRYhEVJ.gif" width="500"  />

## Requirements
- Python 3
- PyQt5
- FeedParser

## How to install
- Make sure that you have Python 3
- Install pyqt5 and feedparser
- Grab the most recent release version, or clone the repository and launch hex-linux-launcher
```
git clone https://github.com/fosspill/hex-linux-launcher.git
cd hex-linux-launcher
./hex-linux-launcher
```

## Dependency installation
### Ubuntu/Debian based
` sudo apt-get install python3-feedparser python3-pyqt5 `
### Arch based
` sudo pacman -S python-feedparser python-pyqt5 `

## Current status
It's now working fully. Check the issues to see if there are any missing functions or bugs.

## WHY ARE THE VERSION NUMBERS SO CONFUSING
The linux version might be behind the main version of the game, which means that the patch notes might be slightly too early in the launcher.

At the same time, the version number provided by Hex Entertainment seems to be wrong and doesn't match what the binary provided actually contains. Until that's fixed we'll have to deal with confusing version numbers!

