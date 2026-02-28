# 🌍 EU Tourism Sentiment Analysis

A comprehensive sentiment analysis dashboard analyzing **6,947+ real Google Maps reviews** from **4,342 accommodations** across 5 major European cities.

![Dashboard Preview](https://img.shields.io/badge/Status-Complete-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Reviews Analyzed](https://img.shields.io/badge/Reviews-6,947-orange)
![Cities](https://img.shields.io/badge/Cities-5-green)

## 📊 Project Overview

This project provides deep insights into tourist accommodation experiences across Central and Eastern European capitals through automated review collection, sentiment analysis, and interactive data visualization.

### 🎯 Key Features

- **Real-time Google Maps Integration**: Interactive maps showing 4,342+ accommodation locations
- **Sentiment Analysis**: AI-powered analysis of review text to extract category-specific feedback
- **Multi-City Comparison**: Side-by-side comparison of 5 European cities
- **Category Performance Tracking**: Analysis across 5 key categories (Location, Cleanliness, Staff, Food, Amenities)
- **Demographic Insights**: Top 5 reviewer nationalities per city
- **Interactive Dashboard**: Professional HTML/JavaScript dashboard with Chart.js visualizations

### 🏙️ Cities Analyzed

| City | Country | Properties | Reviews | Avg Rating |
|------|---------|------------|---------|------------|
| **Budapest** | 🇭🇺 Hungary | 1,350 | 2,417 | 3.98/5 |
| **Krakow** | 🇵🇱 Poland | 977 | 1,519 | 4.16/5 |
| **Tallinn** | 🇪🇪 Estonia | 492 | 703 | 3.87/5 |
| **Riga** | 🇱🇻 Latvia | 779 | 1,022 | 3.90/5 |
| **Sofia** | 🇧🇬 Bulgaria | 744 | 1,286 | 3.90/5 |

## 🛠️ Technology Stack

- **Python 3.8+**: Data collection and analysis
- **Google Maps API**: Review and location data retrieval
- **Chart.js**: Interactive data visualizations
- **HTML/CSS/JavaScript**: Frontend dashboard
- **Natural Language Processing**: Keyword-based sentiment analysis

## 📁 Project Structure

```
eu-tourism-sentiment/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── scripts/
│   ├── google_places_scraper.py      # Collects reviews from Google Places API
│   ├── sentiment_analysis.py          # Analyzes sentiment and extracts insights
│   └── generate_dashboard.py          # Creates the HTML dashboard
│
├── data/
│   ├── all_cities_data.json           # Raw scraped data (not in repo - too large)
│   ├── city_analysis.json             # Processed statistics
│   └── detailed_insights.json         # Category and nationality analysis
│
├── dashboard/
│   └── index.html                     # Interactive dashboard
│
└── docs/
    ├── API_SETUP.md                   # Google Maps API setup guide
    ├── DATA_COLLECTION.md             # Data collection methodology
    └── ANALYSIS_METHODOLOGY.md        # Sentiment analysis approach
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Cloud account with Maps API enabled
- Billing enabled on Google Cloud (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/eu-tourism-sentiment.git
   cd eu-tourism-sentiment
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Maps API**
   - Follow the guide in `docs/API_SETUP.md`
   - Enable Places API in Google Cloud Console
   - Create an API key
   - Add your API key to the scripts

### Usage

#### 1. Collect Data (Optional - pre-collected data included)

```bash
python scripts/google_places_scraper.py
```

This will collect reviews from accommodations in all 5 cities. **Note**: This may take 3-4 hours and will use Google Maps API credits.

#### 2. Run Sentiment Analysis

```bash
python scripts/sentiment_analysis.py
```

Processes reviews to extract:
- Category-specific scores (Location, Cleanliness, Staff, Food, Amenities)
- Sentiment distribution (Positive/Neutral/Negative)
- Reviewer nationality detection

#### 3. Generate Dashboard

```bash
python scripts/generate_dashboard.py
```

Creates the interactive HTML dashboard with all visualizations.

#### 4. View Dashboard

Simply open `dashboard/index.html` in your web browser.

## 📊 Analysis Methodology

### Data Collection

- **Source**: Google Places API (official, legal method)
- **Timeframe**: Reviews collected in February 2026
- **Review Limit**: Up to 5 reviews per property (API limitation)
- **Total Properties**: 4,342 accommodations
- **Total Reviews**: 6,947 reviews

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

Simple pattern matching on reviewer names:
- Character sets (Cyrillic, Latin with diacritics)
- Common name patterns
- Language indicators

## 📈 Key Insights

### Top Performing City
**Krakow, Poland** leads with:
- ⭐ 4.16/5 average rating
- 💚 78.3% positive sentiment
- 🏆 Highest scores in most categories

### Category Champions
- **Best Location**: Budapest (4.12/5)
- **Best Staff**: Budapest & Krakow (4.01/5)
- **Best Food**: Budapest & Krakow (4.01/5)
- **Best Cleanliness**: Krakow (data in analysis)

### Reviewer Demographics
- Majority: International travelers (70-75%)
- Secondary: Spanish/Portuguese speakers (15-20%)
- Others: Slavic, German/Austrian, English-speaking

## 🎨 Dashboard Features

The interactive dashboard provides:

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

## 🔒 Data Privacy & Ethics

- ✅ Uses official Google Places API (legal and approved)
- ✅ Only public review data is collected
- ✅ No personal information stored beyond public usernames
- ✅ Complies with Google's Terms of Service
- ✅ Data used for research and analysis purposes only

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Ideas for Contribution
- Add more cities to the analysis
- Implement advanced NLP (BERT, transformer models)
- Add time-series analysis
- Create predictive models
- Improve nationality detection accuracy
- Add more visualization types

## 📧 Contact

For questions or collaboration opportunities, please open an issue on GitHub.

## 🙏 Acknowledgments

- Google Maps Platform for providing the data API
- Chart.js for visualization library
- All the travelers who shared their accommodation experiences

## 📚 Citation

If you use this project in your research, please cite:

```bibtex
@software{eu_tourism_sentiment_2026,
  title = {EU Tourism Sentiment Analysis Dashboard},
  year = {2026},
  author = {Your Name},
  url = {https://github.com/YOUR_USERNAME/eu-tourism-sentiment}
}
```

---

**⭐ If you find this project useful, please consider giving it a star!**
