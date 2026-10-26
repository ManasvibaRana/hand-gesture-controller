# Hand Gesture Controller

**Swipe the air, press the keys.** Wave your hand in front of the webcam and it presses the arrow keys for you, so you can play browser games or flip through slides without touching the keyboard.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?logo=google&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-keyboard%20control-555)

<!-- Add a GIF here, e.g. ![Demo](docs/demo.gif) -->

## What it does

| Your hand moves | Key pressed |
| --- | --- |
| Swipe right | → |
| Swipe left | ← |
| Swipe up | ↑ |
| Swipe down | ↓ |

Great for endless-runner browser games (lane switching, jumping, sliding), presentation slides, or anything else driven by arrow keys.

## How it works

1. **cvzone's `HandDetector`** (built on Google MediaPipe) finds your hand in each webcam frame.
2. The script follows the **centre of your hand** from one frame to the next.
3. If it moves more than **40 pixels** in one frame, that counts as a swipe in the direction it moved most.
4. **PyAutoGUI** presses the matching arrow key, and the gesture name is shown on screen.

## Getting started

### Prerequisites

- Python 3.8–3.11 (MediaPipe doesn't support every newer version yet)
- A webcam

### Install and run

```bash
git clone https://github.com/ManasvibaRana/hand-gesture-controller.git
cd hand-gesture-controller
python -m venv venv
venv\Scripts\activate          # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Click into the game or slideshow you want to control, then swipe in front of the camera. Press **q** in the camera window to quit.

### Tweaking

In `main.py`:

- **Sensitivity:** change the swipe threshold (`40` pixels). Lower is more sensitive.
- **Detection confidence:** `HandDetector(detectionCon=0.8, ...)`
- **Camera:** `cv2.VideoCapture(0)`. Use `1` for an external webcam.

## Tech stack

Python · OpenCV · cvzone · MediaPipe · PyAutoGUI · NumPy

## Ideas for next steps

- [ ] Pinch to click, and finger distance to control volume
- [ ] A short cooldown so one swipe sends exactly one key press
- [ ] Mirror the preview for a more natural feel

## Author

**Manasviba Rana**: [LinkedIn](https://www.linkedin.com/in/manasviba-rana) · [GitHub](https://github.com/ManasvibaRana)
