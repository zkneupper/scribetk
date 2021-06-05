# `video-subtitler`

A video annotation tool built with [python](https://www.python.org/), [flask](https://pypi.org/project/Flask/), and [wavesurfer.js](https://github.com/katspaugh/wavesurfer.js).

## Installation & Usage

1. How to clone the `video-subtitler` repository:

```bash
# Clone the repository
git clone https://github.com/zkneupper/video-subtitler.git
```

2. If necessary, create new virtual environment containing `python>=3.6` and `flask`.


For `conda` users:

```bash
# Create a new environment called `flask_env`
conda create --name flask_env --file requirements.txt
```


3. Activate the virtual environment containing `python>=3.6` and `flask`.


For `conda` users:

```bash
conda activate flask_env
```


4. How to start the `video-subtitler` server:

```bash
# Activate a python 3.6+ virtual environtment with flask installed

# Go into the video-subtitler/app/ directory
cd video-subtitler/app/

# Start the application server
python app.py
```


5. Open the `video-subtitler` app in your default browser

```bash
# Open the `video-subtitler` app in your default browser
open http://127.0.0.1:5000/
```
