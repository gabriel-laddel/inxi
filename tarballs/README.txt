README for svn/tarballs directory.

This directory is intended to be a repository of older .gz/.tar.gz files 
from svn trunk. Tarballs contain the following (as of version 1.8.34, 
pre 1.8 the .gz is just inxi itself):

inxi
inxi.1 (non gzipped man page)
inxi.1.gz (gz, with: gzip -c -9 inxi.1 > inxi.1.gz)
inxi.changelog (contains all main changes, but NOT all svn commits)
inxi.tar.gz (all of the above)

Note that the current trunk tarball/inxi file names never change, so distro 
maintainers can always grab the same file without having to poke around.

-- trunk is always by definition, the current stable live files. 

-- Only one command to grab the currrent tarball (inxi.tar.gz):
   wget -Nc https://inxi.googlecode.com/svn/trunk/inxi.tar.gz 
   This will never change, so you can set your update / packaging scripts
   to use that url always.

-- not all trunk svn changes will be tarballed as sometimes there are frequent
   changes. No tarballs exist prior to version 1.8.0 because there was no man 
   page or tarball etc.

-- I will try to keep the last tarball version of each major version release 
   (like 1.9.19 as the last of the 1.9 series) if I remember.

Important: the only version of inxi that is supported is the latest current 
svn trunk release. No issue reports or bug reports will be accepted for 
anything other than current svn trunk.

The version number follows these guidelines:
Using example 1.8.14-6

The first digit(s), "1", is a major version, and almost never changes. Only 
a huge milestone, or if inxi reaches 1.9.xx, when it will simply move up to 
2.0.0 just to keep it clean, would cause a change. 

The second digit(s), "8", means a new real feature has been added. Not a 
tweaked existing feature, an actual new feature, which usually also has a new 
argument option letter attached. 

The third, "14", is for everything small, can cover bug fixes, tweaks to 
existing features to add support for something, pretty much anything where you
want the end user to know that they are not up to date. 

The fourth, "6", is extra information from Tarball maintainer, when either the 
third digit has not changed, but there is a change or a patch comes out, 
and the Tarball maintainer has time to pack the change. I don't usually use 
this last one.
 
This 'tarballs' directory provides a bumpy and incomplete history of inxi 
releases (but it's better than nothing), and serves as a repository of 
older inxi versions. Note that inxi did not have .tar.gz until the man 
page was added, version 1.8.2. Before that, the .gz is just the gzip file
of inxi itself, nothing more. inxi_1.8.34.tar.gz is the first version that
includes the inxi.1 and inxi change log files as well.
 
Users must always use the most recent version of inxi to get support!

### EOF ###
