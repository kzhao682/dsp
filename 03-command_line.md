# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

* pwd: show current working directory path
* mkdir: creating a directory
* rmdir: deleting a directory
* touch: creating an empty file
* rm: deleting a file
* mv: rename or move a file or directory
* ls -a: listing hidden files
* cp: copying a file from one directory to another
* less: page through a file
* cat: print the whole file
* find: find files
* grep: find things inside files
* man: read a manual page
* exit: exit the shell
* $ | $: pipes left command to right
* $ < $: redirect input of right to left
* $ > $: redirect input of left to right
* $ >> $: append output of left to file on right

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

* ls: list directory contents
* ls -a: include entries whose names begin with a dot (.)
* ls -l: list in long format
* ls -lh: list in long format using unit suffixes: Byte, Kilobyte, Megabyte, Gigabyte, Terabyte, Petabyte, etc.
* ls -lah: list all entries including names that begin with a dot (.) in long format using unit suffixes
* ls -t: list sorted directory contents in long format by time modified
* ls -Glp: list directory in long format with colorized output and a slash ('/') after each directory


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

* ls -1: list each directory content on a line
* ls -c: list directory contents by timestamp
* ls -i: list inode for each directory content
* ls -m: list directory contents as comma-separated list
* ls -u: list directory contents by file access time

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` is used to construct argument lists and execute utility. It reads space, tab, newline, and end-of-file delimited strings from standard input and executes utility with strings as arguments.

The following is an example of xargs in order to display stdin in rows of two:
```
$echo 1 2 3 4 5 6 | xargs -n 2
1 2
3 4
5 6
```

 

