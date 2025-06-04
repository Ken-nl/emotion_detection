import requests

def emotion_detector(text_to_analyse):
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
                "error": f"API request failed with status {response.status_code}"
            }

        response_dict = response.json()
        emotion_scores = response_dict["emotionPredictions"][0]["emotion"]
        filtered_emotions = {
            "anger": emotion_scores.get("anger", 0),
            "disgust": emotion_scores.get("disgust", 0),
            "fear": emotion_scores.get("fear", 0),
            "joy": emotion_scores.get("joy", 0),
            "sadness": emotion_scores.get("sadness", 0),
        }
        dominant_emotion = max(filtered_emotions, key=filtered_emotions.get)
        filtered_emotions["dominant_emotion"] = dominant_emotion
        return filtered_emotions

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }
