# Very simple Spyware 

## Compatability
This is made for Linux systems with the bash shell.
It should work on other distros just fine but it's only tested on Ubuntu.

## What information can be stolen?
All files that are accessed by sudo nano.

## How does this work?

1. virus.py must be executed with super user rights,
2. this will than edit bash.bashrc (a file that is executed whenever a new bash shell is opened) to include a change that re-links nano to a malicious file (nnano.sh).
3. nano will mean ~/SomeSpyware/nnano.sh as soon as the shell restarts.
4. this program ain't complete yet, sorry

This is obviously a minimalistic and bad spyware that anybody can write within an hour or less and is meant for demonstrating only.
