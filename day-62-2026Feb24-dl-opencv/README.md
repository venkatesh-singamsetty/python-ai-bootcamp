- https://opencv.org/
- https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
- https://github.com/opencv/opencv/tree/master/data/haarcascades
- https://github.com/andrewssobral/vehicle_detection_haarcascades/tree/master/vs2013

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install numpy opencv-python

python haarcascade-frontalface.py

python haarcascade-eye.py
```
