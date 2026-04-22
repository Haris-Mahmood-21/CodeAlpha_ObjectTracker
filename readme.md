# CodeAlpha_ObjectTracker

A Real-Time Object Detection and Tracking Dashboard built for the final task of the CodeAlpha Artificial Intelligence Internship. This project captures live webcam feeds and utilizes state-of-the-art Computer Vision models to track entities on screen.

## 🚀 Features
- **Real-Time Processing:** Captures and processes live webcam frames using OpenCV.
- **Advanced Object Tracking:** Utilizes YOLOv8's built-in tracking algorithms (`persist=True`) to assign and maintain unique IDs for detected objects across sequential frames.
- **Interactive UI:** Built with Streamlit, providing a clean, browser-based dashboard to start and stop the visual feed.
- **High Performance:** Employs the YOLOv8-Nano (`yolov8n.pt`) model for maximum FPS during live inference.

## 🛠️ Tech Stack
- **Computer Vision:** `ultralytics` (YOLOv8), `opencv-python`
- **Frontend Framework:** Streamlit
- **Language:** Python 3

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Haris-Mahmood-21/CodeAlpha_ObjectTracker

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    
3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    
4. **Run the application:**

    ```bash
    streamlit run app.py

**📝 License**
This project is for educational purposes as part of the CodeAlpha Internship.