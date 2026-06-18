"""
IPL Analytics Project - Setup Script
Run this first to download data and install dependencies.
"""

import subprocess
import sys
import os

def install_requirements():
    packages = [
        "pandas", "numpy", "matplotlib", "seaborn",
        "plotly", "streamlit", "openpyxl", "kaggle",
        "nbformat", "jupyter"
    ]
    print("📦 Installing packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + packages)
    print("✅ All packages installed!\n")

def download_data():
    print("📥 Downloading IPL dataset from Kaggle...")
    print("""
    MANUAL STEP (one-time):
    ─────────────────────────────────────────────────
    1. Go to: https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020
       OR:     https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set
    2. Download and extract into:  ./data/
    3. You should have:
         data/matches.csv
         data/deliveries.csv
    ─────────────────────────────────────────────────
    Alternative: Use the Kaggle API
      kaggle datasets download -d patrickb1912/ipl-complete-dataset-20082020
      unzip *.zip -d data/
    """)

if __name__ == "__main__":
    install_requirements()
    download_data()
    print("🏏 Setup complete! Now open:  notebooks/01_EDA.ipynb")
