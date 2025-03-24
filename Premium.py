from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.label import MDLabel
from yt_dlp import YoutubeDL
import os

# Ensure FFmpeg is included
ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
os.environ["FFMPEG_BINARY"] = ffmpeg_path

# Kivy UI Layout
KV = """
ScreenManager:
    MainScreen:

<MainScreen>:
    name: "main"

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(10)
        padding: dp(20)

        MDLabel:
            text: "YouTube Downloader"
            font_style: "H4"
            halign: "center"

        MDTextField:
            id: url_input
            hint_text: "Enter YouTube URL"
            helper_text: "Paste your YouTube link here"
            helper_text_mode: "on_focus"
            size_hint_x: 0.9
            pos_hint: {"center_x": 0.5}

        MDLabel:
            id: quality_label
            text: "Selected Quality: Best"
            halign: "center"
            theme_text_color: "Secondary"

        MDRaisedButton:
            text: "Select Quality"
            on_release: app.open_quality_menu()
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Download"
            on_release: app.download_video()
            md_bg_color: 0, 0.6, 0, 1
            pos_hint: {"center_x": 0.5}

        MDProgressBar:
            id: progress_bar
            value: 0
            pos_hint: {"center_x": 0.5}

        MDLabel:
            id: progress_text
            text: ""
            halign: "center"
            theme_text_color: "Secondary"
"""

class MainScreen(Screen):
    pass

class YouTubeDownloaderApp(MDApp):
    selected_quality = StringProperty("Best")
    download_progress = NumericProperty(0)
    downloading = BooleanProperty(False)

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.menu = None
        return Builder.load_string(KV)

    def open_quality_menu(self):
        """Create and show the dropdown menu for quality selection"""
        quality_options = ["Best", "360p", "480p", "720p", "1080p", "1440p", "4K", "Audio Only"]
        menu_items = [
            {"text": q, "viewclass": "OneLineListItem", "on_release": lambda q=q: self.set_quality(q)}
            for q in quality_options
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.get_screen("main").ids.url_input,
            items=menu_items,
            width_mult=4
        )
        self.menu.open()

    def set_quality(self, quality):
        """Set the selected quality and update UI"""
        self.selected_quality = quality
        self.root.get_screen("main").ids.quality_label.text = f"Selected Quality: {quality}"
        self.menu.dismiss()

    def download_video(self):
        """Download video using yt-dlp with progress update"""
        url = self.root.get_screen("main").ids.url_input.text
        quality = self.selected_quality

        if not url:
            self.show_dialog("Error", "Please provide a YouTube URL.")
            return

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads\Downloads")
        ydl_opts = {
            'outtmpl': f'{downloads_path}/%(title)s.%(ext)s',
            'progress_hooks': [self.progress_hook]
        }

        if quality == "360p":
            ydl_opts['format'] = 'bestvideo[height<=360]+bestaudio/best'
        elif quality == "480p":
            ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best'
        elif quality == "720p":
            ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best'
        elif quality == "1080p":
            ydl_opts['format'] = 'bestvideo[height<=1080]+bestaudio/best'
        elif quality == "1440p":
            ydl_opts['format'] = 'bestvideo[height<=1440]+bestaudio/best'
        elif quality == "4K":
            ydl_opts['format'] = 'bestvideo[height<=2160]+bestaudio/best'
        elif quality == "Audio Only":
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
            ydl_opts['outtmpl'] = f'{downloads_path}/%(title)s.mp3'
        else:
            ydl_opts['format'] = 'best'

        try:
            self.downloading = True
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.downloading = False
            self.show_dialog("Success", f"Downloaded successfully to:\n{downloads_path}")
            self.root.get_screen("main").ids.progress_text.text = "Download Complete"
        except Exception as e:
            self.downloading = False
            self.show_dialog("Error", str(e))

    def progress_hook(self, d):
        """Update progress bar and text"""
        if d['status'] == 'downloading':
            percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
            self.root.get_screen("main").ids.progress_bar.value = percent
            self.root.get_screen("main").ids.progress_text.text = f"Downloading: {percent:.2f}%"
        elif d['status'] == 'finished':
            self.root.get_screen("main").ids.progress_bar.value = 100
            self.root.get_screen("main").ids.progress_text.text = "Processing..."

    def show_dialog(self, title, message):
        """Show an MDDialog with a message"""
        dialog = MDDialog(title=title, text=message)
        dialog.open()

# Run the Kivy App
if __name__ == "__main__":
    YouTubeDownloaderApp().run()