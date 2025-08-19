# OpenDownloader

A modern, user-friendly web application for downloading audio content from YouTube and SoundCloud. Built with Streamlit and powered by yt-dlp and soundcloud-lib.

## ⚠️ **IMPORTANT LEGAL DISCLAIMER**

**This software is provided for educational and personal use only. Users are solely responsible for ensuring their use of this software complies with all applicable laws and regulations.**

### Copyright and Legal Compliance

- **You are responsible for your own actions**: This tool is designed for downloading content that you have the legal right to access and download.
- **Respect copyright laws**: Only download content that you own, have permission to download, or is in the public domain.
- **No bypassing of restrictions**: This software should not be used to circumvent any legitimate access controls or copyright protections.
- **Personal use only**: Downloaded content should be for personal, non-commercial use unless you have explicit permission for other uses.

**The developers of this software are not responsible for any misuse, copyright violations, or illegal activities performed by users. Use this software responsibly and in accordance with applicable laws.**

## 🚀 Features

- **Multi-platform support**: Download from both YouTube and SoundCloud
- **High-quality audio**: Automatic conversion to MP3 format
- **User-friendly interface**: Clean, intuitive Streamlit web interface
- **Fast downloads**: Optimized download processes
- **Cross-platform**: Works on Windows, macOS, and Linux

## 📋 Prerequisites

- Python 3.7 or higher
- FFmpeg (for audio conversion)
- Internet connection

## 🛠️ Installation
We recommend using Docker for this approach:
```bash
docker run -dt -p 8501:8501 ghcr.io/bencetotht/opendownloader:1.0
```
By providing the `DOWNLOAD_PATH` environment variable, you can set a specific download location, and also mount the folder to your system, like the following:
```bash
docker run -dt -p 8501:8501 -e DOWNLOAD_PATH=/app/assets -v ./assets:/app/assets ghcr.io/bencetotht/opendownloader:1.0
```

### Installing FFmpeg

#### macOS (using Homebrew):
```bash
brew install ffmpeg
```

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### Windows:
Download from [FFmpeg official website](https://ffmpeg.org/download.html) or use Chocolatey:
```bash
choco install ffmpeg
```

### Install from source

1. **Clone the repository:**
```bash
git clone https://github.com/bencetotht/opendownloader.git
cd opendownloader
```

2. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. **Start the application:**
```bash
streamlit run app.py
```

2. **Open your web browser** and navigate to the displayed URL (usually `http://localhost:8501`)

3. **Select your platform** (YouTube or SoundCloud)

4. **Enter the URL** of the content you want to download

5. **Click Download** and wait for the process to complete

## 📁 Project Structure

```
opendownloader/
├── app.py              # Main Streamlit application
├── src/
│   ├── __init__.py
│   └── utils.py        # Download utilities
├── requirements.txt     # Python dependencies
├── LICENSE            # Apache 2.0 License
└── README.md          # This file
```

## 🔧 Dependencies

- **streamlit**: Web application framework
- **yt-dlp**: YouTube downloader library
- **soundcloud-lib**: SoundCloud API wrapper

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## ⚠️ Disclaimer

This software is provided "as is", without warranty of any kind. The authors and contributors are not responsible for any damages or legal issues that may arise from the use of this software.

**Remember**: Always respect copyright laws and only download content you have the legal right to access.

## 📞 Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Use responsibly and respect intellectual property rights.**
