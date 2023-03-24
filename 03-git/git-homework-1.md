# Git Homework 1

## Exercise 1

Install git and clone this repo.

    $ git clone https://github.com/fisher85/backender-roadmap.git

## Exercise 2

Set your _user name_ and _email address_.

    $ git config --global user.name "John Doe"
    $ git config --global user.email johndoe@example.com

## Exercise 3

Create file, commit changes, undo changes.

    $ git status
    $ touch exercise3.txt
    $ git status
    $ git add exercise3.txt
    $ git status
    $ git diff --staged
    $ git reset HEAD exercise3.txt
    $ git status
    $ git add exercise3.txt
    $ git status
    $ git commit -m "Friday"
    $ git status
    $ git log
    $ git commit --amend -m "Friday 13"
    $ git log
    $ git reset HEAD~1
    $ git log
    $ git status

## Exercise 4

Find commit message by hash `438c6c10d7b196c1a301b81e2e5355883550d3d9`.

    $ git show 438
    $ git show 438c
    $ git show 438c6c10d7b196c1a301b81e2e5355883550d3d9
    $ git log 438c6c10 -1

## Exercise 5

**Try to mess something up in the repository.** Delete all files, change content, rewrite history in remote repository.
