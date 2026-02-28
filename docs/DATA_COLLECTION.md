# Data Collection Methodology

## Overview

This document describes how data was collected for the EU Tourism Sentiment Analysis project.

## Data Source

**Google Places API** - Official Google Maps data source

### Why Google Places API?

✅ **Legal**: Complies with Google's Terms of Service  
✅ **Reliable**: Official, well-maintained data  
✅ **Comprehensive**: Includes reviews, ratings, locations  
✅ **Structured**: Easy to parse and analyze  

## Collection Process

### 1. City Selection

Five Central/Eastern European capitals were selected based on:
- Tourism popularity
- English review availability
- Geographic diversity
- Data availability

**Selected Cities:**
- Budapest, Hungary
- Krakow, Poland
- Tallinn, Estonia
- Riga, Latvia
- Sofia, Bulgaria

### 2. Search Parameters

```python
search_params = {
    'location': city_coordinates,
    'radius': 5000,  # 5km from city center
    'type': 'lodging'  # Hotels, hostels, B&Bs
}
```

### 3. Data Collection Script

The `google_places_scraper.py` script:

1. **Geocodes** each city name to coordinates
2. **Searches** for accommodations within radius
3. **Retrieves** details for each property:
   - Name, address, coordinates
   - Overall rating
   - Total review count
   - Up to 5 recent reviews per property
4. **Saves** to JSON file

### 4. Review Limitations

**Google Places API limits:**
- Maximum 5 reviews per property
- Reviews sorted by "most relevant" (Google's algorithm)
- Not guaranteed to be most recent

**Mitigation:**
- Collected from many properties (4,342 total)
- Diverse sample across cities
- Still statistically significant (6,947 reviews)

## Data Structure

### Raw Data Format

```json
{
  "Budapest": [
    {
      "place_id": "ChIJ...",
      "name": "Hotel Example",
      "address": "Street 123, Budapest",
      "rating": 4.5,
      "total_ratings": 1234,
      "lat": 47.4979,
      "lng": 19.0402,
      "reviews": [
        {
          "author_name": "John Doe",
          "rating": 5,
          "text": "Great hotel...",
          "time": "2026-01-15T10:30:00",
          "language": "en"
        }
      ]
    }
  ]
}
```

## Collection Statistics

| Metric | Value |
|--------|-------|
| Total Properties | 4,342 |
| Total Reviews | 6,947 |
| Collection Time | ~4 hours |
| API Calls | ~9,000 |
| Data Size | ~25 MB |
| Time Period | February 2026 |

## Data Quality

### Validation Steps

1. **Duplicate removal**: Same place_id filtered
2. **Null checks**: Missing data handled
3. **Coordinate validation**: Lat/lng within city bounds
4. **Review text checks**: Non-empty reviews only

### Data Coverage

- **Language**: Primarily English reviews
- **Review age**: Mix of recent and older reviews
- **Property types**: Hotels, hostels, apartments, B&Bs
- **Price ranges**: Budget to luxury

## Ethical Considerations

✅ **Public data only**: Reviews are publicly available  
✅ **No personal info**: Only public usernames collected  
✅ **Aggregated analysis**: No individual profiling  
✅ **Research purpose**: Non-commercial use  
✅ **API compliance**: Follows Google's TOS  

## Reproducibility

To reproduce this data collection:

```bash
# 1. Set up API key
export GOOGLE_MAPS_API_KEY="your_key_here"

# 2. Run scraper
python scripts/google_places_scraper.py

# 3. Wait ~4 hours for completion
# Results saved to: data/all_cities_data.json
```

## Known Limitations

1. **Sample bias**: Only properties on Google Maps
2. **Language bias**: Primarily English reviews
3. **Recency**: API returns "relevant" not "recent" reviews
4. **Volume**: Limited to 5 reviews per property
5. **Verification**: Can't verify reviewer authenticity

## Future Improvements

- Expand to more cities
- Collect over time for trend analysis
- Include non-English reviews with translation
- Cross-reference with other platforms (TripAdvisor, Booking.com)
- Verify reviewer profiles where possible
