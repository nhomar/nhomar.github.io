Generator (Blog) [![Build Status](https://travis-ci.org/nhomar/nhomar.github.io.svg?branch=generator)](https://travis-ci.org/nhomar/nhomar.github.io)
Master (Generated Pages) [![Build Status](https://travis-ci.org/nhomar/nhomar.github.io.svg?branch=master)](https://travis-ci.org/nhomar/nhomar.github.io)

Nhomar’s Blog
---

Here the blog based on [Pelican](http://getpelican.com) which is serving my personal blog.

The main point here it that I was looking for a a blog system where comply with this feature:

1. Can be versiones with git.
2. Written on ReestructuredText, markdown or both.
3. Have a system to version only the rst/md file line by line.
4. Written in python.
5. With twitter bootstrap css.
6. Minimal mantainance, no servers, no databases.

Then here is what I got.

1. In the branch “generator” you will find the blog itself, using “pelican”.
2. In the branch “master” you will find the auto-deployed files by travis.
3. In the .travis.yml you will find the configuration to achieve that.
4. All the information is mixing some manuals from the official wiki for pelican.

The theme is based on pelican-bootstrap3 improved with the corporative colors
of my company using bootswatch structure.

Hacking This for your own purpose.
---

1. Fork the repository.
2. Save change the name of the repository to username.github.io.
3. Clean all the “content” folder.
4. Follow the manual of [pelican](https://docs.getpelican.com) to create and set your enviroment.

Creating Content.
---

1. Create an article or page under the folder “content”.
2. Create the [metadata](http://docs.getpelican.com/en/3.4.0/content.html#file-metadata) for that file.
3. Write [rst](http://docutils.sourceforge.net/docs/user/rst/quickref.html)

TODO:

1. Put here all commands to fork and improve.
2. Create a little script to create a new content or document myself how pelican does without manually set the metadata.
3. Multi Lang.

##The content of my blog is licenced under [Creative Commons Attribution-ShareAlike 4.0 International](https://github.com/idleberg/Creative-Commons-4.0-Markdown/blob/master/licenses/by-sa.markdown)
