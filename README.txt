InSAR-TS Toolbox
================

A QGIS plugin for time series analysis of InSAR data (Persistent Scatterer and Distributed Scatterer points).
It provides clustering, descriptive statistics, spectral analysis, and visualization tools for InSAR time series data within QGIS.

QGIS Compatibility: 3.x and above
Python Version: 3.9 or later
License: GPL-2.0-or-later

-------------------------------------------------------------------------------
OVERVIEW OF TABS
-------------------------------------------------------------------------------

Clustering:
    Select numeric fields from a point layer and run clustering using KMeans or DBSCAN.
    Results are stored in a cluster_id field and visualized with automatic color symbology (noise in grey).

Data Properties:
    Compute descriptive statistics (mean, median, std, min, max, count) for selected fields,
    across the whole layer or within a selected rectangle (ROI). Inline histograms are available.

TS Analysis:
    Click on a point feature to display its displacement time series and amplitude spectrum.
    The three strongest spectral peaks are highlighted and listed.

Attributes:
    Lists non-time-series attributes for the selected feature, including layer name, feature ID,
    and number of epochs available.

-------------------------------------------------------------------------------
INSTALLATION
-------------------------------------------------------------------------------

1. Download or clone this repository:
       git clone https://github.com/AKD11-09/insar-ts-toolbox.git

2. In QGIS, open:
       Plugins → Manage and Install Plugins → Install from ZIP

3. Select the plugin ZIP and install.

-------------------------------------------------------------------------------
DEPENDENCIES
-------------------------------------------------------------------------------

The InSAR-TS Toolbox relies on several Python libraries for numerical analysis, clustering,
and visualization. Most of these are already included in standard QGIS 3.x installations.

Required Python packages:
    - numpy
    - pandas
    - matplotlib
    - scikit-learn
    - scipy
    - seaborn
    - statsmodels

Installation of missing libraries:

Windows (OSGeo4W Shell):
    pip install numpy pandas matplotlib scikit-learn scipy seaborn statsmodels

Linux / macOS:
    pip3 install numpy pandas matplotlib scikit-learn scipy seaborn statsmodels

Notes:
    - All imports are handled gracefully inside the plugin. If a required library is missing,
      QGIS will display a message such as:
          "Missing dependency: numpy – please install it via pip."
    - No external binaries or compiled extensions are required.
    - Tested on Python 3.9+ and QGIS 3.0 and later.

-------------------------------------------------------------------------------
TROUBLESHOOTING
-------------------------------------------------------------------------------

- No feature under cursor: zoom in and retry.
- No time-series fields: ensure fields are named like YYYYMMDD and numeric.
- Empty stats: ensure numeric fields were selected and ROI contains features.

-------------------------------------------------------------------------------
SUPPORT & ISSUES
-------------------------------------------------------------------------------

Report bugs and feature requests at:
    https://github.com/AKD11-09/insar-ts-toolbox/issues

-------------------------------------------------------------------------------
AUTHORS
-------------------------------------------------------------------------------

Ashwin Kumar Dhanasekaran
Mohammad Omidalizarandi
Kourosh Shahryarinia
Institute of Geodesy (GIH), Leibniz University Hannover, Germany
