# `video-subtitler`

A video annotation tool built with [python](https://www.python.org/), [flask](https://pypi.org/project/Flask/), and [wavesurfer.js](https://github.com/katspaugh/wavesurfer.js).

This tool is adapted from the `wavesurfer.js` video annotation [example](http://wavesurfer-js.org/example/video-annotation/index.html).




## Installation / Setup

Clone the `video-subtitler` repository:

```bash
# Clone the repository
git clone https://github.com/zkneupper/video-subtitler.git
```

If necessary, create a new virtual environment containing `python>=3.6`, `flask`, and `click`.

For `conda` users:

```bash
# Create a new environment called `flask_env`
conda create --name flask_env --file requirements.txt
```


Activate the virtual environment containing `python>=3.6` and `flask`.

For `conda` users:

```bash
conda activate flask_env
```


## Usage


### Example 1: Running `video-subtitler` with the default options

To run the app with the default setting and using the demo video, do the following:

```bash
# Activate your virtual environment

# Go into the video-subtitler/app/ directory
cd video-subtitler/app/

# Start the application server
python app.py
```

Running `python app.py` will start the server and open the app in your browser



### Example 2: Running `video-subtitler` for your own video and annotation

Suppose that you have a video `video.mp4` located at this path: `/full/path/to/video.mp4`

Additionally, suppose that you want to create an annotation file called `video_annotation.json` located at this path: `/full/path/to/video_annotation.json`


To run the `video-subtitler` app for your own video and annotation, do the following:

```bash
# Activate your virtual environment

# Go into the video-subtitler/app/ directory
cd video-subtitler/app/

# python app.py --filepath_video <filepath_video> --filepath_annotation <filepath_annotation>
python app.py --filepath_video /full/path/to/video.mp4 --filepath_annotation /full/path/to/video_annotation.json
```


### CLI Options

Below are the command line interface (cli) options for the `video-subtitler` app:

```
Usage: app.py [OPTIONS]

Options:
  --filepath_video TEXT       The file path to the video you want to annotate.
  --filepath_annotation TEXT  The file path to the json file containing the
                              video annotations.

  --port INTEGER              port number
  -d, --debug                 Run the app in DEBUG mode.
  --browser / --no-browser    Automatically open in browser
  --help                      Show this message and exit.
```
