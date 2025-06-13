# 🎥 YouTube Video Downloader

A powerful **GUI-based YouTube Video Downloader** built using **Python**, **Kivy**, and **KivyMD**. This application enables users to download videos in various resolutions including **360p**, **480p**, **720p**, **1080p**, **1440p**, **4K**, and **Audio Only**, with real-time progress tracking and integrated error handling.

---

## 🚀 Features

- ✅ **User-friendly interface** with clean material design  
- ✅ **Quality selection**: 360p, 480p, 720p, 1080p, 1440p, 4K, or Audio Only  
- ✅ **Progress bar** for real-time download status  
- ✅ **FFmpeg integration** for audio-only downloads  
- ✅ **Error handling** for invalid URLs and download issues  

---

## 🛠️ Technologies Used

- **Python** – Core programming  
- **Kivy** – Cross-platform GUI development  
- **KivyMD** – Material Design components for Kivy  
- **yt-dlp** – Efficient video downloading  
- **FFmpeg** – Audio extraction from video  
- KivyMD widgets like `MDDropdownMenu`, `MDDialog`, `MDProgressBar`  

---

## 📦 Installation

### ✅ Prerequisites

Ensure Python **3.x** is installed on your machine.

### 📥 Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Dhananjay66/YouTube-Downloader
   cd YouTube-Downloader
    ```

2. **Install dependencies**:

   ```bash
   pip install kivy kivymd yt-dlp ffmpeg-python
   ```

3. **Install FFmpeg** (if not already installed):

   * **Windows**: [Download from official FFmpeg site](https://ffmpeg.org/download.html) and add to PATH
   * **Linux (Debian/Ubuntu)**:

     ```bash
     sudo apt install ffmpeg
     ```
   * **macOS**:

     ```bash
     brew install ffmpeg
     ```

4. **Run the application**:

   ```bash
   python main.py
   ```

---

## 📋 Usage

1. Enter the **YouTube video URL** in the input field
2. Select the **desired quality** from the dropdown
3. Click **Download** to start
4. Monitor the **progress bar and status messages**
5. Downloaded files are saved in the `Downloads/` directory inside the project

---

## 🧩 Troubleshooting

* ❌ **Download fails?**  
  🔹 Ensure a valid YouTube URL is provided  
  🔹 Check your internet connection

* ⚠️ **FFmpeg error?**  
  🔹 Make sure FFmpeg is installed and added to system `PATH`

* 🔄 **yt-dlp outdated?**  
  🔹 Update it using:
    ```bash
    pip install --upgrade yt-dlp
    ```


---

## 📎 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Dhananjay Pratap Singh**
📧 [Contact](mailto:pratapsinghd665@gmail.com) | 🌐 [GitHub Profile](https://github.com/Dhananjay66)

---
