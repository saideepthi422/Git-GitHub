# Git Commands Cheat Sheet
#Written by :-Saideepthi
## Basic Git Commands
git init                     # Initialize a new Git repository  
git clone <repo-url>         # Clone an existing repository  
git status                   # Show the status of changes  
git add .                    # Add all modified files to staging  
git commit -m "message"      # Commit changes with a message  
git push origin main         # Push commits to the remote repository  
git pull origin main         # Pull the latest changes from remote  
## Working with Branches Git Commands
git branch                   # List all branches  
git branch <branch-name>     # Create a new branch  
git checkout <branch-name>   # Switch to another branch  
git checkout -b <branch-name> # Create and switch to a new branch  
git merge <branch-name>      # Merge a branch into the current branch  
git branch -d <branch-name>  # Delete a branch  
# Viewing commit history Git Commands
git log                      # Show commit history  
git log --oneline            # Show commit history in a single line format  
git blame <file>             # Show who modified each line in a file  
##  Undoing changes
git reset HEAD~1             # Undo the last commit but keep changes  
git checkout -- <file>       # Discard local changes in a file  
git revert <commit-hash>     # Create a new commit to undo changes  
## Working with Remote Repositories
git remote -v                # Show remote repositories  
git remote add origin <repo-url> # Add a remote repository  
git push origin <branch-name> # Push changes to remote branch  
git pull origin <branch-name> # Pull latest changes from remote  
## Stashing Changes
git stash                    # Temporarily save changes  
git stash pop                # Restore the most recent stashed changes  
git stash list               # Show all stashed changes  
## Deleting Files
git rm <file>                # Remove a file and stage the deletion  
git rm -r <folder>           # Remove a folder and stage the deletion  

# Explination of Git Commands
git init	-Initializes a new Git repository in the current directory.
git clone <repo-url>	-Creates a local copy of a remote repository.
git status	-Shows the current state of your working directory.
git add .	-Adds all changed files to the staging area.
git commit -m "message"	-Saves the changes with a commit message.
git push origin main	-Uploads committed changes to the remote repository.
git pull origin main	-Fetches and merges updates from the remote repository.

## Steps to Upload This to GitHub
git init
git add .
git commit -m "Added Git commands cheat sheet"
git branch -M main
git remote add origin https://github.com/your-username/git-commands.git
git push -u origin main

## Your Git commands file is now on GitHub! 🎉
