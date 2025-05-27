# 🚦 Traffic Sign Recognition Using CNN

## 🧠 Objectives
- Develop a CNN-based model to recognize and classify traffic signs from images.
- Train and evaluate on a custom dataset for high classification accuracy.
- Contribute towards real-time autonomous systems and driver assistance technologies.

## 🚧 Problem Statement
Traffic sign recognition is a crucial feature in autonomous driving systems. Recognizing traffic signs in real time with high precision is essential for the safety and reliability of such systems. This project builds a CNN model capable of identifying traffic signs under diverse environmental conditions using a custom dataset. The goal is to develop a model that generalizes well and can be deployed in real-world scenarios.

## 🏗️ System Model
- **Input Size:** 64x64 RGB images
- **CNN Architecture:**  
  `Conv2D` → `MaxPooling2D` → `Dropout` → `Dense` layers
- **Activation Functions:** ReLU for hidden layers, Softmax for output
- **Optimizer:** Adam
- **Loss Function:** Categorical Cross-Entropy

## ⚙️ Simulation Parameters and Results
- **Training/Validation Split:** 80% training, 20% validation
- **Epochs:** 15
- **Batch Size:** 32
- **Final Training Accuracy: 98.91%**
- **Final Validation Accuracy: 99.85%**
- **Final Training Loss: 0.0338**
- **Final Validation Loss: 0.0052**

### 📊 Visualizations
- Training & Validation Accuracy vs. Epochs
- Training & Validation Loss vs. Epochs
- Confusion Matrix showing class-wise performance

## ✅ Conclusion
- CNNs demonstrate strong performance in classifying traffic signs.
- Achieved **98.91% accuracy** on a custom dataset, confirming robustness.
- Promising results suggest suitability for **real-world integration**.

## 🚀 Future Work
- Real-time traffic sign detection using live camera input.
- Mobile and embedded deployment for low-power systems.
- Expanding to multilingual and international traffic sign datasets.

## 👨‍💻 Author
**Sohaib**  
AI Student & Deep Learning Enthusiast  




---

