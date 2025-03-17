# LiveFX-Recorder
🎥 LiveFX Recorder – Real-time Video Recording with Cool Effects

A simple real-time video recorder with interactive filters, inspired by Mac's Photo Booth.  
Easily apply live effects and record videos using your webcam.

## ✨ Features
- **🔴 Video Recording**: Click the "REC" button to start/stop recording.
- **🎨 Live Filters**: Apply filters in real time with a button click or spacebar.
  - `Normal`
  - `Negative (Invert Colors)`
  - `Flip (Mirror Mode)`
- **🎥 Save Videos**: Videos are saved in **MP4 format** (`output.mp4`).
- **🖱 Mouse Support**: Click buttons on the screen to toggle recording and filters.
- **⌨️ Keyboard Support**: 
  - Press `SPACE` to change filters.
  - Press `ESC` to exit.

## 🛠 Installation
### 1️⃣ Install OpenCV
Make sure you have OpenCV installed in Python:
```bash
pip install opencv-python numpy
```

## 🎬 Controls

| Action                  | Mouse                   | Keyboard |
|-------------------------|------------------------|----------|
| **Start/Stop Recording** | Click the "REC" button | N/A      |
| **Change Filter**       | Click the "FILTER" button | `SPACE`  |
| **Exit Program**        | N/A                    | `ESC`    |

## 🖼️ Interface
- **🔴 Red Button**: Starts/Stops Recording  
- **🎨 Gray/Blue/Green Button**: Changes Filters  
- **Live Video Feed**: Displays the current camera feed with applied effects  

## 🔧 Troubleshooting

### ❓ 1. The output video doesn't play in QuickTime Player (Mac)?
✅ Use `H264` codec instead of `mp4v`:
```python
video_writer = cv.VideoWriter('output.mp4', cv.VideoWriter_fourcc(*'H264'), 20.0, (640, 480))
```

### ❓ 2. The camera doesn't open?
✅ Try changing the camera source:
```python
camera = cv.VideoCapture(1)  # Change from 0 to 1 if you have multiple cameras
```

## 📝 License
This project is licensed under the **MIT License** – feel free to modify and distribute!

