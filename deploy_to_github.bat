@echo off
echo ╔══════════════════════════════════════════════════════════════╗
echo ║          🚀 Deploy to GitHub - Quick Setup                   ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git is not installed. Please install Git first.
    echo Download from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git is installed
echo.

REM Initialize git if not already initialized
if not exist .git (
    echo 📦 Initializing Git repository...
    git init
    echo ✅ Git initialized
) else (
    echo ✅ Git repository already exists
)
echo.

REM Add all files
echo 📝 Adding files to Git...
git add .
echo ✅ Files added
echo.

REM Commit
echo 💾 Creating commit...
set /p commit_message="Enter commit message (or press Enter for default): "
if "%commit_message%"=="" set commit_message=Initial commit for deployment
git commit -m "%commit_message%"
echo ✅ Commit created
echo.

REM Set main branch
echo 🌿 Setting main branch...
git branch -M main
echo ✅ Main branch set
echo.

REM Add remote
echo 🔗 Adding remote repository...
set /p repo_url="Enter your GitHub repository URL (e.g., https://github.com/username/repo.git): "
git remote remove origin 2>nul
git remote add origin %repo_url%
echo ✅ Remote added
echo.

REM Push to GitHub
echo 🚀 Pushing to GitHub...
git push -u origin main
if errorlevel 1 (
    echo.
    echo ⚠️  Push failed. This might be because:
    echo    1. Repository doesn't exist on GitHub
    echo    2. You need to authenticate
    echo    3. Remote URL is incorrect
    echo.
    echo 💡 Create the repository on GitHub first, then run this script again.
    pause
    exit /b 1
)

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║          ✅ SUCCESS! Code pushed to GitHub                   ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 📋 Next Steps:
echo    1. Go to render.com and sign up
echo    2. Click "New +" → "Web Service"
echo    3. Connect your GitHub repository
echo    4. Follow the DEPLOYMENT_GUIDE.md for detailed instructions
echo.
pause
