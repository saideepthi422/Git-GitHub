# Git Installation Guide

## Install Git on Ubuntu

### Step 1: Update the Package List
```bash
sudo apt update
```

### Step 2: Install Git
```bash
sudo apt install git -y
```

### Step 3: Verify Installation
```bash
git --version
```

### Step 4: Configure Git (Optional)
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
---

## Install Git on Windows

### Step 1: Download Git for Windows
- Download the installer from the official [Git website](https://git-scm.com/downloads).

### Step 2: Run the Installer
- Open the downloaded `.exe` file and follow the installation instructions.
- Keep the default settings unless you have specific preferences.

### Step 3: Verify Installation
- Open **Command Prompt** or **Git Bash** and run:
```bash
git --version
```

### Step 4: Configure Git (Optional)
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

---

## Verify Git Configuration
```bash
git config --list
```

## Uninstall Git (If Needed)

### Ubuntu:
```bash
sudo apt remove git -y
```

### Windows:
- Go to **Control Panel > Programs > Uninstall a program** and remove Git.

---

Now Git is installed and ready to use on both Ubuntu and Windows! 🚀

