# Face Recognition and Extraction Tool

## Overview
This Python tool automatically detects and extracts faces from images using OpenCV. It processes all images in an input directory, detects faces using Haar Cascades, and saves the extracted faces as standardized 48x48 pixel images.

## Features
- Automatic face detection in multiple image formats (PNG, JPG, JPEG, TIFF, BMP)
- Standardized face extraction and resizing
- Batch processing of multiple images
- Output in both image and text format
- Support for grayscale processing

## Prerequisites
- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

Install required packages:
```bash
pip install opencv-python numpy
```

## Project Structure
```
face-recognition-master/
│
├── Input/                 # Place input images here
├── Output/               # Extracted faces and data will be saved here
├── Haar_Cascades/        # Contains face detection classifier
├── Facial_Recognition_py3.py
└── README.md
```

## Setup
1. Clone this repository
2. Create required directories:
```powershell
mkdir Input
mkdir Output
mkdir Haar_Cascades
```

3. Download the Haar Cascade classifier:
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml" -OutFile "Haar_Cascades\haarcascade_frontalface_default.xml"
```

## Usage
1. Place your images in the `Input` folder
2. Run the script:
```powershell
python Facial_Recognition_py3.py
```
3. Check the `Output` folder for results:
   - Individual face images (`face_0.jpg`, `face_1.jpg`, etc.)
   - Text file with pixel data (`output_file.txt`)

## Output Format
- Face images are saved as 48x48 pixel JPG files
- Each line in `output_file.txt` contains space-separated pixel values for one face

## Supported Image Formats
- PNG
- JPG/JPEG
- TIFF
- BMP

## Limitations
- Best results with front-facing faces
- Requires good lighting conditions
- May not detect faces at extreme angles
- Maximum face detection size of 300x300 pixels

## License
This project is open source and available under the MIT License.

## Contributing
Feel free to submit issues and enhancement requests.