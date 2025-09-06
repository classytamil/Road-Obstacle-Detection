import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import numpy as np
from PIL import Image

# Load YOLOv8 pretrained on COCO
model = YOLO("yolov8n.pt")   # small model, fast enough for demo

# COCO Classes
COCO_CLASSES = [
    'person','bicycle','car','motorcycle','airplane','bus','train','truck','boat',
    'traffic light','fire hydrant','stop sign','parking meter','bench','bird','cat',
    'dog','horse','sheep','cow','elephant','bear','zebra','giraffe','backpack','umbrella',
    'handbag','tie','suitcase','frisbee','skis','snowboard','sports ball','kite','baseball bat',
    'baseball glove','skateboard','surfboard','tennis racket','bottle','wine glass','cup','fork',
    'knife','spoon','bowl','banana','apple','sandwich','orange','broccoli','carrot','hot dog','pizza',
    'donut','cake','chair','couch','potted plant','bed','dining table','toilet','tv','laptop','mouse',
    'remote','keyboard','cell phone','microwave','oven','toaster','sink','refrigerator','book','clock',
    'vase','scissors','teddy bear','hair drier','toothbrush'
]

# Road-related classes
RELEVANT_CLASSES = [
    'person','bicycle','car','motorcycle','bus','truck',
    'traffic light','stop sign','fire hydrant','bench','dog','cow','horse','sheep','potted plant'
]
CLASS_IDX = [COCO_CLASSES.index(c) for c in RELEVANT_CLASSES]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Road Obstacle Detection", layout="wide")
st.title("🚦 Road Obstacle Detection")

option = st.sidebar.radio("Choose Input Type:", ["Upload Image", "Live Webcam"])
import time

# Image Upload Detection
if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    with st.spinner("Processing..."):
        time.sleep(3)

    if uploaded_file is not None:
        # Read file as image
        img = Image.open(uploaded_file).convert("RGB")
        img_array = np.array(img)

        # Run detection directly on numpy array
        results = model(img_array, classes=CLASS_IDX, conf=0.4)

        # Plot results
        result_img = results[0].plot()

        st.image(result_img, caption="Detected Obstacles", use_column_width=True)

# Live Webcam Detection
elif option == "Live Webcam":
    st.write("Click start to use webcam for live detection")

    run = st.checkbox("Start Webcam")

    FRAME_WINDOW = st.image([])

    cap = cv2.VideoCapture(0)  # 0 = default webcam

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture frame from webcam.")
            break

        # Run YOLO detection
        results = model(frame, classes=CLASS_IDX, conf=0.4)
        result_frame = results[0].plot()

        # Convert BGR -> RGB
        FRAME_WINDOW.image(cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB))

    cap.release()
