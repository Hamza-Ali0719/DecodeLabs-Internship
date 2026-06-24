# Project 4: Visual Recognition Engine (OCR + Object Detection)

**Author:** Hamza Ali  
**Batch:** 2026  
**Internship:** DecodeLabs  

## Overview
This project implements a hybrid visual recognition pipeline that performs both **Optical Character Recognition (OCR)** to extract text and **Object Detection** using MobileNet-SSD to identify objects within a single image.

## Features
- **Dual Processing:** Extracts text and detects objects simultaneously.
- **Visual Annotations:** Draws bounding boxes with confidence scores on the output image.
- **Professional Logging:** Maintains a detailed log (`vision_log.log`) for debugging.
- **Report Generation:** Saves all extracted data into a structured `.txt` report.

## Tech Stack
- Python 3
- OpenCV (cv2.dnn)
- Tesseract OCR
- MobileNet-SSD (Pre-trained)
- NumPy

## How to Run
1. Install dependencies:
   ```bash
   pip install opencv-python pytesseract numpy
