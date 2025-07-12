import requests

def emotion_detector(text_to_analyze):
    """ 
    Runs emotion detection using the Watson NLP library
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
    emotions = result['emotionPredictions'][0]['emotion']
    top_emotion = max(emotions.items(), key = lambda x: x[1])
    emotions['dominant_emotion'] = top_emotion[0]
    
    return emotions

