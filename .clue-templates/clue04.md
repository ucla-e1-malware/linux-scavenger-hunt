### Clue 4: Moving Day ###

Welcome! I hope you are viewing this file in `less`. As a reminder:

- Use arrow keys to move up and down
- Use space bar to jump down a full page
- Hit `q` to exit once you are done reading

#### Making Space ####

We've been exploring the directories that already exist on the computer. But
what if we want to make our own folders and files? The first thing we need to
do is create a new directory. First go home by running just: `cd`. Then do

    mkdir saved-clues

What we're going to do is save off all the clues we find in a separate folder
that we created with `mkdir` (make directory). Since the README is clue 1 we
don't need to worry about it. If you've been writing down all the clue
locations, this next part should be easy.

#### Stop Copying Me ####

Let's copy all of the clues we've found so far to our saved-clues folder:

    cp linux-scavenger-hunt/clues/12345/clue saved-clues/clue2
    cp linux-scavenger-hunt/clues/[YOUR_CLUE_NUMBER]/clue saved-clues/clue3

This copies (`cp`) each clue to the new folder and gives them new names.
We can also leave out the file name and do this:

    cp linux-scavenger-hunt/clues/12345/clue saved-clues/
    cp linux-scavenger-hunt/clues/[YOUR_CLUE_NUMBER]/clue saved-clues/

By ending in a `/`, this tells `cp` to keep the same file name. However, since they are
both named `clue`, the second file would overwrite the first, which is not what we want. 

#### Keep Your Options Open ####

Linux commands often have options that change how they behave. For instance,
compare `ls -l` to ordinary `ls`. Here the `-l` is an option. You can group 
options together like this

    ls -lah
    
The best way to find out about options is the manpage or google.

#### Moving On ####

Now let's say we don't like the folder name `saved-clues`. We can just move
(`mv`) it:

    mv saved-clues [pick a new name]

Now do an `ls` to see the results of the move. Be careful with `mv`: you can
easily overwrite an existing folder! Let's find a way to avoid that.

#### Find Clue 5 ####

Read the man page for `mv` and find an
option to prevent overwriting. That option is your next hint.

Note: use the shorthand version of the option - it should be a single letter.
