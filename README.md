# Deep Learning Brain Tumor Detector

[![Python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/tensorflow-2.12-orange)](https://www.tensorflow.org/)

## Project Overview
This project presents a **Convolutional Neural Network (CNN)** designed to detect brain tumors from MRI images. Early diagnosis of brain tumors is critical for improving patient outcomes, and this model demonstrates how deep learning can enhance diagnostic accuracy in medical imaging.

The CNN model was trained with a preprocessed dataset and achieved a **test accuracy of 90%**, effectively classifying tumor and non-tumor cases. Hyperparameter tuning, data augmentation, and dropout layers were applied to improve performance and generalization.

---

## Features
- Detects presence of brain tumors from MRI scans.
- CNN architecture with 4 convolutional layers (filters: 32, 64, 128, 128) and a Dense layer with 128 neurons.
- Dropout rates: 0.1, 0.2, 0.3, 0.4 across layers.
- Adam optimizer with learning rate 0.005.
- Batch size of 32.
- Data augmentation: flipping, zooming, shearing, width and height shifts.
- Preprocessing includes image resizing (224x224) and normalization.

---

## Dataset
- Original dataset contains **150 tumor images ("yes")** and **73 non-tumor images ("no")**, creating an imbalance.
- Dataset was split into:
  - 80% Training
  - 10% Validation
  - 10% Test
- Images were resized and normalized for consistent input.

---

## Methodology
1. **Data Preprocessing:** resizing, normalization, data augmentation (shifts, flips, zooms, shear).
2. **Model Construction:** 4 convolutional layers + Dense layer, progressive dropout.
3. **Training:** Adam optimizer, learning rate 0.005, batch size 32, early stopping with patience=5.
4. **Evaluation:** Confusion matrix, accuracy, precision, recall, F1 score.

---

## Installation and Usage

### Install Dependencies
Make sure you have Python 3.x installed. Install required packages such as TensorFlow/Keras:

```bash
pip install tensorflow numpy matplotlib pandas scikit-learn jupyter
