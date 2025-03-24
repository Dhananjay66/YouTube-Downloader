# YouTube Video Downloader

## Overview

This is a GUI-based **YouTube Video Downloader** built using Python, Kivy, and KivyMD. The app allows users to download YouTube videos in different resolutions, including **360p, 480p, 720p, 1080p, 1440p, 4K, and Audio Only**. It features a progress bar for real-time tracking and integrates **yt-dlp** for efficient downloading.

## Features

✅ **User-friendly GUI** for downloading YouTube videos  
✅ **Quality selection** (360p, 480p, 720p, 1080p, 1440p, 4K, Audio Only)  
✅ **Real-time progress tracking** with a progress bar  
✅ **FFmpeg integration** for audio extraction  
✅ **Error handling** for invalid URLs or download failures  

## Technologies Used

- **Python** (Core Programming Language)  
- **Kivy & KivyMD** (GUI Development)  
- **yt-dlp** (YouTube Downloading)  
- **FFmpeg** (Audio Extraction)  
- **MDDropdownMenu, MDDialog, MDProgressBar** (KivyMD Components)  

## Installation

### Prerequisites

Make sure you have **Python 3.x** installed on your system.

### Steps

1️⃣ **Clone the repository:**
```sh
git clone https://github.com/Dhananjay66/YouTube-Downloader
cd YouTube-Downloader

2️⃣ Install dependencies:

sh
Copy
Edit
pip install kivy kivymd yt-dlp ffmpeg-python

3️⃣ Download FFmpeg (if not installed):

Windows: Download from FFmpeg Official Site

Linux/Mac: Install via package manager

sh
Copy
Edit
sudo apt install ffmpeg  # Ubuntu/Debian  
brew install ffmpeg  # macOS
4️⃣ Run the application:

sh
Copy
Edit
python main.py
Usage
Enter a YouTube URL in the text field.

Select a quality option from the dropdown menu.

Click "Download" to start the process.

Monitor the progress through the progress bar and status messages.

Find the downloaded file in the Downloads/Downloads folder.

Troubleshooting
🔹 Download fails? Ensure you have a valid YouTube URL.
🔹 FFmpeg missing? Ensure it is installed and added to the system path.
🔹 yt-dlp outdated? Update it using:

sh
Copy
Edit
pip install --upgrade yt-dlp
