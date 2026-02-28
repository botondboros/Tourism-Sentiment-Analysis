"""
Sentiment Analysis Module
Analyzes review sentiment, detects trends, and identifies quality changes
"""

import re
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
import numpy as np
from collections import Counter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class SentimentScore:
    """Sentiment analysis result"""
    positive_score: float  # 0-1
    negative_score: float  # 0-1
    neutral_score: float   # 0-1
    overall_sentiment: str  # positive, negative, neutral
    confidence: float       # 0-1
    

@dataclass
class TrendAnalysis:
    """Trend analysis result"""
    direction: str  # improving, declining, stable
    change_magnitude: float
    statistical_significance: bool
    time_period_days: int
    sample_size: int


class SentimentAnalyzer:
    """Analyze sentiment in reviews using keyword-based and statistical methods"""
    
    def __init__(self):
        # Hungarian positive keywords (extend as needed)
        self.positive_keywords_hu = {
            'kiváló', 'kitűnő', 'fantasztikus', 'csodálatos', 'nagyszerű',
            'tökéletes', 'remek', 'kiváló', 'ajánlom', 'tiszta', 'barátságos',
            'finom', 'ízletes', 'friss', 'modern', 'kényelmes', 'szép'
        }
        
        # Hungarian negative keywords (extend as needed)
        self.negative_keywords_hu = {
            'rossz', 'szörnyű', 'undorító', 'piszkos', 'drága', 'lassú',
            'hideg', 'zajos', 'régi', '問題', 'csalódás', 'kellemetlen',
            'nem ajánlom', 'soha többé', 'elkerülendő'
        }
        
        # English positive keywords
        self.positive_keywords_en = {
            'excellent', 'great', 'amazing', 'wonderful', 'perfect',
            'fantastic', 'outstanding', 'beautiful', 'delicious', 'clean',
            'friendly', 'comfortable', 'recommend', 'loved', 'enjoyed'
        }
        
        # English negative keywords
        self.negative_keywords_en = {
            'terrible', 'awful', 'horrible', 'dirty', 'expensive', 'slow',
            'cold', 'noisy', 'old', 'problem', 'disappointed', 'avoid',
            'never again', 'worst', 'unpleasant'
        }
    
    def analyze_text(self, text: str, language: str = 'auto') -> SentimentScore:
        """
        Analyze sentiment of a text
        
        Args:
            text: Review text to analyze
            language: Language code ('hu', 'en', 'auto')
            
        Returns:
            SentimentScore object
        """
        if not text:
            return SentimentScore(0.5, 0.5, 1.0, 'neutral', 0.0)
        
        text_lower = text.lower()
        
        # Detect language if auto
        if language == 'auto':
            language = self._detect_language(text_lower)
        
        # Select appropriate keyword sets
        if language == 'hu':
            positive_kw = self.positive_keywords_hu
            negative_kw = self.negative_keywords_hu
        else:
            positive_kw = self.positive_keywords_en
            negative_kw = self.negative_keywords_en
        
        # Count keyword matches
        positive_count = sum(1 for kw in positive_kw if kw in text_lower)
        negative_count = sum(1 for kw in negative_kw if kw in text_lower)
        total_count = positive_count + negative_count
        
        if total_count == 0:
            return SentimentScore(0.5, 0.5, 1.0, 'neutral', 0.3)
        
        # Calculate scores
        positive_score = positive_count / total_count
        negative_score = negative_count / total_count
        neutral_score = 1.0 - max(positive_score, negative_score)
        
        # Determine overall sentiment
        if positive_score > negative_score + 0.2:
            overall = 'positive'
            confidence = positive_score
        elif negative_score > positive_score + 0.2:
            overall = 'negative'
            confidence = negative_score
        else:
            overall = 'neutral'
            confidence = 1.0 - abs(positive_score - negative_score)
        
        return SentimentScore(
            positive_score=positive_score,
            negative_score=negative_score,
            neutral_score=neutral_score,
            overall_sentiment=overall,
            confidence=min(confidence, 1.0)
        )
    
    def _detect_language(self, text: str) -> str:
        """
        Simple language detection based on character patterns
        
        Args:
            text: Text to analyze
            
        Returns:
            Language code ('hu' or 'en')
        """
        # Hungarian-specific characters
        hu_chars = 'áéíóöőúüű'
        hu_count = sum(1 for char in text.lower() if char in hu_chars)
        
        # Simple heuristic: if >2% of characters are Hungarian-specific, classify as Hungarian
        if len(text) > 0 and (hu_count / len(text)) > 0.02:
            return 'hu'
        return 'en'
    
    def analyze_rating_distribution(self, ratings: List[float]) -> Dict:
        """
        Analyze the distribution of ratings
        
        Args:
            ratings: List of rating values
            
        Returns:
            Dictionary with distribution statistics
        """
        if not ratings:
            return {}
        
        ratings_array = np.array(ratings)
        
        distribution = {
            'mean': float(np.mean(ratings_array)),
            'median': float(np.median(ratings_array)),
            'std_dev': float(np.std(ratings_array)),
            'min': float(np.min(ratings_array)),
            'max': float(np.max(ratings_array)),
            'count': len(ratings),
            'rating_counts': dict(Counter(ratings))
        }
        
        # Calculate percentiles
        distribution['percentile_25'] = float(np.percentile(ratings_array, 25))
        distribution['percentile_75'] = float(np.percentile(ratings_array, 75))
        
        return distribution


class TrendDetector:
    """Detect trends in time-series data"""
    
    def __init__(self, significance_threshold: float = 0.05):
        self.significance_threshold = significance_threshold
    
    def detect_rating_trend(self, 
                           ratings_with_dates: List[Tuple[datetime, float]],
                           window_days: int = 90) -> TrendAnalysis:
        """
        Detect trends in ratings over time
        
        Args:
            ratings_with_dates: List of (date, rating) tuples
            window_days: Time window for comparison
            
        Returns:
            TrendAnalysis object
        """
        if len(ratings_with_dates) < 2:
            return TrendAnalysis('insufficient_data', 0.0, False, window_days, len(ratings_with_dates))
        
        # Sort by date
        sorted_ratings = sorted(ratings_with_dates, key=lambda x: x[0])
        
        # Split into recent and historical
        cutoff_date = datetime.now() - timedelta(days=window_days)
        
        recent_ratings = [r for d, r in sorted_ratings if d >= cutoff_date]
        historical_ratings = [r for d, r in sorted_ratings if d < cutoff_date]
        
        if not recent_ratings or not historical_ratings:
            return TrendAnalysis('insufficient_data', 0.0, False, window_days, len(ratings_with_dates))
        
        # Calculate means
        recent_mean = np.mean(recent_ratings)
        historical_mean = np.mean(historical_ratings)
        
        # Calculate change
        change = recent_mean - historical_mean
        
        # Determine direction
        if abs(change) < 0.2:
            direction = 'stable'
        elif change > 0:
            direction = 'improving'
        else:
            direction = 'declining'
        
        # Simple statistical test (t-test would be better in production)
        recent_std = np.std(recent_ratings)
        historical_std = np.std(historical_ratings)
        pooled_std = np.sqrt((recent_std**2 + historical_std**2) / 2)
        
        # Significance based on effect size
        if pooled_std > 0:
            effect_size = abs(change) / pooled_std
            significant = effect_size > 0.5  # Medium effect size
        else:
            significant = False
        
        return TrendAnalysis(
            direction=direction,
            change_magnitude=float(change),
            statistical_significance=significant,
            time_period_days=window_days,
            sample_size=len(recent_ratings) + len(historical_ratings)
        )
    
    def detect_volume_spike(self, 
                           review_dates: List[datetime],
                           window_days: int = 30) -> Dict:
        """
        Detect unusual spikes in review volume
        
        Args:
            review_dates: List of review dates
            window_days: Time window for baseline calculation
            
        Returns:
            Dictionary with spike detection results
        """
        if len(review_dates) < 10:
            return {'spike_detected': False, 'reason': 'insufficient_data'}
        
        # Sort dates
        sorted_dates = sorted(review_dates)
        
        # Calculate reviews per day
        date_counts = Counter([d.date() for d in sorted_dates])
        
        # Get recent window
        cutoff_date = datetime.now().date() - timedelta(days=window_days)
        recent_counts = [count for date, count in date_counts.items() if date >= cutoff_date]
        historical_counts = [count for date, count in date_counts.items() if date < cutoff_date]
        
        if not recent_counts or not historical_counts:
            return {'spike_detected': False, 'reason': 'insufficient_data'}
        
        # Calculate baseline
        baseline_mean = np.mean(historical_counts)
        baseline_std = np.std(historical_counts)
        
        # Check for spikes (>2 standard deviations above mean)
        max_recent = max(recent_counts)
        threshold = baseline_mean + (2 * baseline_std)
        
        spike_detected = max_recent > threshold
        
        return {
            'spike_detected': spike_detected,
            'max_daily_reviews': int(max_recent),
            'baseline_avg': float(baseline_mean),
            'threshold': float(threshold),
            'spike_magnitude': float((max_recent - baseline_mean) / baseline_std) if baseline_std > 0 else 0
        }


class QualityMonitor:
    """Monitor quality changes over time"""
    
    def __init__(self):
        self.sentiment_analyzer = SentimentAnalyzer()
        self.trend_detector = TrendDetector()
    
    def analyze_quality_change(self, 
                               reviews: List[Dict],
                               time_window_days: int = 90) -> Dict:
        """
        Comprehensive quality change analysis
        
        Args:
            reviews: List of review dictionaries with 'date', 'rating', 'text' keys
            time_window_days: Time window for trend detection
            
        Returns:
            Dictionary with quality analysis
        """
        if not reviews:
            return {'status': 'no_data'}
        
        # Extract ratings with dates
        ratings_with_dates = [
            (datetime.fromisoformat(r['date']), r['rating']) 
            for r in reviews if 'date' in r and 'rating' in r
        ]
        
        # Detect rating trend
        rating_trend = self.trend_detector.detect_rating_trend(
            ratings_with_dates, 
            window_days=time_window_days
        )
        
        # Analyze review volume
        review_dates = [datetime.fromisoformat(r['date']) for r in reviews if 'date' in r]
        volume_analysis = self.trend_detector.detect_volume_spike(review_dates)
        
        # Sentiment analysis on recent reviews
        cutoff_date = datetime.now() - timedelta(days=time_window_days)
        recent_reviews = [
            r for r in reviews 
            if 'date' in r and datetime.fromisoformat(r['date']) >= cutoff_date
        ]
        
        sentiment_scores = []
        for review in recent_reviews:
            if 'text' in review and review['text']:
                sentiment = self.sentiment_analyzer.analyze_text(review['text'])
                sentiment_scores.append(sentiment)
        
        # Calculate sentiment distribution
        if sentiment_scores:
            sentiment_dist = {
                'positive': sum(1 for s in sentiment_scores if s.overall_sentiment == 'positive'),
                'negative': sum(1 for s in sentiment_scores if s.overall_sentiment == 'negative'),
                'neutral': sum(1 for s in sentiment_scores if s.overall_sentiment == 'neutral')
            }
        else:
            sentiment_dist = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        return {
            'rating_trend': {
                'direction': rating_trend.direction,
                'change': rating_trend.change_magnitude,
                'significant': rating_trend.statistical_significance
            },
            'volume_analysis': volume_analysis,
            'sentiment_distribution': sentiment_dist,
            'total_reviews_analyzed': len(reviews),
            'recent_reviews_analyzed': len(recent_reviews),
            'time_window_days': time_window_days
        }


def main():
    """Example usage"""
    # Example review data
    example_reviews = [
        {
            'date': '2024-01-15',
            'rating': 4.5,
            'text': 'Kiváló szállás, nagyon tiszta és kényelmes. Ajánlom!'
        },
        {
            'date': '2024-02-01',
            'rating': 3.0,
            'text': 'Átlagos élmény, semmi extra.'
        },
        {
            'date': '2024-02-15',
            'rating': 5.0,
            'text': 'Fantasztikus! Tökéletes minden.'
        }
    ]
    
    # Analyze sentiment
    analyzer = SentimentAnalyzer()
    for review in example_reviews:
        sentiment = analyzer.analyze_text(review['text'])
        logger.info(f"Review sentiment: {sentiment.overall_sentiment} (confidence: {sentiment.confidence:.2f})")
    
    # Monitor quality
    monitor = QualityMonitor()
    quality_analysis = monitor.analyze_quality_change(example_reviews, time_window_days=30)
    logger.info(f"Quality analysis: {quality_analysis}")


if __name__ == "__main__":
    main()
