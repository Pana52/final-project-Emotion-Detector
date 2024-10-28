import requests

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
        
        # Print the entire response JSON for inspection
        print("Response JSON:", response.json())
        return response.json().get('text', "Key 'text' not found in response")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
