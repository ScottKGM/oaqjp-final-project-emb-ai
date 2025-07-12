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
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None