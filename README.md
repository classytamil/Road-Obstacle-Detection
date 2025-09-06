# 🚦 Road Obstacle Detection with YOLOv8 + Streamlit  

This project is a **real-time road obstacle detection system** built with [Streamlit](https://streamlit.io/) and [YOLOv8](https://github.com/ultralytics/ultralytics).  
It allows you to:  
- Upload an image and detect relevant road obstacles.  
- Use your **webcam** for live obstacle detection.  

## ✨ Features  
- ✅ YOLOv8n pretrained on COCO dataset  
- ✅ Detects **road-related objects** (cars, buses, trucks, traffic lights, stop signs, people, animals, etc.)  
- ✅ **Image Upload** and **Live Webcam** detection modes  
- ✅ Simple and interactive UI with Streamlit  

---

## 🛠️ Installation  

Clone the repository:  
```bash
git clone https://github.com/your-username/road-obstacle-detection.git
cd road-obstacle-detection
```

Create and activate a virtual environment:  
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

Install dependencies:  
```bash
pip install -r requirements.txt
```

---

## 📦 Requirements  

The main Python packages used are:  
- `streamlit`  
- `ultralytics`  
- `opencv-python`  
- `numpy`  
- `Pillow`  

Example `requirements.txt`:  
```txt
streamlit
ultralytics
opencv-python
numpy
Pillow
```

---

## 🚀 Usage  

Run the Streamlit app:  
```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

### Modes:
- **Upload Image** → Upload a `.jpg` / `.jpeg` / `.png` image and detect obstacles.  
- **Live Webcam** → Turn on your webcam and see detections in real-time.  

---

## 📸 Example  

**Detection on Uploaded Image:**  
![Example Image Detection](https://via.placeholder.com/800x400.png?text=Example+Detection)  

**Live Webcam Detection:**  
![Example Webcam](https://via.placeholder.com/800x400.png?text=Live+Webcam+Detection)  

---

## 🧠 Object Classes  

The app focuses on **road-related classes** from the COCO dataset, such as:  
- Person, Car, Bicycle, Motorcycle, Bus, Truck  
- Traffic Light, Stop Sign, Fire Hydrant  
- Dog, Cow, Horse, Sheep  
- Bench, Potted Plant  

---

## 📌 Notes  
- Model used: **YOLOv8n** (small, fast, good for demo).  
- You can replace with `yolov8s.pt`, `yolov8m.pt`, etc. for higher accuracy.  
- Make sure you have a working webcam for live mode.  

---

## 📜 License  
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.  
