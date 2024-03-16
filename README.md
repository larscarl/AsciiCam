# ASCII Cam Mirror

ASCII Cam Mirror is a Python application that captures video from your computer's webcam, mirrors the image like a reflection, and converts it to real-time ASCII art. This project uses OpenCV for capturing video frames and processes them into ASCII characters to create a fun and artistic representation of the webcam feed.

## Features

- Real-time video capture from the webcam.
- Mirror effect to make the video feed behave like a looking glass.
- Conversion of video frames to ASCII art.
- Adjustable image width and character mapping for different artistic effects.

## Getting Started

### Prerequisites

- Python 3.6 or higher.
- A webcam connected to your computer.

### Installation

1. Clone this repository or download the source code.

`git clone [https://github.com/larscarl/AsciiCam/](https://github.com/larscarl/AsciiCam/)`

2. Navigate to the project directory.

`cd ascii-cam-mirror`

3. Install the required Python packages.

`pip install -r requirements.txt`


### Running the Application

To start the ASCII art mirror, simply run the `videoToAscii.py` script from your terminal:

`python videoToAscii.py`

The application will run directly in the terminal displaying the video feed from your webcam converted into ASCII art in real-time. To quit, press "ctrl+c".

## How It Works

The application captures video frames from the webcam using OpenCV, then each frame is:

1. Mirrored horizontally to create a reflection effect.
2. Converted to grayscale to simplify processing.
3. Resized to maintain the aspect ratio and to speed up the ASCII conversion process.
4. Converted into ASCII characters based on the brightness of each pixel.

The ASCII characters used for the conversion are defined in the `ASCII_CHARS` string, and can be adjusted to change the visual style of the output.

## Customization

You can customize the appearance of the ASCII art by modifying the `ASCII_CHARS` string or by adjusting the `new_width` parameter in the `resize_image` function to change the resolution of the ASCII art output.

## Requirements

This project requires `opencv-python-headless` version `4.9.0.80`. Make sure to install all dependencies from the `requirements.txt` file.
