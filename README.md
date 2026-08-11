# InSAR-TS Toolbox

[![QGIS](https://img.shields.io/badge/QGIS-3.x-green.svg)](https://qgis.org) 
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A QGIS plugin for **time series analysis of InSAR data** (Persistent Scatterer and Distributed Scatterer points).  
It provides clustering, descriptive statistics, spectral analysis, and visualization tools for InSAR time series data within QGIS.

---

## 📑 Overview of Tabs

### 🔹 Clustering
Select numeric fields from a point layer and run clustering with **KMeans** or **DBSCAN**.  
Results are written to a `cluster_id` field and visualized with automatic color symbology (noise is shown in grey).

### 🔹 Data Properties
Compute descriptive statistics (*mean, median, std, min, max, count*) for selected fields, either across the whole layer or within a drawn rectangle (ROI).  
Inline histograms are provided, with optional distribution fits (Normal, Student-t, Uniform, Exponential, Chi-square).

### 🔹 TS Analysis
Click on a point feature in a time-series dataset to display its displacement time series and corresponding amplitude spectrum.  
The three strongest spectral peaks are automatically highlighted and reported in the legend.

### 🔹 Attributes
The right-hand panel in **TS Analysis** lists all non-time-series attributes for the selected feature.  
The information line shows the layer name, feature ID, and the number of epochs available.

---

## 💡 TS Analysis Tips
- Time is converted to years; detrending + Hann window reduce spectral leakage.  
- For irregular sampling, interpret high-frequency peaks cautiously.  
- Resize panels with the splitter: plots (left) and attributes (right).  

---

## 🛠 Troubleshooting
- **No feature under cursor**: zoom in and try again (picker uses a small pixel tolerance).  
- **No time-series fields found**: ensure fields are named like `YYYYMMDD` and contain numeric values.  
- **Empty stats**: make sure numeric fields were selected and ROI contains features.

---

## 📥 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/AKD11-09/insar-ts-toolbox.git
   ```
2. Copy the `insar_ts_toolbox` folder into your QGIS plugin directory:
   ```
   <QGIS profile>/python/plugins/
   ```
3. Enable **InSAR-TS Toolbox** in *Plugins → Manage and Install Plugins*.

---

## 🙏 Acknowledgements

Developed at the **Geodätisches Institut Hannover (GIH)**, Leibniz University Hannover.

This work was supported by a **DAAD (German Academic Exchange Service) Research Grant**.
