# GitHub Repository Setup Instructions

## 📦 Preparing Your Repository

Follow these steps to create and publish your EU Tourism Sentiment Analysis project on GitHub.

## Step 1: Create GitHub Repository

1. **Go to GitHub** and sign in: https://github.com
2. **Click** the "+" icon (top right) → "New repository"
3. **Repository details:**
   - Name: `eu-tourism-sentiment`
   - Description: `Sentiment analysis dashboard analyzing 6,947+ Google Maps reviews from 4,342 accommodations across 5 European cities`
   - Visibility: **Public** (to share with others)
   - ✅ Check "Add README file" (we'll replace it)
   - License: MIT License
4. **Click** "Create repository"

## Step 2: Organize Your Local Files

Create the following folder structure on your computer:

```
eu-tourism-sentiment/
├── README.md                          ← Main documentation
├── LICENSE                            ← MIT License
├── requirements.txt                   ← Python dependencies
├── .gitignore                        ← Files to ignore
│
├── scripts/
│   ├── google_places_scraper.py      ← Your scraper script
│   ├── sentiment_analysis.py         ← Your analysis script
│   └── generate_dashboard.py         ← Dashboard generator
│
├── data/
│   ├── city_analysis.json            ← Processed stats (can share)
│   └── detailed_insights.json        ← Category analysis (can share)
│   └── .gitkeep                      ← Keep folder in git
│
├── dashboard/
│   └── index.html                    ← Your final dashboard
│
└── docs/
    ├── API_SETUP.md                  ← API setup guide
    ├── DATA_COLLECTION.md            ← Methodology docs
    └── GITHUB_SETUP.md               ← This file
```

**Important:** Do NOT include `all_cities_data.json` (too large - 25MB+)

## Step 3: Initialize Git Repository

Open terminal/command prompt in your project folder:

```bash
# Navigate to your project folder
cd path/to/eu-tourism-sentiment

# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: EU Tourism Sentiment Analysis project"

# Connect to GitHub
git remote add origin https://github.com/YOUR_USERNAME/eu-tourism-sentiment.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Add Large Files to Git LFS (Optional)

If you want to include the large data file:

```bash
# Install Git LFS
git lfs install

# Track large JSON files
git lfs track "*.json"
git add .gitattributes

# Add and commit
git add data/all_cities_data.json
git commit -m "Add large data file with LFS"
git push
```

## Step 5: Create Repository Topics

On GitHub repository page:
1. Click ⚙️ next to "About"
2. Add topics:
   - `sentiment-analysis`
   - `google-maps-api`
   - `python`
   - `data-visualization`
   - `tourism`
   - `nlp`
   - `dashboard`
   - `europe`
3. Click "Save changes"

## Step 6: Enable GitHub Pages (Optional)

To host your dashboard online:

1. Go to **Settings** → **Pages**
2. Source: **Deploy from branch**
3. Branch: **main** → folder: **/ (root)**
4. Click **Save**
5. Your dashboard will be live at:
   `https://YOUR_USERNAME.github.io/eu-tourism-sentiment/dashboard/`

## Step 7: Create Releases

Tag major versions:

```bash
# Create a tag
git tag -a v1.0.0 -m "Initial release - 5 cities analyzed"

# Push tags
git push --tags
```

On GitHub:
1. Go to **Releases** → **Create a new release**
2. Choose tag: **v1.0.0**
3. Release title: **v1.0.0 - Initial Release**
4. Description:
   ```markdown
   ## 🎉 First Release
   
   Analysis of 6,947 reviews from 5 European cities:
   - Budapest, Hungary
   - Krakow, Poland
   - Tallinn, Estonia
   - Riga, Latvia
   - Sofia, Bulgaria
   
   ### Features
   - Interactive dashboard with Google Maps integration
   - Sentiment analysis across 5 categories
   - Nationality-based insights
   - Multi-city comparison
   ```
5. Click **Publish release**

## Step 8: Add Repository Badges

Add these to your README.md:

```markdown
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-success)
![Reviews](https://img.shields.io/badge/Reviews-6,947-orange)
![Cities](https://img.shields.io/badge/Cities-5-blue)
```

## Step 9: Create a Good First Issue

Help others contribute:

1. Go to **Issues** → **New issue**
2. Title: "Add support for new city"
3. Label: `good first issue`, `enhancement`
4. Description:
   ```markdown
   We'd like to expand analysis to more cities!
   
   **To do:**
   - [ ] Choose a new European city
   - [ ] Collect reviews using the scraper
   - [ ] Run analysis
   - [ ] Update README with new statistics
   
   **Good cities to add:**
   - Prague, Czech Republic
   - Vienna, Austria
   - Warsaw, Poland
   ```

## Step 10: Share Your Project

### On LinkedIn
See the LinkedIn post template below!

### On Twitter/X
```
🌍 Just released an open-source sentiment analysis dashboard analyzing 6,947+ Google Maps reviews from 5 European cities!

Built with #Python, Google Maps API, and NLP

✨ Interactive maps
📊 Category analysis  
🌐 Nationality insights

Check it out: [your-github-link]

#DataScience #Tourism #OpenSource
```

### On Reddit
Post in:
- r/dataisbeautiful
- r/Python
- r/datasets
- r/travel

## Maintenance

### Regular Updates
```bash
# Pull latest changes
git pull

# Make changes
# ... edit files ...

# Commit and push
git add .
git commit -m "Update: Added new visualizations"
git push
```

### Protect Your API Key

**NEVER commit your API key!**

Instead, use environment variables:

```python
import os

API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
```

Set in terminal:
```bash
export GOOGLE_MAPS_API_KEY="your_key_here"
```

## Need Help?

- [GitHub Docs](https://docs.github.com)
- [Git LFS](https://git-lfs.github.com)
- [GitHub Pages](https://pages.github.com)

---

**Next:** Share your project with the world using the LinkedIn post template!
