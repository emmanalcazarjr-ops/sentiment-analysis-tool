"""
Sentiment Analysis Tool
Analyzes text sentiment (positive, negative, neutral) using keyword-based analysis.
"""

import re
import json


def analyze_sentiment(text: str) -> dict:
    """Analyze the sentiment of the given text."""
    
    positive_words = [
        'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',
        'love', 'like', 'happy', 'joy', 'beautiful', 'perfect', 'best',
        'awesome', 'brilliant', 'outstanding', 'superb', 'delighted',
        'pleased', 'excited', 'grateful', 'thankful', 'blessed', 'success',
        'win', 'victory', 'achieve', 'accomplish', 'improve', 'better',
        'helpful', 'kind', 'generous', 'friendly', 'pleasant', 'nice',
        'recommend', 'satisfied', 'quality', 'premium', 'valuable'
    ]

    negative_words = [
        'bad', 'terrible', 'horrible', 'awful', 'poor', 'worst',
        'hate', 'dislike', 'angry', 'sad', 'ugly', 'broken', 'fail',
        'failure', 'disappoint', 'frustrated', 'annoyed', 'furious',
        'disgusted', 'miserable', 'painful', 'suffer', 'problem',
        'issue', 'bug', 'error', 'crash', 'slow', 'expensive',
        'waste', 'scam', 'fraud', 'complaint', 'refund', 'return',
        'unhappy', 'dissatisfied', 'unreliable', 'defective', 'useless'
    ]

    text_lower = text.lower()
    words = re.findall(r'\b\w+\b', text_lower)

    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    total_sentiment_words = positive_count + negative_count

    if total_sentiment_words == 0:
        score = 0.0
        sentiment = "NEUTRAL"
        confidence = 0.5
    else:
        score = (positive_count - negative_count) / max(len(words), 1)
        score = max(-1.0, min(1.0, score * 5))

        if score > 0.1:
            sentiment = "POSITIVE"
        elif score < -0.1:
            sentiment = "NEGATIVE"
        else:
            sentiment = "NEUTRAL"

        confidence = min(0.95, 0.5 + abs(score) * 0.5)

    positive_found = [w for w in words if w in positive_words]
    negative_found = [w for w in words if w in negative_words]
    keywords = list(set(positive_found + negative_found))[:10]

    return {
        "sentiment": sentiment,
        "score": round(score, 4),
        "confidence": round(confidence, 4),
        "keywords": keywords,
        "details": {
            "positive_words": positive_found,
            "negative_words": negative_found,
            "word_count": len(words)
        }
    }


def main():
    """Interactive CLI for sentiment analysis."""
    print("=" * 50)
    print("  Sentiment Analysis Tool")
    print("  Type 'quit' to exit")
    print("=" * 50)
    print()

    while True:
        text = input("Enter text to analyze: ").strip()
        
        if text.lower() == 'quit':
            print("\nGoodbye!")
            break
        
        if not text:
            print("Please enter some text.\n")
            continue

        result = analyze_sentiment(text)

        print(f"\n{'─' * 40}")
        print(f"  Sentiment: {result['sentiment']}")
        print(f"  Score: {result['score']}")
        print(f"  Confidence: {result['confidence']:.1%}")
        
        if result['keywords']:
            print(f"  Keywords: {', '.join(result['keywords'])}")
        
        print(f"{'─' * 40}\n")


if __name__ == "__main__":
    main()
