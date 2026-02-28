# 🌍 EU Tourism Sentiment Analysis

A comprehensive sentiment analysis dashboard analyzing **6,947+ real Google Maps reviews** from **4,342 accommodations** across 5 major European cities.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Reviews Analyzed](https://img.shields.io/badge/Reviews-6,947-orange)
![Cities](https://img.shields.io/badge/Cities-5-green)
![License](https://img.shields.io/badge/License-MIT-success)

## 📊 Project Overview

This project provides deep insights into tourist accommodation experiences across Central and Eastern European capitals through automated review collection, sentiment analysis, and interactive data visualization.

### 🏙️ Cities Analyzed

| City | Country | Properties | Reviews | Avg Rating |
|------|---------|------------|---------|------------|
| **Budapest** | 🇭🇺 Hungary | 1,350 | 2,417 | 3.98/5 |
| **Krakow** | 🇵🇱 Poland | 977 | 1,519 | 4.16/5 |
| **Tallinn** | 🇪🇪 Estonia | 492 | 703 | 3.87/5 |
| **Riga** | 🇱🇻 Latvia | 779 | 1,022 | 3.90/5 |
| **Sofia** | 🇧🇬 Bulgaria | 744 | 1,286 | 3.90/5 |

## 🎯 Key Features

- **Real-time Google Maps Integration**: Interactive maps showing 4,342+ accommodation locations
- **Sentiment Analysis**: AI-powered analysis of review text to extract category-specific feedback
- **Multi-City Comparison**: Side-by-side comparison of 5 European cities
- **Category Performance Tracking**: Analysis across 5 key categories (Location, Cleanliness, Staff, Food, Amenities)
- **Demographic Insights**: Top 5 reviewer nationalities per city with category-specific scores
- **Interactive Dashboard**: Professional HTML/JavaScript dashboard with Chart.js visualizations

## 🚀 Live Demo

**Dashboard:** [https://botondboros.github.io/Tourism-Sentiment-Analysis/dashboard/](https://botondboros.github.io/Tourism-Sentiment-Analysis/dashboard/)

## 🛠️ Technology Stack

- **Python 3.8+**: Data collection and analysis
- **Google Maps Places API**: Review and location data retrieval
- **Chart.js**: Interactive data visualizations
- **HTML/CSS/JavaScript**: Frontend dashboard
- **Natural Language Processing**: Keyword-based sentiment analysis

## 📈 Key Insights

### Top Performing City
**Krakow, Poland** leads with:
- ⭐ 4.16/5 average rating
- 💚 78.3% positive sentiment
- 🏆 Highest scores in most categories

### Category Champions
- **Best Location**: Budapest (4.13/5)
- **Best Staff**: Krakow & Budapest (4.0+/5)
- **Best Food**: Krakow & Budapest (4.0+/5)

### Reviewer Demographics
- Majority: English-speaking travelers (80-87%)
- Secondary: Spanish speakers (3-6%)
- Others: French, Italian, German

## 📁 Project Structure

```
Tourism-Sentiment-Analysis/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── dashboard/
│   └── index.html              # Interactive dashboard
│
├── scripts/
│   ├── google_places_scraper.py
│   └── sentiment_analysis.py
│
├── docs/
│   ├── API_SETUP.md
│   └── DATA_COLLECTION.md
│
└── data/
    └── .gitkeep
```

## 🎨 Dashboard Features

### Overview Page
- City selection cards with key metrics
- Quick stats for each destination

### Multi-City Comparison
- Side-by-side category performance
- Reviewer nationality distribution
- Rating trends across cities

### Individual City Pages
- Interactive Google Maps with property locations
- Sentiment distribution (pie chart)
- Rating distribution (bar chart)
- Category performance (horizontal bar chart)
- Top 5 nationalities (table & breakdown)
- Nationality × Category analysis (grouped bar chart)

## 📊 Data Analysis Methodology

### Data Collection
- **Source**: Google Places API (official, legal method)
- **Total Properties**: 4,342 accommodations
- **Total Reviews**: 6,947 reviews
- **Collection Time**: ~4 hours

### Sentiment Analysis
Reviews are analyzed using keyword-based NLP:

**Category Keywords:**
- **Location**: central, walk, nearby, transport, metro
- **Cleanliness**: clean, dirty, spotless, hygiene, fresh
- **Staff**: staff, service, helpful, friendly, reception
- **Food**: breakfast, meal, restaurant, delicious, tasty
- **Amenities**: pool, gym, spa, wifi, parking, room

**Sentiment Classification:**
- Ratings 4-5: Positive
- Rating 3: Neutral
- Ratings 1-2: Negative

### Nationality Detection
Language detection from review text:
- Uses language field from Google Maps API
- Keyword-based detection for review text
- Supports: English, Spanish, French, German, Italian

## 🔒 Data Privacy & Ethics

- ✅ Uses official Google Places API (legal and approved)
- ✅ Only public review data is collected
- ✅ No personal information stored beyond public usernames
- ✅ Complies with Google's Terms of Service
- ✅ Data used for research and analysis purposes only

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Maps Platform for providing the data API
- Chart.js for visualization library
- All the travelers who shared their accommodation experiences

## 📧 Contact

For questions or collaboration opportunities, please open an issue on GitHub.

---

**⭐ If you find this project useful, please consider giving it a star!**

Built with ❤️ using Python, Google Maps API, and JavaScript
