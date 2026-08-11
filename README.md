# InSAR-TS Toolbox

[![QGIS](https://img.shields.io/badge/QGIS-3.x-green.svg)](https://qgis.org) 
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/) 
[![License: GPL v2+](https://img.shields.io/badge/License-GPL%20v2%2B-blue.svg)](LICENSE)

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

## 📦 Requirements

QGIS 3.0 or later, with Python 3.

| Package | Used for | Ships with QGIS? |
|---|---|---|
| `numpy` | numerics throughout | ✅ yes |
| `pandas` | tabular handling of time series | ✅ yes |
| `matplotlib` | time-series, spectrum and histogram plots | ✅ yes |
| `scipy` | Lomb–Scargle periodogram, distribution fits | ✅ yes |
| `scikit-learn` | KMeans and DBSCAN clustering | ❌ **no — install manually** |

`numpy`, `pandas`, `matplotlib` and `scipy` are bundled with the standard QGIS
installers (OSGeo4W on Windows, and the official macOS/Linux packages), so no action
is normally needed.

**`scikit-learn` is not bundled** and must be installed into the Python environment
that QGIS uses. Only the *Clustering* tab needs it — the other tabs work without it.

- **Windows (OSGeo4W):** open the *OSGeo4W Shell* from the Start menu and run
  ```bash
  python -m pip install scikit-learn
  ```
- **Linux / macOS:** install into the Python that QGIS uses, e.g.
  ```bash
  python3 -m pip install scikit-learn
  ```

Restart QGIS afterwards. To confirm from inside QGIS, open *Plugins → Python Console*
and run `import sklearn; print(sklearn.__version__)`.

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

---

## 📄 License

Copyright © 2025–2026 Ashwin Kumar Dhanasekaran, Kourosh Shahryarinia, Mohammad Omidalizarandi.

This program is free software; you can redistribute it and/or modify it under the
terms of the **GNU General Public License version 2**, or (at your option) any later
version. See [LICENSE](LICENSE) for the full text.

This plugin builds on the QGIS Python API, which is itself GPL-2.0-or-later.
