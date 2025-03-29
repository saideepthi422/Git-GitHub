## Git & GitHub Commands Cheat Sheet

# 1. Git Configuration

git config --global user.name "Your Name" – Set Git username

git config --global user.email "you@example.com" – Set Git email

git config --global color.ui auto – Enable colored output

git config --list – View all Git configurations

# 2. Initialize and Clone Repositories

git init – Initialize a new Git repository

git clone <repo_url> – Clone an existing repository

# 3. Staging and Committing Changes

git status – Check the status of working directory

git add <file> – Add a specific file to staging area

git add . – Add all changes to staging area

git commit -m "Your commit message" – Commit staged changes

git commit -am "Your commit message" – Add & commit in one step

# 4. Branching & Merging

git branch – List all branches

git branch <branch-name> – Create a new branch

git checkout <branch-name> – Switch to another branch

git checkout -b <branch-name> – Create and switch to a new branch

git merge <branch-name> – Merge a branch into the current branch

git branch -d <branch-name> – Delete a branch

# 5. Remote Repositories

git remote -v – View remote repositories

git remote add origin <repo_url> – Link local repo to remote

git push -u origin <branch-name> – Push changes to remote branch

git pull origin <branch-name> – Pull latest changes from remote

git fetch origin – Fetch latest changes without merging

git clone <repo_url> – Clone a remote repository

# 6. Undo & Reset Changes

git checkout -- <file> – Discard changes in working directory

git reset HEAD <file> – Unstage a file from staging area

git reset --hard HEAD~1 – Undo last commit permanently

git revert <commit-hash> – Create a new commit reversing changes

# 7. Viewing History & Logs

git log – View commit history

git log --oneline – View compact commit history

git show <commit-hash> – Show details of a specific commit

git diff – View unstaged changes

git diff --staged – View staged changes

git blame <file> – Show who made changes to a file

# 8. Stashing Changes

git stash – Save changes temporarily

git stash pop – Apply stashed changes and remove them from stash

git stash list – View stashed changes

git stash apply – Apply stashed changes without deleting them

git stash drop – Delete a specific stash

# 9. Tagging Versions

git tag – List all tags

git tag -a v1.0 -m "Version 1.0" – Create an annotated tag

git push origin --tags – Push tags to remote repository

git checkout v1.0 – Switch to a specific tag

# 10. Deleting Files

git rm # Remove a file and stage the deletion

git rm -r # Remove a folder and stage the deletion

# 11. Working with GitHub

gh auth login – Authenticate GitHub CLI

gh repo create <repo-name> – Create a new GitHub repository

gh repo clone <repo> – Clone a GitHub repository

gh issue list – List all issues in a repo

gh pr create – Create a pull request

gh release create <tag> – Create a GitHub release

## Explination of Git Commands

git init -Initializes a new Git repository in the current directory. 

git clone -Creates a local copy of a remote repository.

git status -Shows the current state of your working directory.

git add . -Adds all changed files to the staging area.

git commit -m "message" -Saves the changes with a commit message. 

git push origin main -Uploads committed changes to the remote repository. 

git pull origin main -Fetches and merges updates from the remote repository.

## Steps to Upload This to GitHub

git init git add . 

git commit -m "Added Git commands cheat sheet"

git branch -M main git remote add origin https://github.com/your-username/git-commands.git

git push -u origin main

# Your Git commands file is now on GitHub! 🎉

## This cheat sheet covers essential Git & GitHub commands.
