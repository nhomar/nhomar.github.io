#!/usr/bin/env bash
BRANCH=master #Usage of master is mandatory for username and organization pages, try gh-pages for project pages.
TARGET_REPO=nhomar/nhomar.github.io.git
PELICAN_OUTPUT_FOLDER=output
PELICAN_BOOTSTRAP_BRANCH="master"
PELICAN_BOOTSTRAP_REPO="nhomar/pelican-bootstrap3.git"

echo -e "Testing travis-encrypt"
echo -e "$VARNAME"

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to Github Pages\n"
    if [ "$TRAVIS" == "true" ]; then
        git config --global user.email "travis@travis-ci.org"
        git config --global user.name "Travis"
        git clone --quiet --branch=$PELICAN_BOOTSTRAP_BRANCH https://github.com/$PELICAN_BOOTSTRAP_REPO $HOME/pelican-bootstrap3 > /dev/null
    fi
    #using token clone gh-pages, or master branch
    git clone --quiet --branch=$BRANCH https://${GH_TOKEN}@github.com/$TARGET_REPO built_website > /dev/null
    #go into directory and copy data we're interested in to that directory
    cd built_website
    rsync -rv --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* .
    #add, commit and push files
    git add -f .
    git commit -m "Travis build $TRAVIS_BUILD_NUMBER pushed to Github Pages"
    git push -fq origin $BRANCH > /dev/null
    echo -e "Deploy completed\n"
fi


