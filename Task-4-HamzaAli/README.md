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




## 📁 Project Structure

```
Task-4-HamzaAli/
│
├── vision_recognizer.py              # Main AI system (OOP)
├── deploy.prototxt                   # Model architecture config
├── mobilenet_iter_73000.caffemodel   # Pre-trained weights (22MB)
├── sample.jpg                        # Test input image
├── sample_output.jpg                 # Output with bounding boxes (auto)
├── sample_results.txt                # Extracted text & objects (auto)
├── vision_log.log                    # Execution logs (auto)
└── README.md                         # Documentation
```

---

## ⚙️ Tech Stack

| Technology       | Purpose                                     |
| ---------------- | ------------------------------------------- |
| Python 3         | Core programming language                   |
| OpenCV (cv2.dnn) | Image processing & neural network inference |
| pytesseract      | Optical Character Recognition (OCR)         |
| MobileNet-SSD    | Pre-trained object detection model          |
| NumPy            | Numerical computations                      |

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Hamza-Ali0719/DecodeLabs-Internship.git
cd DecodeLabs-Internship
cd Task-4-HamzaAli
```

---

### 2️⃣ Install Dependencies

```bash
pip install opencv-python pytesseract numpy
```

⚠️ **Windows (Multiple Python Versions):**

```bash
C:\Users\raoh1\AppData\Local\Programs\Python\Python314\python.exe -m pip install opencv-python pytesseract numpy
```

---

### 3️⃣ Install Tesseract OCR

Download from: **UB-Mannheim Tesseract**

* Run installer: `tesseract-ocr-w64-setup-5.3.3.20231005.exe`
* Install with default settings

---

### 4️⃣ Download Model Files

Place in project root:

* `deploy.prototxt`
* `mobilenet_iter_73000.caffemodel`

---

### 5️⃣ Run the Project

```bash
python vision_recognizer.py
```

---

## 🧪 Example Usage

**Input:** Image containing a person holding a signboard

**Terminal Output:**

```
2026-06-24 14:10:34,672 - INFO - MobileNet-SSD model loaded successfully.
2026-06-24 14:10:35,130 - INFO - OCR Extracted 17 characters.
2026-06-24 14:10:35,357 - INFO - Detected person with 96.31% confidence.

✅ VISION PIPELINE COMPLETE
📸 Output Image: sample_output.jpg
📄 Report File: sample_results.txt
🔍 Objects Found: 1
📝 Text Found: 17 characters
```

---

## 📊 Algorithm Explanation

| Component         | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| Preprocessing     | Converts image to grayscale + thresholding for noise reduction |
| Blob Conversion   | Converts image into 4D tensor for model input                  |
| MobileNet-SSD     | Detects objects using pre-trained deep learning                |
| Confidence Filter | Filters detections > 50% confidence                            |
| Tesseract OCR     | Extracts UTF-8 text from image                                 |

---

## 🏗️ System Architecture

```
        INPUT (Image)
              │
              ▼
     PREPROCESSING
 (Grayscale + Threshold)
        │        │
        ▼        ▼
     OCR       Object Detection
 (Tesseract)   (MobileNet-SSD)
        │        │
        ▼        ▼
        OUTPUT (Image + Text File)
```

---

## 🧪 Testing & Validation

| Test Case          | Input              | Expected Result                | Status   |
| ------------------ | ------------------ | ------------------------------ | -------- |
| Text-heavy Image   | Book cover         | Extract >10 characters         | ✅ Passed |
| Object-heavy Image | Person / Car       | Detect objects >50% confidence | ✅ Passed |
| Hybrid Image       | Signboard + person | Detect both text & object      | ✅ Passed |
| Invalid File       | Missing image      | Graceful error handling        | ✅ Passed |
| Low Confidence     | Blurry image       | No false positives             | ✅ Passed |

---

## 🚧 Challenges & Solutions

| Challenge                        | Solution                             |
| -------------------------------- | ------------------------------------ |
| ModuleNotFoundError: cv2         | Installed using absolute Python path |
| Hidden File Extensions (Windows) | Removed `.txt` from `.prototxt` file |
| Tesseract Not Found              | Installed UB-Mannheim executable     |
| OCR Returned 0 Text              | Used clearer test image              |

---

## 🔮 Future Improvements

* 🌐 Web Interface (Flask / Streamlit)
* 🎥 Real-Time Detection (Webcam Integration)
* 🤖 Upgrade to YOLOv8 (80+ object classes)
* ☁️ Cloud Deployment (AWS / GCP)
* 🎨 Advanced Visualization (heatmaps, masks)

---

## 📜 Conclusion

This project demonstrates how to integrate **deep learning models + OCR** into a complete AI pipeline.

It bridges the gap between:

* **Unstructured visual data**
* **Structured computational output**

---

## 👨‍💻 Author

**Hamza Ali**
📍 DecodeLabs Internship (Batch 2026)
📅 June 2026

🔗 GitHub: https://github.com/Hamza-Ali0719

---

## 📎 License

This project is for **educational purposes** under the DecodeLabs Industrial Training Program.

---

