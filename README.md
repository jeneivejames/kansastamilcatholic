# Kansas Tamil Catholic Community Website

A beautiful community website for the Kansas Tamil Catholic Community featuring Mass schedules, events, gallery, and contact information.

## 🚀 Deploy to Vercel (No Authentication Required)

This website is ready to deploy on Vercel as a public website with **no authentication required**.

### Option 1: Deploy via Vercel Dashboard (Easiest)

1. **Download the project folder** from Databricks workspace:
   - Download all files from `/Users/jeneive.dhanapalan@gmail.com/kansas-tamil-catholic-community/`
   - Or use the files directly from this folder

2. **Go to Vercel**:
   - Visit [vercel.com](https://vercel.com)
   - Sign up or log in (free account)

3. **Import Project**:
   - Click "Add New" → "Project"
   - Upload your project folder
   - Vercel will auto-detect the Flask app

4. **Deploy**:
   - Click "Deploy"
   - Wait 1-2 minutes
   - Your site will be live at: `https://your-project-name.vercel.app`

### Option 2: Deploy via GitHub (Recommended for Updates)

1. **Create a GitHub repository**:
   - Go to [github.com](https://github.com)
   - Create a new repository (e.g., `kansas-tamil-catholic`)

2. **Upload files to GitHub**:
   - Upload all files from this folder
   - Commit and push

3. **Connect Vercel to GitHub**:
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New" → "Project"
   - Import from GitHub
   - Select your repository

4. **Deploy**:
   - Vercel will automatically deploy
   - Every time you push to GitHub, Vercel will auto-redeploy

### Option 3: Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Navigate to project folder
cd kansas-tamil-catholic-community

# Deploy
vercel

# Follow the prompts
# Your site will be live!
```

## 📁 Project Structure

```
kansas-tamil-catholic-community/
├── app.py                    # Flask application (Backend)
├── app.yaml                  # Databricks app config (not needed for Vercel)
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel configuration
├── templates/
│   └── index.html           # Website HTML
└── static/
    └── images/              # Upload your photos here
        ├── priests_group.jpg
        ├── mother_mary.jpg
        ├── community_gathering.jpg
        ├── mass_celebration.jpg
        └── youth_group.jpg
```

## ✏️ Update Content

Edit `app.py` to update:
- **Mass Schedule** (lines 8-26)
- **Events** (lines 29-60)
- **Contact Info** (lines 93-99)

Then redeploy:
- If using GitHub: Push changes → Auto-redeploys
- If using CLI: Run `vercel --prod`
- If using dashboard: Re-upload files

## 📸 Add Photos

1. Place your photos in `static/images/` folder
2. Name them:
   - `priests_group.jpg`
   - `mother_mary.jpg`
   - `community_gathering.jpg`
   - `mass_celebration.jpg`
   - `youth_group.jpg`
3. Redeploy

## 🌐 Current Content

### Mass Schedule
- **Sunday, October 18, 2026** at St. Michael's Church, Leawood, KS

### Events
- **Family Rosary** - Every Weekend in October
- **Christmas Program 2026** - December 24 (Planning)

### Contact
- **Coordinator**: John
- **Phone**: (913) 461-2244
- **WhatsApp**: Direct connect button
- **Location**: St. Michael's Church, Leawood, KS

## 🎨 Features

✅ **No authentication required** - Public website
✅ **Responsive design** - Mobile, tablet, desktop
✅ **Bilingual** - Tamil & English
✅ **Beautiful design** - Traditional Catholic colors (blue, gold)
✅ **WhatsApp integration** - Direct connect button
✅ **Photo gallery** - Showcase community moments
✅ **Event calendar** - Keep community informed
✅ **Mass schedule** - Never miss Tamil Mass

## 💡 Tips

- Vercel provides a **free domain**: `your-project.vercel.app`
- You can add a **custom domain** in Vercel settings
- Site is **automatically HTTPS** (secure)
- **Free hosting** with generous limits
- **Auto-deploys** when connected to GitHub

## 📞 Support

For questions, contact: John - (913) 461-2244

---

**May God bless the Kansas Tamil Catholic Community!** 🙏✝️