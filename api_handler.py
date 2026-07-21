import json
from sentiment import analyze_sentiment


def lambda_handler(event, context):
    """AWS Lambda / Vercel Serverless handler."""
    try:
        body = json.loads(event.get('body', '{}'))
        text = body.get('text', '')
        
        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Text is required'})
            }
        
        result = analyze_sentiment(text)
        result['input'] = {'text': text[:200] + '...' if len(text) > 200 else text}
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(result)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
