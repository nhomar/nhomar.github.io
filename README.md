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

A. Fork the repository.
B. Save change the name of the repository to username.github.io.
C. Clean all the “content” folder.
D. Follow the manual of [pelican](https://docs.getpelican.com) to create and set your enviroment.

TODO: Put here all commands to fork and improve.
