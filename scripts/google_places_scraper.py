"""
Google Places Scraper for Accommodation Reviews
Legal and uses official Google Places API
"""

import googlemaps
from datetime import datetime
from typing import List, Dict
import time
import json

class GooglePlacesReviewScraper:
    """Scrape reviews from Google Places API (legal and official)"""
    
    def __init__(self, api_key: str):
        """
        Initialize with your Google API key
        
        Get your key from: https://console.cloud.google.com/
        Enable Places API and create credentials
        """
        self.gmaps = googlemaps.Client(key=api_key)
    
    def search_accommodations(self, location: str, radius: int = 5000) -> List[Dict]:
        """
        Search for hotels/accommodations in a location
        
        Args:
            location: City name (e.g., "Budapest, Hungary")
            radius: Search radius in meters (default 5km)
            
        Returns:
            List of accommodation dictionaries
        """
        print(f"Searching accommodations in {location}...")
        
        # First, geocode the location to get coordinates
        geocode_result = self.gmaps.geocode(location)
        
        if not geocode_result:
            print(f"Could not find location: {location}")
            return []
        
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        
        print(f"Found coordinates: {lat}, {lng}")
        
        # Search for hotels nearby
        places_result = self.gmaps.places_nearby(
            location=(lat, lng),
            radius=radius,
            type='lodging'  # Hotels, B&Bs, accommodations
        )
        
        accommodations = []
        
        for place in places_result.get('results', []):
            accommodation = {
                'place_id': place['place_id'],
                'name': place['name'],
                'address': place.get('vicinity', ''),
                'rating': place.get('rating'),
                'total_ratings': place.get('user_ratings_total', 0),
                'location': {
                    'lat': place['geometry']['location']['lat'],
                    'lng': place['geometry']['location']['lng']
                }
            }
            accommodations.append(accommodation)
        
        print(f"Found {len(accommodations)} accommodations")
        return accommodations
    
    def get_place_details(self, place_id: str) -> Dict:
        """
        Get detailed information about a specific place including reviews
        
        Args:
            place_id: Google Place ID
            
        Returns:
            Dictionary with place details and reviews
        """
        print(f"Fetching details for place: {place_id}")
        
        # Get place details with reviews
        place_details = self.gmaps.place(
            place_id=place_id,
            fields=['name', 'rating', 'reviews', 'formatted_address', 
                   'user_ratings_total', 'price_level']
        )
        
        result = place_details.get('result', {})
        
        # Extract reviews
        reviews = []
        for review in result.get('reviews', []):
            review_data = {
                'author_name': review.get('author_name'),
                'rating': review.get('rating'),
                'text': review.get('text'),
                'time': datetime.fromtimestamp(review.get('time')).isoformat(),
                'language': review.get('language', 'unknown'),
                'author_url': review.get('author_url', ''),
                'relative_time': review.get('relative_time_description', '')
            }
            reviews.append(review_data)
        
        return {
            'place_id': place_id,
            'name': result.get('name'),
            'address': result.get('formatted_address'),
            'rating': result.get('rating'),
            'total_ratings': result.get('user_ratings_total'),
            'price_level': result.get('price_level'),
            'reviews': reviews,
            'review_count': len(reviews)
        }
    
    def collect_all_reviews(self, location: str, max_places: int = 20) -> List[Dict]:
        """
        Collect reviews for accommodations in a location
        
        Args:
            location: City name
            max_places: Maximum number of places to process
            
        Returns:
            List of all collected data
        """
        # Search for accommodations
        accommodations = self.search_accommodations(location)
        
        # Limit to max_places
        accommodations = accommodations[:max_places]
        
        all_data = []
        
        for i, accommodation in enumerate(accommodations):
            print(f"\nProcessing {i+1}/{len(accommodations)}: {accommodation['name']}")
            
            # Get detailed reviews
            details = self.get_place_details(accommodation['place_id'])
            all_data.append(details)
            
            # Respect rate limits
            time.sleep(1)
        
        return all_data
    
    def save_to_json(self, data: List[Dict], filename: str):
        """Save collected data to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Saved data to {filename}")


def main():
    """Example usage"""
    
    # STEP 1: Get your Google API key from https://console.cloud.google.com/
    API_KEY = "YOUR_GOOGLE_API_KEY_HERE"  # Replace with your actual key
    
    # STEP 2: Initialize scraper
    scraper = GooglePlacesReviewScraper(API_KEY)
    
    # STEP 3: Collect reviews from Budapest hotels
    print("Starting Google Places review collection...")
    print("=" * 60)
    
    data = scraper.collect_all_reviews(
        location="Budapest, Hungary",
        max_places=10  # Start with 10 hotels for testing
    )
    
    # STEP 4: Save to file
    scraper.save_to_json(data, 'budapest_reviews_google.json')
    
    # STEP 5: Print summary
    print("\n" + "=" * 60)
    print("COLLECTION SUMMARY")
    print("=" * 60)
    total_reviews = sum(place['review_count'] for place in data)
    print(f"Total places: {len(data)}")
    print(f"Total reviews collected: {total_reviews}")
    
    # Show sample
    if data and data[0]['reviews']:
        print("\nSample review:")
        sample = data[0]['reviews'][0]
        print(f"  Place: {data[0]['name']}")
        print(f"  Rating: {sample['rating']}/5")
        print(f"  Text: {sample['text'][:100]}...")


if __name__ == "__main__":
    main()

