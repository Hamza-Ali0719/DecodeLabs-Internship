import cv2
import numpy as np
import pytesseract
import os
import logging
from datetime import datetime

# ==========================================
# PROFESSIONAL LOGGING SETUP
# ==========================================
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, 'vision_log.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# ==========================================
# CLASS: VisionRecognizer (The Optic Nerve)
# ==========================================
class VisionRecognizer:
    def __init__(self):
        """Initialize the Vision Engine with pre-trained models."""
        logging.info("Initializing VisionRecognizer...")
        
        # Paths for MobileNet-SSD
        self.prototxt_path = os.path.join(script_dir, "deploy.prototxt")
        self.model_path = os.path.join(script_dir, "mobilenet_iter_73000.caffemodel")
        
        # Class labels for MobileNet-SSD (20 objects)
        self.classes = [
            "background", "aeroplane", "bicycle", "bird", "boat",
            "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
            "dog", "horse", "motorbike", "person", "pottedplant",
            "sheep", "sofa", "train", "tvmonitor"
        ]
        
        # Load the pre-trained model
        self.net = None
        self.load_model()
        
        # Configure Tesseract (if installed in default path)
        # For Windows users, uncomment and set path if needed:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        logging.info("VisionRecognizer ready.")

    def load_model(self):
        """Load the MobileNet-SSD model."""
        try:
            if os.path.exists(self.prototxt_path) and os.path.exists(self.model_path):
                self.net = cv2.dnn.readNetFromCaffe(self.prototxt_path, self.model_path)
                logging.info("MobileNet-SSD model loaded successfully.")
            else:
                logging.warning("Model files not found. Please download them.")
                logging.warning("Download 'deploy.prototxt' and 'mobilenet_iter_73000.caffemodel'.")
                self.net = None
        except Exception as e:
            logging.error(f"Error loading model: {e}")
            self.net = None

    def preprocess_image(self, image_path):
        """Read image and prepare it for processing."""
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found: {image_path}")
        return image

    def perform_ocr(self, image):
        """Extract text from image using Tesseract."""
        logging.info("Performing OCR...")
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Apply threshold to preprocess
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        # Extract text
        try:
            text = pytesseract.image_to_string(thresh, lang='eng')
            text = text.strip()
            logging.info(f"OCR Extracted {len(text)} characters.")
            return text
        except Exception as e:
            logging.error(f"OCR failed: {e}")
            return ""

    def detect_objects(self, image):
        """Detect objects using MobileNet-SSD."""
        if self.net is None:
            logging.error("Model not loaded. Skipping object detection.")
            return [], image

        logging.info("Performing Object Detection...")
        (h, w) = image.shape[:2]
        
        # Create 4D blob from image
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
        self.net.setInput(blob)
        detections = self.net.forward()

        objects_detected = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  # 50% confidence threshold
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                
                label = self.classes[idx] if idx < len(self.classes) else "Unknown"
                objects_detected.append({
                    "label": label,
                    "confidence": round(confidence * 100, 2),
                    "bbox": (startX, startY, endX, endY)
                })
                
                # Draw rectangle and label on image
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
                text = f"{label}: {confidence:.2f}"
                cv2.putText(image, text, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                logging.info(f"Detected {label} with {confidence*100:.2f}% confidence.")

        return objects_detected, image

    def run_pipeline(self, image_path):
        """Main execution method."""
        logging.info(f"Starting Vision Pipeline for: {image_path}")
        
        # 1. Read Image
        image = self.preprocess_image(image_path)
        original_image = image.copy()
        
        # 2. Perform OCR
        extracted_text = self.perform_ocr(original_image)
        
        # 3. Perform Object Detection
        objects, annotated_image = self.detect_objects(original_image)
        
        # 4. Save Outputs
        # Save Annotated Image
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_img_path = os.path.join(script_dir, f"{base_name}_output.jpg")
        cv2.imwrite(output_img_path, annotated_image)
        logging.info(f"Annotated image saved to: {output_img_path}")
        
        # Save Text Report
        report_path = os.path.join(script_dir, f"{base_name}_results.txt")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("="*50 + "\n")
            f.write("DECODELABS VISION RECOGNITION REPORT\n")
            f.write(f"Timestamp: {datetime.now()}\n")
            f.write(f"Input File: {image_path}\n")
            f.write("="*50 + "\n\n")
            
            f.write("[OBJECTS DETECTED]\n")
            if objects:
                for idx, obj in enumerate(objects, 1):
                    f.write(f"{idx}. {obj['label']} (Confidence: {obj['confidence']}%)\n")
                    bbox = obj['bbox']
                    f.write(f"   Location: X={bbox[0]}, Y={bbox[1]}, W={bbox[2]-bbox[0]}, H={bbox[3]-bbox[1]}\n")
            else:
                f.write("No objects detected with confidence > 50%.\n")
            
            f.write("\n[EXTRACTED TEXT]\n")
            if extracted_text:
                f.write(extracted_text)
            else:
                f.write("No text extracted.\n")
        
        logging.info(f"Report saved to: {report_path}")
        
        # Print final summary to console
        print("\n" + "="*50)
        print("✅ VISION PIPELINE COMPLETE")
        print("="*50)
        print(f"📸 Output Image: {output_img_path}")
        print(f"📄 Report File: {report_path}")
        print(f"🔍 Objects Found: {len(objects)}")
        print(f"📝 Text Found: {len(extracted_text)} characters")
        print("="*50)

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # Initialize the engine
    engine = VisionRecognizer()
    
    # Path to your test image
    # Keep a sample image named 'sample.jpg' in the same folder, or change this path
    test_image = os.path.join(script_dir, "sample.jpg")
    
    if not os.path.exists(test_image):
        logging.error(f"Test image not found at: {test_image}")
        print("\n⚠️  Please add a 'sample.jpg' file in this folder to test.")
        print("Or modify the 'test_image' variable in the script.")
    else:
        engine.run_pipeline(test_image)