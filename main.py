import os
import sys
import cv2
from ultralytics import YOLO
import ffmpeg
import speech_recognition as sr
from pydub import AudioSegment

def run_detection(video_path):
    output_log = []

    # Step 1: Extract audio using ffmpeg
    output_log.append("🔊 Extracting audio for profanity detection...")
    audio_path = "temp_audio.wav"

    try:
        ffmpeg.input(video_path).output(audio_path).run(overwrite_output=True)
    except ffmpeg.Error as e:
        output_log.append(f"Error extracting audio: {str(e)}")
        return "<br>".join(output_log)

    # Step 2: Convert to readable format if needed
    sound = AudioSegment.from_file(audio_path)
    sound.export("converted.wav", format="wav")

    # Step 3: Transcribe audio using Google Web Speech API
    recognizer = sr.Recognizer()
    with sr.AudioFile("converted.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        text = ""
        output_log.append("⚠️ Could not understand audio.")
    except sr.RequestError as e:
        output_log.append(f"Google API error: {e}")
        return "<br>".join(output_log)

    # Step 4: Check for profanity
    bad_words = [
        "damn", "hell", "shit", "fuck", "fucking", "bitch", "bastard", "asshole", "dick", "piss",
        "crap", "pussy", "cock", "slut", "whore", "violence", "kill", "murder", "rape", "terrorist"
    ]
    flagged_words = [word for word in bad_words if word in text]

    if flagged_words:
        output_log.append(f"⚠️ Profanity detected in audio: {flagged_words}")
    else:
        output_log.append("✅ No profanity detected in audio.")

    # Step 5: Run YOLOv8 for frame-level violence detection
    output_log.append("🔍 Running violence detection on frames...")
    yolo = YOLO("runs/detect/train4/weights/best.pt")
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    detected = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % 30 != 0:
            continue

        results = yolo(frame)
        if results[0].boxes.conf.numel() > 0:
            output_log.append(f"⚠️ Violence detected at frame {frame_count}")
            detected = True
            break

    cap.release()
    if not detected:
        output_log.append("✅ No violence detected in video.")

    return "<br>".join(output_log)
