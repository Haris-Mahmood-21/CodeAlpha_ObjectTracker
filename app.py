import  streamlit as st
import cv2
from ultralytics import YOLO

# Load App
st.set_page_config(page_title="Real-Time Object Tracker", page_icon="👁️", layout = "wide")
st.title("👁️ Real-Time Object Detection & Tracking")
st.write("Powered by YOLOv8 and OpenCV")

# Load Yolo Model
@st.cache_resource
def load_model():
    return YOLO('yolov8n.pt')

model = load_model()

# Creating buttons
col1, col2 = st.columns(2)

with col1:
    start_button = st.button( "🟢 Start Webcam", type="primary", use_container_width="True")
    
with col2:    
    stop_button = st.button( "🔴 Stop Webcam", type="secondary", use_container_width="True")
    
frame_placeholder = st.empty()

# Opening Webcam
if start_button:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")

    else:
        st.success("Webcam active. Press 'Stop Webcam' to halt.")

# Continuous loop to grab frames 
        while cap.isOpened and not stop_button:
            ret, frame = cap.read()
            if not ret:
                st.error( "Failed to capture frame from webcam. "  )
                break

# Showing result 
            results = model.track(frame, persist=True, conf = 0.5 )
            annotated_frames = results[0].plot()
            annotated_frames_rgb = cv2.cvtColor( annotated_frames, cv2.COLOR_BGR2RGB )
            frame_placeholder.image( annotated_frames_rgb, channels='RGB', use_container_width=True)

# Clean up after loops end.
        cap.release()
        cv2.destroyAllWindows()
        st.info("Webcam Stopped.") 


