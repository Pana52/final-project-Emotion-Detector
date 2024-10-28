from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detection():
    # Retrieve the text to analyze from the GET request query parameter
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Process the text and detect emotions
    result = emotion_detector(text_to_analyze)

    # Format the output string as specified
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    # Return the response as JSON
    return jsonify({"response": response_text})

@app.route('/')
def index():
    return render_template('index.html')  # Serve the main page

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
