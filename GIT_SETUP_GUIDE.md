# Git Setup Guide for OpenGeoTech

This guide will help you set up Git for your OpenGeoTech package and connect it to the GitHub repository.

## Prerequisites

- Git installed on your system
- GitHub account
- Access to the OpenGeotechnical organization on GitHub

## Initial Git Setup

1. **Initialize Git in your project directory**

   If you haven't already initialized Git in your project, run:

   ```bash
   git init
   ```

2. **Add your files to Git**

   Stage all your files for the initial commit:

   ```bash
   git add .
   ```

3. **Create your first commit**

   ```bash
   git commit -m "Initial commit of OpenGeoTech package"
   ```

## Connecting to GitHub Repository

1. **Add the remote repository**

   Connect your local repository to the GitHub repository:

   ```bash
   git remote add origin https://github.com/OpenGeotechnical/opengeotech.git
   ```

2. **Verify the remote connection**

   Ensure the remote was added correctly:

   ```bash
   git remote -v
   ```

   You should see:
   ```
   origin  https://github.com/OpenGeotechnical/opengeotech.git (fetch)
   origin  https://github.com/OpenGeotechnical/opengeotech.git (push)
   ```

3. **Push your code to GitHub**

   Push your local repository to GitHub:

   ```bash
   git push -u origin main
   ```

   Note: If your default branch is named `master` instead of `main`, use:
   ```bash
   git push -u origin master
   ```

## Working with Branches

1. **Create a new branch for feature development**

   ```bash
   git checkout -b feature/new-feature-name
   ```

2. **Push a new branch to GitHub**

   ```bash
   git push -u origin feature/new-feature-name
   ```

## Common Git Workflow

1. **Pull latest changes before starting work**

   ```bash
   git pull origin main
   ```

2. **Create a branch for your changes**

   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make your changes and commit them**

   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

4. **Push your changes to GitHub**

   ```bash
   git push -u origin feature/your-feature
   ```

5. **Create a Pull Request on GitHub**

   Go to the GitHub repository page and create a pull request from your branch to the main branch.

## Using SSH Instead of HTTPS (Optional)

If you prefer using SSH instead of HTTPS for GitHub authentication:

1. **Generate SSH keys** (if you don't have them already)

   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. **Add your SSH key to your GitHub account**

   Copy your public key and add it to your GitHub account settings.

3. **Change the remote URL to use SSH**

   ```bash
   git remote set-url origin git@github.com:OpenGeotechnical/opengeotech.git
   ```

## Troubleshooting

- **Authentication issues**: Make sure you have the correct permissions to the repository
- **Push rejected**: Pull the latest changes before pushing
- **Merge conflicts**: Resolve conflicts in the affected files, then add and commit them 