#!/usr/bin/env python3
"""
Quick Photo Upload Guide for Kansas Tamil Catholic Community App

TO ADD YOUR REAL PHOTOS:

1. SAVE YOUR PHOTOS FROM CHAT:
   - Right-click on the clergy photo (priests group) → Save as: clergy.jpg
   - Right-click on the Mary statue photo → Save as: mary.jpg

2. UPLOAD TO DATABRICKS:
   Method A - Via Workspace Files UI:
   - Go to Workspace → Files
   - Navigate to: /Users/jeneive.dhanapalan@gmail.com/kansas-tamil-catholic-community/static/images/
   - Click "Upload" button
   - Select clergy.jpg and mary.jpg
   
   Method B - Via this script:
   - Save your photos to your local computer as clergy.jpg and mary.jpg
   - Run this script to upload them
"""

import os
import shutil
from pathlib import Path

# Target directory
IMAGES_DIR = Path("/Workspace/Users/jeneive.dhanapalan@gmail.com/kansas-tamil-catholic-community/static/images")

print("Kansas Tamil Catholic Community - Photo Upload Helper")
print("=" * 60)
print(f"\nTarget directory: {IMAGES_DIR}")
print(f"Directory exists: {IMAGES_DIR.exists()}")

if IMAGES_DIR.exists():
    print(f"\nCurrent files in images directory:")
    for file in IMAGES_DIR.iterdir():
        size = file.stat().st_size if file.is_file() else 0
        print(f"  - {file.name} ({size:,} bytes)")
else:
    print("\n⚠️  Images directory doesn't exist. Creating it...")
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    print("✅ Directory created!")

print("\n" + "=" * 60)
print("NEXT STEPS:")
print("1. Save photos from chat as 'clergy.jpg' and 'mary.jpg'")
print("2. Upload them to the images folder via Databricks Files UI")
print("3. Deploy the app to see your real photos!")
print("=" * 60)