# 🧠 Project 4: Visual Recognition Engine (OCR + Object Detection)

**AI-Powered Image Understanding using MobileNet-SSD & Tesseract OCR**

---

## 📌 Overview

The **Visual Recognition Engine** is a hybrid AI system that simulates the **“Optic Nerve”** of a machine. It can simultaneously:

* 📖 Extract text from images (OCR)
* 🧍 Detect real-world objects

### 🔧 Technologies Used:

* 🖼️ **OpenCV DNN** – Object detection
* 📖 **Tesseract OCR** – Text extraction
* 🧠 **MobileNet-SSD (Transfer Learning)** – 20-class object recognition

👉 **Example:**

**Input:** Image of a person holding a "STOP" sign
**Output:**

* Detects **Person (96% confidence)**
* Extracts **"STOP"**

---

## 🎯 Features

* ✔️ **Dual AI Pipeline** (OCR + Object Detection)
* ✔️ **Clean Visual Output** with bounding boxes & labels
* ✔️ **Confidence Filtering** (>50% only)
* ✔️ **Professional Logging System** (`vision_log.log`)
* ✔️ **Structured Report Generation** (`.txt`)
* ✔️ **No Training Required** (Pre-trained model)

---

## 🧠 How It Works

1. **Input Image** (`.jpg` / `.png`)
2. **Preprocessing**

   * Grayscale conversion
   * Thresholding for OCR
   * Blob creation for neural network
3. **Parallel Processing**

   * 📖 OCR → Extract text using `pytesseract`
   * 🧍 Detection → Identify objects using MobileNet-SSD
4. **Output**

   * Annotated image
   * Text report

---

## 🔄 Pipeline

```text
User Image → Preprocessing → [OCR Engine] → Extracted Text
                           → [MobileNet-SSD] → Bounding Boxes & Labels
                                       ↓
                    Annotated Image + Structured Report
```

---

## 📁 Project Structure

```text
Task-4-HamzaAli/
│
├── vision_recognizer.py              # Main AI system (OOP)
├── deploy.prototxt                   # Model architecture config
├── mobilenet_iter_73000.caffemodel   # Pre-trained weights (22MB)
├── sample.jpg                        # Test input image
├── sample_output.jpg                 # Output with bounding boxes
├── sample_results.txt                # Extracted text & objects
├── vision_log.log                    # Execution logs
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
cd DecodeLabs-Internship/Task-4-HamzaAli
```

---

### 2️⃣ Install Dependencies

```bash
pip install opencv-python pytesseract numpy
```

⚠️ **Windows Users (Multiple Python Versions):**

```bash
C:\Users\raoh1\AppData\Local\Programs\Python\Python314\python.exe -m pip install opencv-python pytesseract numpy
```

---

### 3️⃣ Install Tesseract OCR

* Download from: **UB-Mannheim Tesseract**
* Run installer:

  ```
  tesseract-ocr-w64-setup-5.3.3.20231005.exe
  ```
* Install with default settings

---

### 4️⃣ Add Model Files

Place these in the root folder:

* `deploy.prototxt`
* `mobilenet_iter_73000.caffemodel`

---

### 5️⃣ Run the Project

```bash
python vision_recognizer.py
```

---

## 🧪 Example Usage

**Input:** Image with a person holding a signboard

**Output (Terminal):**

```text
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

| Component         | Description                        |
| ----------------- | ---------------------------------- |
| Preprocessing     | Grayscale + thresholding           |
| Blob Conversion   | Image → 4D tensor                  |
| MobileNet-SSD     | Object detection                   |
| Confidence Filter | Removes low-confidence predictions |
| Tesseract OCR     | Extracts UTF-8 text                |

---

## 🏗️ System Architecture

```text
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

| Test Case        | Input              | Expected Result        | Status   |
| ---------------- | ------------------ | ---------------------- | -------- |
| Text-heavy Image | Book cover         | Extract >10 characters | ✅ Passed |
| Object-heavy     | Person / Car       | Detect >50% confidence | ✅ Passed |
| Hybrid Image     | Signboard + person | Detect both            | ✅ Passed |
| Invalid File     | Missing image      | Graceful error         | ✅ Passed |
| Low Confidence   | Blurry image       | No false positives     | ✅ Passed |

---

## 🚧 Challenges & Solutions

| Challenge                   | Solution                         |
| --------------------------- | -------------------------------- |
| ModuleNotFoundError: cv2    | Installed using full Python path |
| Hidden Extensions (Windows) | Fixed `.prototxt.txt` issue      |
| Tesseract Not Found         | Installed UB-Mannheim version    |
| OCR Output Empty            | Used clearer input image         |

---

## 🔮 Future Improvements

* 🌐 Web Interface (Flask / Streamlit)
* 🎥 Real-Time Detection (Webcam)
* 🤖 Upgrade to YOLOv8 (80+ classes)
* ☁️ Cloud Deployment (AWS / GCP)
* 🎨 Advanced Visualization (heatmaps, masks)

---

## 📜 Conclusion

This project demonstrates a complete **AI perception pipeline**:

* 🔍 Understanding images (object detection)
* 📖 Reading text (OCR)
* 📊 Producing structured outputs

It bridges the gap between:

* **Unstructured visual data**
* **Structured machine-readable results**

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
