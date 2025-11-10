# 🚀 Deployment Guide - Vercel (Frontend) + Render (Backend)

This guide will help you deploy your Hair & Scalp Disease Detection application with:
- **Backend (Django + ML Model)** on **Render**
- **Frontend (Static files)** served via **Vercel** or **Render**

---

## 📋 Prerequisites

1. **GitHub Account** - Your code must be in a GitHub repository
2. **Render Account** - Sign up at [render.com](https://render.com)
3. **Vercel Account** (Optional) - Sign up at [vercel.com](https://vercel.com)

---

## 🎯 Deployment Strategy

### Option 1: Full Stack on Render (Recommended - Simpler)
Deploy both frontend and backend on Render as a single web service.

### Option 2: Split Deployment
- Backend API on Render
- Frontend on Vercel (requires API configuration)

---

## 🔧 Option 1: Deploy Everything on Render (Recommended)

### Step 1: Prepare Your Repository

1. **Push your code to GitHub:**
```bash
cd required_files
git init
git add .
git commit -m "Initial commit for deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 2: Create Render Account & Service

1. Go to [render.com](https://render.com) and sign up
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure the service:

**Basic Settings:**
- **Name:** `hair-scalp-detector`
- **Region:** Choose closest to your users
- **Branch:** `main`
- **Root Directory:** Leave empty or set to `required_files`
- **Runtime:** `Python 3`

**Build & Deploy:**
- **Build Command:**
```bash
pip install -r requirements_production.txt && cd minor && python manage.py collectstatic --no-input && python manage.py migrate
```

- **Start Command:**
```bash
cd minor && gunicorn minor.wsgi:application
```

**Environment Variables:**
Click **"Advanced"** and add these environment variables:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | Generate a random string (click "Generate") |
| `DJANGO_SETTINGS_MODULE` | `minor.settings_production` |
| `ALLOWED_HOSTS` | `.onrender.com` |

### Step 3: Add PostgreSQL Database (Optional but Recommended)

1. In Render Dashboard, click **"New +"** → **"PostgreSQL"**
2. Name it `hair-scalp-db`
3. Choose **Free** plan
4. Click **"Create Database"**
5. Copy the **Internal Database URL**
6. Go back to your Web Service → **Environment**
7. Add new variable:
   - **Key:** `DATABASE_URL`
   - **Value:** Paste the Internal Database URL

### Step 4: Deploy!

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for the build to complete
3. Your app will be live at: `https://your-app-name.onrender.com`

### Step 5: Update Settings

After deployment, update `settings_production.py`:

```python
ALLOWED_HOSTS = [
    'your-app-name.onrender.com',  # Replace with your actual Render URL
    'localhost',
    '127.0.0.1',
]

CSRF_TRUSTED_ORIGINS = [
    'https://your-app-name.onrender.com',  # Replace with your actual Render URL
]
```

Commit and push changes - Render will auto-deploy.

---

## 🔧 Option 2: Split Deployment (Advanced)

### Backend on Render

Follow **Option 1** steps above for backend deployment.

### Frontend on Vercel

**Note:** This approach is more complex because Django templates need the backend.

1. **Separate Static Files:**
   - Extract all HTML templates to a separate frontend folder
   - Convert Django templates to static HTML
   - Update API endpoints to point to Render backend

2. **Deploy to Vercel:**
```bash
cd frontend
vercel
```

3. **Configure CORS:**
   Update `settings_production.py`:
```python
CORS_ALLOWED_ORIGINS = [
    "https://your-app.vercel.app",
]
```

**⚠️ Warning:** This approach requires significant refactoring to separate frontend from Django templates.

---

## 🔐 Security Checklist

Before going live, ensure:

- [ ] `DEBUG = False` in production settings
- [ ] Strong `SECRET_KEY` (use environment variable)
- [ ] `ALLOWED_HOSTS` configured correctly
- [ ] HTTPS enabled (automatic on Render)
- [ ] Database backups enabled
- [ ] Environment variables set (not hardcoded)
- [ ] Static files collected and served properly

---

## 📊 Post-Deployment

### Monitor Your App

1. **Render Dashboard:**
   - View logs: Click your service → **"Logs"**
   - Monitor metrics: **"Metrics"** tab
   - Check health: **"Events"** tab

2. **Test Your App:**
   - Visit your deployed URL
   - Test image upload
   - Test prediction functionality
   - Test camera capture
   - Check all pages load correctly

### Common Issues & Solutions

**Issue: Static files not loading**
```bash
# Solution: Run collectstatic
cd minor
python manage.py collectstatic --no-input
```

**Issue: Database errors**
```bash
# Solution: Run migrations
cd minor
python manage.py migrate
```

**Issue: 502 Bad Gateway**
- Check logs in Render dashboard
- Verify `gunicorn` is installed
- Check start command is correct

**Issue: CORS errors**
- Add frontend domain to `CORS_ALLOWED_ORIGINS`
- Verify `corsheaders` is installed
- Check middleware order

---

## 🔄 Continuous Deployment

Render automatically deploys when you push to GitHub:

```bash
# Make changes
git add .
git commit -m "Update feature"
git push origin main
# Render will auto-deploy in ~5 minutes
```

---

## 💰 Cost Breakdown

### Free Tier (Render)
- ✅ Web Service: Free (spins down after 15 min inactivity)
- ✅ PostgreSQL: 90 days free, then $7/month
- ✅ 750 hours/month free

### Paid Tier (Recommended for Production)
- 💵 Web Service: $7/month (always on)
- 💵 PostgreSQL: $7/month
- **Total: $14/month**

---

## 📚 Additional Resources

- [Render Documentation](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)

---

## 🆘 Need Help?

If you encounter issues:

1. Check Render logs: Dashboard → Your Service → Logs
2. Verify environment variables are set correctly
3. Test locally with production settings:
   ```bash
   export DJANGO_SETTINGS_MODULE=minor.settings_production
   python manage.py runserver
   ```
4. Check GitHub repository is up to date

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Web service created and configured
- [ ] Environment variables set
- [ ] Database created (if using PostgreSQL)
- [ ] Build completed successfully
- [ ] App is accessible via Render URL
- [ ] All features tested on production
- [ ] HTTPS working
- [ ] Static files loading correctly
- [ ] Database migrations applied
- [ ] Monitoring set up

---

**🎉 Congratulations! Your app is now live!**

Share your deployed URL: `https://your-app-name.onrender.com`
