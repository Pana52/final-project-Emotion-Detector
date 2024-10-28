"""
Flask application for Emotion Detection.

This module provides endpoints for analyzing text emotions using the Watson NLP service.
The application includes a GET route for processing text input, a main page for user input,
and error handling for blank or invalid inputs.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detection():
    """
    Endpoint to analyze emotion in a given text.

    Retrieves text from the query parameters, analyzes it using emotion_detector,
    and returns a JSON response with formatted emotion results or an error message
    for invalid input.

    Returns:
        JSON response containing emotion scores and the dominant emotion, or
        an error message for blank inputs.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Process the text and detect emotions
    result = emotion_detector(text_to_analyze)

    # Check if the result indicates an invalid input
    if result['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

    return jsonify({"response": response_text})

@app.route('/')
def index():
    """
    Serves the main HTML page.

    Returns:
        Rendered template of index.html.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
