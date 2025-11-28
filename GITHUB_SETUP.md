# 🚀 GitHub Setup Guide

This guide will help you push your Fourier Transform Explorer app to GitHub.

## Step 0: Configure Git Identity (Required First Step)

Before making commits, configure your Git identity:

```bash
# Set your name and email (use your GitHub email if you have one)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Or set it only for this repository:
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

## Step 1: Make Initial Commit

The repository has been initialized and files are staged. Make your first commit:

```bash
git commit -m "Initial commit: Fourier Transform Explorer app"
```

## Step 2: Create GitHub Repository

1. **Go to GitHub**: Visit [github.com](https://github.com) and sign in
2. **Create New Repository**:
   - Click the "+" icon in the top right
   - Select "New repository"
   - Repository name: `Fourier-Transform-Explorer` (or your preferred name)
   - Description: "Interactive multi-page Streamlit app for learning Fourier Transform"
   - Choose **Public** or **Private**
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

## Step 3: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Fourier-Transform-Explorer.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 4: Verify

Visit your repository on GitHub to confirm all files are uploaded.

## Alternative: Using SSH

If you prefer SSH (and have SSH keys set up):

```bash
git remote add origin git@github.com:YOUR_USERNAME/Fourier-Transform-Explorer.git
git branch -M main
git push -u origin main
```

## Future Updates

After making changes to your code:

```bash
# Stage changes
git add .

# Commit changes
git commit -m "Description of your changes"

# Push to GitHub
git push
```

## Quick Reference

```bash
# Check status
git status

# See what files changed
git diff

# View commit history
git log

# Pull latest changes (if working from multiple locations)
git pull
```

## Troubleshooting

### If you get "remote origin already exists":
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/Fourier-Transform-Explorer.git
```

### If you need to set your Git identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### If push is rejected:
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

**Need help?** Check GitHub's documentation or the Git documentation.

