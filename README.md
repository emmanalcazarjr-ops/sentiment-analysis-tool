# Sentiment Analysis Tool

A Python-based sentiment analysis tool that classifies text as positive, negative, or neutral using keyword-based analysis.

## Features

- Keyword-based sentiment analysis
- Confidence scoring
- Positive/negative keyword extraction
- Interactive CLI mode
- API-ready for serverless deployment

## Usage

### CLI Mode
```bash
python sentiment.py
```

### As a Module
```python
from sentiment import analyze_sentiment

result = analyze_sentiment("This product is amazing!")
print(result)
# {
#   'sentiment': 'POSITIVE',
#   'score': 0.75,
#   'confidence': 0.87,
#   'keywords': ['amazing'],
#   'details': {...}
# }
```

## API

The sentiment analysis is also available as a live API:
- **URL:** https://sentiment-api-nine.vercel.app
- **Method:** POST
- **Body:** `{"text": "Your text here"}`

## Tech Stack

- Python 3.9+
- Regular expressions for text processing
- No external dependencies required

## Author

**Emmanuel L. Alcazar Jr.**
- GitHub: [@emmanalcazarjr-ops](https://github.com/emmanalcazarjr-ops)
