# Sentiment Analysis Tool

A Python-based sentiment analysis tool that classifies text as positive, negative, or neutral using keyword-based analysis with confidence scoring. The tool uses curated keyword dictionaries and a scoring algorithm to determine sentiment polarity without requiring any external ML libraries or API calls. Also deployed as a serverless API on Vercel with DeepSeek AI integration for enhanced analysis.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.9+ |
| Analysis | Keyword-based scoring (regex + custom dictionaries) |
| AI Enhancement | DeepSeek AI (optional, for API deployment) |
| Deployment | Vercel Serverless Functions |
| Dependencies | None (stdlib only for core analysis) |

## Features

- Keyword-based sentiment classification (positive / negative / neutral)
- Confidence scoring with percentage breakdown
- Positive and negative keyword extraction
- Interactive CLI mode for testing
- REST API endpoint with DeepSeek AI enhancement

## Installation

```bash
# Clone the repository
git clone https://github.com/emmanalcazarjr-ops/sentiment-analysis-tool.git
cd sentiment-analysis-tool

# No dependencies required — run directly
python sentiment.py
```

## Usage

### CLI Mode

```bash
python sentiment.py
# Enter text when prompted
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

### REST API

The sentiment analysis is also available as a live API:

```bash
curl -X POST https://sentiment-api-nine.vercel.app/api \
  -H "Content-Type: application/json" \
  -d '{"text": "This product is amazing!"}'
```

## Live Demo

[Sentiment Analysis API](https://sentiment-api-nine.vercel.app)

## Author

**Emmanuel L. Alcazar Jr.**
- GitHub: [@emmanalcazarjr-ops](https://github.com/emmanalcazarjr-ops)
- Portfolio: [portfolio-elalcazarjr.vercel.app](https://portfolio-elalcazarjr.vercel.app)
