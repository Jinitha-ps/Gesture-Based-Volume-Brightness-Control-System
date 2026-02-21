# 🖐 Gesture-Based Volume & Brightness Control System

This project is a real-time computer vision application that allows users to control system volume and screen brightness using hand gestures through a webcam.

Using MediaPipe’s hand landmark detection, the system tracks finger positions and dynamically maps finger distance to system-level controls.

**🚀 Features**

*  Real-time hand tracking using MediaPipe

*  Volume control using thumb–index finger distance

*  Brightness control using thumb–middle finger distance

*  Dynamic interpolation for smooth control transitions

*  Visual UI bars for volume and brightness levels

*  FPS display for performance monitoring

*  Live webcam processing using OpenCV

**🛠 Technologies Used**

*  Python 3.10

*  OpenCV

*  MediaPipe

*  NumPy

*  Pycaw (Windows Audio Control)

*  screen-brightness-control

**🎯 How It Works**

*  The distance between the thumb and index finger controls system volume.

*  The distance between the thumb and middle finger controls screen brightness.

*  Distance values are interpolated to system-level ranges.

*  Visual indicators display current volume and brightness percentages.

**📌 Use Cases**

*  Touchless system control

*  Accessibility support systems

*  Smart interfaces

