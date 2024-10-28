import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        
        # Parse the JSON response and navigate to the correct section
        response_data = response.json()
        print("Response JSON:", json.dumps(response_data, indent=2))  # Debug line
        
        # Extract emotions from the nested structure
        emotions = response_data["emotionPredictions"][0]["emotion"]
        anger = emotions.get("anger", 0)
        disgust = emotions.get("disgust", 0)
        fear = emotions.get("fear", 0)
        joy = emotions.get("joy", 0)
        sadness = emotions.get("sadness", 0)
        
        # Determine the dominant emotion
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Format and return the output
        result = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
        return result
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
