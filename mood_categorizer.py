from textblob import TextBlob

def categorize_by_mood(metadata):
    mood_keywords = {
        'happy': ['happy', 'joyful', 'cheerful', 'glad', 'delighted'],
        'sad': ['sad', 'melancholic', 'blue', 'down', 'unhappy'],
        'energetic': ['energetic', 'excited', 'upbeat', 'lively', 'dynamic'],
        'calm': ['calm', 'peaceful', 'relaxed', 'soothing', 'tranquil']
    }

    title = metadata.get('title', [''])[0]
    artist = metadata.get('artist', [''])[0]
    description = f"{title} {artist}"

    sentiment = TextBlob(description).sentiment.polarity

    for mood, keywords in mood_keywords.items():
        if any(keyword in description.lower() for keyword in keywords):
            return mood

    if sentiment > 0.3:
        return 'happy'
    elif sentiment < -0.3:
        return 'sad'
    elif 0 < sentiment <= 0.3:
        return 'energetic'
    else:
        return 'calm'
