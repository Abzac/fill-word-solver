# Fill word solver

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://travis-ci.com/Abzac/guss.svg?branch=master)](https://travis-ci.com/Abzac/guss)
<a href="https://black.readthedocs.io/en/stable/?badge=stable"><img alt="Documentation Status" src="https://readthedocs.org/projects/black/badge/?version=stable"></a>
<a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

<img alt="Fill Word" src="https://raw.githubusercontent.com/Abzac/fill-word-solver/master/fill-word.jpeg">

# Intro

Helps to solve a "Fill Word" puzzle.


# What is "Fill word"?
"Fill words", also known as the "Hungarian crossword" puzzles - is a puzzle in which you want to find all the words inscribed in a square grid. 
At first glance, the letters are written randomly, but in fact, they are part of a word.

Words can be bent in any direction at a right angle but do not intersect with each other. 
To find the words you need to identify each of them with the mouse from the first letter to the last.
After all the words in "Fill Word" unraveled, empty cells should not remain. 
When a word is selected correctly, it will appear in the lower list and obscured in the grid "Fill words".

You can find much of them here: <a href="https://en.grandgames.net/filvordy/">Grand Fill Words Collection</a>


# Usage example

You may see usage example in `src/solver.py`

```
# cd src
# python3 solver.py

2019-07-11 02:24:06,828 - root - INFO - Loaded 175025 words
2019-07-11 02:24:06,828 - root - INFO - Building word index...
2019-07-11 02:24:09,406 - root - INFO - Searching...
2019-07-11 02:24:09,409 - root - INFO - Found 21 words
2019-07-11 02:24:09,410 - root - INFO - Found words: 21

==== ландшафт (1) ====
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    т    #    #    #
#    #    ф    а    ш    д
#    #    #    л    а    н

==== агроном (1) ====
#    #    #    #    а    #
#    #    #    #    г    м
#    #    #    #    р    о
#    #    #    #    о    н
#    #    #    #    #    #
#    #    #    #    #    #

==== огород (1) ====
#    #    #    #    #    #
о    г    о    #    #    #
#    о    р    #    #    #
#    д    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== шалфей (2) ====
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    й    #    #    ш    #
#    е    ф    л    а    #

#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    й    #    а    ш    #
#    е    ф    л    #    #

==== город (1) ====
#    #    #    #    #    #
#    г    о    #    #    #
#    о    р    #    #    #
#    д    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== между (1) ====
м    е    ж    д    #    #
#    #    #    у    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== алан (1) ====
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    а    #    #
#    #    #    л    а    н

==== брод (1) ====
#    #    #    #    #    #
#    #    #    #    #    #
#    о    р    б    #    #
#    д    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== бром (1) ====
#    #    #    #    #    #
#    #    #    #    #    м
#    #    #    б    р    о
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== горб (2) ====
#    #    #    #    #    #
#    г    о    #    #    #
#    #    р    б    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

#    #    #    #    #    #
#    г    #    #    #    #
#    о    р    б    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== гром (1) ====
#    #    #    #    #    #
#    #    #    #    г    м
#    #    #    #    р    о
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== грош (1) ====
#    #    #    #    #    #
#    #    #    #    г    #
#    #    #    #    р    #
#    #    #    #    о    #
#    #    #    #    ш    #
#    #    #    #    #    #

==== джем (1) ====
м    е    ж    д    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== дуга (1) ====
#    #    #    д    а    #
#    #    #    у    г    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== морг (1) ====
#    #    #    #    #    #
#    #    #    #    г    м
#    #    #    #    р    о
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== ноша (2) ====
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    о    н
#    #    #    #    ш    #
#    #    #    #    а    #

#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    о    н
#    #    #    а    ш    #
#    #    #    #    #    #

==== омег (1) ====
м    е    #    #    #    #
о    г    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== сорт (1) ====
#    #    #    #    #    #
#    #    #    #    #    #
с    о    р    #    #    #
#    #    т    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== трос (1) ====
#    #    #    #    #    #
#    #    #    #    #    #
с    о    р    #    #    #
#    #    т    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== утро (2) ====
#    #    #    #    #    #
#    #    #    #    #    #
#    о    р    #    #    #
#    #    т    у    #    #
#    #    #    #    #    #
#    #    #    #    #    #

#    #    #    #    #    #
#    #    о    #    #    #
#    #    р    #    #    #
#    #    т    у    #    #
#    #    #    #    #    #
#    #    #    #    #    #

==== шала (2) ====
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    а    ш    #
#    #    #    л    а    #

#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    #    #    #
#    #    #    а    ш    #
#    #    #    л    а    #
```

# Algorithm

This library implements special "Recursive Dict" data structure (which is something like a 
<a href="https://en.wikipedia.org/wiki/Trie" title="Trie - Wikipedia">Trie data structure</a> or "prefix search index"),
effectively searching all dictionary words and their possible places, using 
<a href="https://en.wikipedia.org/wiki/Depth-first_search">Depth-First Search algorithm</a> from each position.

     
# Algorithm work example

Given a dictionary of known English words:
```
find
finding
fix
run
```
Yes, it's pretty small, but it's only for the purposes of the example.

Let's try to find all the words from the dictionary in the matrix!

**Step -1.** Build word index with all the words we know at all. It would look something like:
```python
d = {
    'f': {
        'i': {
            'n': {
                'd': {
                    'i': {
                        'n': {
                            'g': {
                                None: {},  # mark meaning that `finding` ends here
                            },
                        },
                    None: {},  # mark meaning that `find` ends here
                    }
                }  
            },
            'x': {
                None: {},  # mark meaning that `find` ends here
            }
        }
    },
    'r': {
        'u': {
            'n': {
                None: {},  # mark meaning that `run` ends here
            }
        }
    }
} 
```
OK! We now have the effective word index (`RecursiveDict` in terminology of my code)

**Step 0**
Given matrix
```
f i x
d n r
k n u
```
Let's try to find all the words in it!


**Step 1**
1. Starting from letter _"f"_ in the top-left corner.
```
f * *
* * *
* * *
```

2. Let's take a look inside the recursive dictionary. Hm... From letter _"f"_ we can consume letters _"i"_ and _"x"_. OK.
```python
list(d['f'].keys()) == ['i', 'x']
```

3. Now we try to move to all possible directions, right and down, as for now. We have a letter _"d"_ down, and letter _"i"_ to the left
```
f i *
d * *
* * *
```

4. So, we can't go down, because we can't consume letter _"d"_ after _"f"_ (it's because no words start with _"fd"_).
```python
'x' not in d['f']
```

5. But we can _try_, just _try_ to consume letter _"i"_ next, because some of the dictionary words start with _"fi"_.
```python
'i' not in d['f']
```


6. So we go left from _"f"_, now we have _"f"_ and _"i"_ in out path. Now we have prefix _"fi"_
```
f i *
_ * *
* * *
```

```python
d = f['i']
```

7. OK. Let's move next. We can move right and down (but we can't go back in Depth-First Search)
```
f i x
_ n *
* * *
```

8. Okay, we have both _"x"_ and _"n"_ now in _"d"_, so as DFS is recursive we have to split our search in two:
one we'll try to explore the way down and another would go to the right. Let's only take a look for the move to the right.

9. Well, now we in cell with _"x"_ having a path to it like "f" -> "i" -> "x".
```
f i x
_ * *
* * *
```
Our dictionary has a special mark (`None` keyword) meaning that this is the end of some word.
So we can add the word `fix` to the resulting found words list.

10. But we can not stop yet! We have to move next because we could possibly have some words starting with _"fix"_, but longer, like "fixing".
Unfortunately, in this example, we can not find more words, because the only explorable way, "fixr" is not an English word, nor a prefix for some English word. 

So, our search is ended here. This algorithm would find a word _"run"_ as well, but we would skip it in this example.
 

# Dictionaries
All dictionaries are loaded automatically. 
You may place any word dictionaries (in UTF-8) in `data/dictionaries` folder. 

Included `zdf.txt` is the <a href="https://en.wikipedia.org/wiki/Andrey_Zaliznyak">Andrey Zaliznyak's</a> words dictionary 
got from <a href="http://www.speakrus.ru/dict/">here</a> (but encoded to UTF-8).

Included `engmix.txt` is English words dictionary got from <a href="http://www.gwicks.net/dictionaries.htm">here</a> (but without some strange words in the end).
