from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_web():
    text_to_analyse = request.args.get('textToAnalyze')
    print("TEXT INPUT:", text_to_analyse)

    result = emotion_detector(text_to_analyse)
    print("RESULT:", result)

    if not result or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    formatted = (
        f"For the given statement, the system response is "
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']} and "
        f"sadness: {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
