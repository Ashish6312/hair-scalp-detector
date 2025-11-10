@echo off
echo ╔══════════════════════════════════════════════════════════════════════════╗
echo ║          📱 Mobile App Setup - Hair & Scalp AI                           ║
echo ╚══════════════════════════════════════════════════════════════════════════╝
echo.

echo 📋 Step 1: Installing required packages...
pip install cairosvg pillow
echo ✅ Packages installed
echo.

echo 🎨 Step 2: Generating app icons...
python generate_icons.py
echo ✅ Icons generated
echo.

echo 📦 Step 3: Committing changes...
git add .
git commit -m "Add PWA mobile app support with icons"
echo ✅ Changes committed
echo.

echo 🚀 Step 4: Pushing to GitHub...
git push origin main
echo ✅ Pushed to GitHub
echo.

echo ╔══════════════════════════════════════════════════════════════════════════╗
echo ║                    ✅ MOBILE APP SETUP COMPLETE!                         ║
echo ╚══════════════════════════════════════════════════════════════════════════╝
echo.
echo 📱 Your app is now installable as a mobile app!
echo.
echo 🌐 Live URL: https://hair-scalp-detector.onrender.com
echo.
echo 📋 Next Steps:
echo    1. Wait 3-5 minutes for Render to deploy
echo    2. Visit the URL on your phone
echo    3. Tap "Install" when prompted
echo    4. App will be added to your home screen!
echo.
echo 📖 For detailed instructions, see: 📱_MOBILE_APP_GUIDE.md
echo.
pause
