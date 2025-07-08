import cv2
import os

def extract_frames_from_videos(source_dir, target_dir, label_name):
    os.makedirs(f"{target_dir}/images", exist_ok=True)
    os.makedirs(f"{target_dir}/labels", exist_ok=True)

    video_files = [f for f in os.listdir(source_dir) if f.endswith(('.mp4', '.avi'))]

    for idx, video in enumerate(video_files):
        cap = cv2.VideoCapture(os.path.join(source_dir, video))
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret or frame_count >= 1:  # Only extract the first frame
                break

            frame_name = f"{label_name}_{idx:04d}.jpg"
            cv2.imwrite(os.path.join(f"{target_dir}/images", frame_name), frame)

            label_file = frame_name.replace(".jpg", ".txt")
            class_id = 0 if label_name == "Fight" else 1
            with open(os.path.join(f"{target_dir}/labels", label_file), "w") as f:
                f.write(f"{class_id} 0.5 0.5 1.0 1.0")  # Dummy bounding box

            frame_count += 1

        cap.release()

# Set base path to your exact dataset location
base_path = r"C:\Users\HP\Pictures\restricted_content_detector_starter\drive\MyDrive\Colab Notebooks\computerVision\Project\Real Life Violence Dataset"

# Run for all video classes
extract_frames_from_videos(f"{base_path}\\train\\Fight", "data/train", "Fight")
extract_frames_from_videos(f"{base_path}\\train\\NonFight", "data/train", "NonFight")
extract_frames_from_videos(f"{base_path}\\val\\Fight", "data/val", "Fight")
extract_frames_from_videos(f"{base_path}\\val\\NonFight", "data/val", "NonFight")
