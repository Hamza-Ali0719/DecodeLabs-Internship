# Project 4: Visual Recognition Engine (OCR + Object Detection)

**AI-Powered Image Understanding using MobileNet-SSD & Tesseract OCR**

---

## 📌 Overview
The Visual Recognition Engine is an AI-based hybrid system that simulates the **"Optic Nerve"** of a machine. It can simultaneously read printed text from images and detect physical objects in real-time.

It uses:
- 🖼️ **OpenCV DNN** (Deep Neural Network module) for object detection.
- 📖 **Tesseract OCR** for text extraction.
- 🧠 **Transfer Learning** (MobileNet-SSD) to identify 20 different object classes.

👉 **Example:** Input: A photo of a person holding a "STOP" sign.  
Output: Detects *Person* (96% confidence) + Extracts *"STOP"* text.

---

## 🎯 Features
- ✔️ **Dual Recognition Pipeline:** OCR and Object Detection run simultaneously.
- ✔️ **Visual Annotations:** Draws professional green bounding boxes with confidence scores.
- ✔️ **Confidence Thresholding:** Ignores detections below 50% to avoid false positives.
- ✔️ **Professional Logging:** Maintains both console and file-based logging (`vision_log.log`) for debugging.
- ✔️ **Structured Reporting:** Saves all extracted text and object coordinates into a clean `.txt` report.
- ✔️ **Pre-trained Efficiency:** Uses MobileNet-SSD, eliminating the need for expensive GPU training.

---

## 🧠 How It Works
1. **Input:** The system reads a standard image (`.jpg` or `.png`).
2. **Preprocessing:** Converts the image to grayscale and applies thresholding for OCR; creates a 4D `blob` for object detection.
3. **Parallel Processing:**
   - *Path 1 (Text):* `pytesseract` extracts all machine-readable characters.
   - *Path 2 (Objects):* MobileNet-SSD scans the image and identifies known objects.
4. **Output:** Overlays bounding boxes on the image and saves a text report.

---

## 🔄 Pipeline
```text
User Image → Preprocessing → [OCR Engine] → Extracted Text
                           → [MobileNet-SSD] → Bounding Boxes & Labels
                                       ↓
                    Annotated Image + Structured Report
