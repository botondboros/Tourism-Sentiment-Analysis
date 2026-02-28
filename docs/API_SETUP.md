# Google Maps API Setup Guide

This guide walks you through setting up the Google Maps Platform API for the EU Tourism Sentiment Analysis project.

## Prerequisites

- A Google account
- A credit/debit card (for verification - free tier available)

## Step-by-Step Setup

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "New Project"
3. Enter project name: `eu-tourism-sentiment`
4. Click "Create"

### 2. Enable Billing

1. In the left sidebar, go to "Billing"
2. Click "Link a billing account"
3. Follow prompts to add payment method
4. **Note**: Google offers $200 free credit monthly

### 3. Enable Required APIs

1. In the search bar, type "Places API"
2. Click "Places API (New)"
3. Click "ENABLE"
4. Repeat for "Maps JavaScript API"

### 4. Create API Key

1. Go to "APIs & Services" → "Credentials"
2. Click "+ CREATE CREDENTIALS" → "API key"
3. Copy your API key (looks like: `AIzaSyBxxxxx...`)

### 5. Secure Your API Key (Recommended)

1. Click on your newly created API key
2. Under "Application restrictions":
   - For testing: Select "None"
   - For production: Select "HTTP referrers" and add your domain
3. Under "API restrictions":
   - Select "Restrict key"
   - Enable only: "Places API" and "Maps JavaScript API"
4. Click "SAVE"

### 6. Add API Key to Project

In `scripts/google_places_scraper.py`, replace:
```python
API_KEY = "YOUR_GOOGLE_API_KEY_HERE"
```

With your actual API key:
```python
API_KEY = "AIzaSyBxxxxxxxxxxxxxxxxxxxxx"
```

## Cost Estimation

### Places API Pricing (as of 2026)
- **Text Search**: $32 per 1,000 requests
- **Place Details**: $17 per 1,000 requests
- **Free tier**: $200 credit/month

### Project Costs
For collecting data from 5 cities:
- ~5,000 Place Details requests
- **Estimated cost**: ~$85
- **With free tier**: $0 (if under monthly limit)

## Rate Limits

- **Default**: 100 requests per 10 seconds
- **Daily quota**: Varies by account
- The scraper includes delays to respect rate limits

## Troubleshooting

### "This API key is not authorized"
- Check that Places API is enabled
- Verify API restrictions allow your IP/domain

### "Billing must be enabled"
- Ensure billing account is linked to project
- Wait 1-2 minutes after enabling billing

### "Rate limit exceeded"
- Reduce request frequency in script
- Wait for quota reset (usually daily)

## Security Best Practices

1. **Never commit API keys to git**
   - Use environment variables
   - Add to `.gitignore`

2. **Use API restrictions**
   - Limit to specific APIs
   - Add domain/IP restrictions

3. **Monitor usage**
   - Set up billing alerts
   - Review usage in Cloud Console regularly

## Additional Resources

- [Google Maps Platform Documentation](https://developers.google.com/maps/documentation)
- [Places API Reference](https://developers.google.com/maps/documentation/places/web-service)
- [API Key Best Practices](https://cloud.google.com/docs/authentication/api-keys)
