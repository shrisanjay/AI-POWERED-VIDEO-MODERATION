from flask import Flask, render_template, request
import os
from main import run_detection

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        if 'video' not in request.files:
            return "No file part"
        file = request.files['video']
        if file.filename == '':
            return "No selected file"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Run detection
        output = run_detection(filepath)

        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Detection Results</title>
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #1f1c2c, #928dab);
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    color: #f0f0f0;
                }}
                h2 {{
                    font-size: 3rem;
                    margin-bottom: 20px;
                    text-shadow: 2px 2px #000;
                    color: #00e6e6;
                }}
                .result-box {{
                    background: rgba(0, 0, 0, 0.8);
                    padding: 30px 40px;
                    border-radius: 15px;
                    box-shadow: 0 0 30px #00e6e6;
                    max-width: 800px;
                    text-align: center;
                    font-size: 1.25rem;
                    color: #e0f7fa;
                }}
                .back-button {{
                    margin-top: 30px;
                    background-color: #00e6e6;
                    border: none;
                    color: #000;
                    padding: 12px 24px;
                    font-size: 1rem;
                    border-radius: 8px;
                    text-decoration: none;
                    font-weight: bold;
                    transition: background-color 0.3s ease;
                    box-shadow: 0 0 10px #00e6e6;
                }}
                .back-button:hover {{
                    background-color: #00b3b3;
                    color: white;
                }}
                .footer {{
                    position: absolute;
                    bottom: 20px;
                    font-size: 0.9rem;
                    color: #ccc;
                }}
            </style>
        </head>
        <body>
            <h2>Detection Results</h2>
            <div class="result-box">
                {output}
            </div>
            <a href="/" class="back-button">⬅ Back to Upload</a>
            <div class="footer">Powered by Flask, YOLOv8 & Whisper</div>
        </body>
        </html>
        """

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
