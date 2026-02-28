> **A comprehensive data-driven analysis for tourism accommodations. Sentiment analysis dashboard analyzing 6,947+ Google Maps reviews from 4,342 accommodations across 5 European cities **

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Google Places API](https://img.shields.io/badge/API-Google%20Places-green.svg)](https://developers.google.com/maps/documentation/places)

---

## 📊 Overview

Tourism Rating Sentiment & City Benchmark is a sentiment analysis that tracks accommodation reviews across European cities. Using Google Places API, natural language processing, and data visualization, it provides actionable insights for tourism stakeholders, hospitality managers, and destination marketing organizations.

### 🎯 Key Features

- **Multi-City Comparative Analysis** - Benchmark Budapest, Krakow, Tallinn, Riga, and Sofia
- **Sentiment Analysis** - Automated categorization of reviews (positive/negative/neutral)
- **Category Classification** - Analyzes 8 key dimensions: staff, cleanliness, location, room quality, price, breakfast, amenities, accessibility
- **Nationality Insights** - Identifies top 6-8 visitor nationalities per market
- **Gender Analysis** - Demographics breakdown by category
- **Geo-Visualization** - Interactive maps showing accommodation density and review volume
- **Automated Insights** - Generates top 12 market insights automatically
- **Real-Time Dashboard** - Beautiful, interactive web interface with European design

---

## 🚀 Live Demo

![Dashboard Screenshot](docs/images/dashboard-preview.png)


---

## 🛠️ Technology Stack

- **Data Collection**: Google Places API, Python 3.8+
- **Analysis**: NumPy, Pandas, Custom NLP algorithms
- **Sentiment Analysis**: Keyword-based (Multilingual European language support)
- **Visualization**: Chart.js, Leaflet Maps, HTML5/CSS3
- **Backend**: FastAPI, SQLite
- **Deployment**: Python HTTP Server, Docker-ready

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Google Places API key ([Get one free](https://console.cloud.google.com/))
- ~500MB free disk space

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/tourism-rating-benchmark.git
cd tourism-rating-benchmark

# Install dependencies
pip install -r requirements-simple.txt

# Add your Google API key
# Edit collect_multi_city.py and add your key

# Run data collection (takes 4-6 hours)
python collect_multi_city.py

# Analyze the data
python analyze_snapshot.py

# Start the dashboard
python -m http.server 8000
# Open http://localhost:8000/snapshot_dashboard.html
```

---

## 📖 Methodology

### Data Collection

- **Grid-based search**: 2km grid pattern ensures complete city coverage
- **Sample size**: 200-400 properties per city (size-dependent)
- **Reviews per property**: Up to 5 (Google API limitation)
- **Deduplication**: Ensures no property counted twice

### Analysis Methods

- **Sentiment**: Keyword-based analysis with multilingual European language support
- **Categories**: 8 predefined categories with extensive keyword matching
- **Nationality**: Derived from review language
- **Gender**: Name-based heuristic detection (~70% accuracy)

### Limitations

- Only recent reviews (Google provides latest 5 per property)
- Snapshot analysis (no historical trends)
- Gender detection approximate
- Nationality inferred from language

---

## 📊 Use Cases

### Tourism Boards
- Identify market strengths and weaknesses
- Compare performance against competing destinations
- Track sentiment trends
- Optimize marketing strategies

### Hospitality Managers
- Benchmark against competition
- Identify improvement areas
- Understand visitor demographics
- Monitor reputation metrics

### Researchers
- Academic studies on tourism sentiment
- Cross-cultural hospitality analysis
- Destination competitiveness research
- Data-driven policy recommendations


We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

ű
