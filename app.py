from flask import Flask, request, render_template, send_file
from pytube import YouTube
import os

app = Flask(__name__)

# Home route to render the download form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the download logic
@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path='downloads', filename='video.mp4')
        return send_file('downloads/video.mp4', as_attachment=True)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
