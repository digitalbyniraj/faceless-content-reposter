from downloader import download_youtube_video

def main():
    print("📥 Faceless Content Reposter")
    url = input("Enter YouTube video URL: ")
    watermark = input("Enter watermark text (e.g. @yourhandle): ")

    downloaded = download_youtube_video(url)
    print(f"✅ Downloaded: {downloaded}")

    watermarked = add_watermark(downloaded, watermark_text=watermark)
    print(f"🎬 Watermarked video saved at: {watermarked}")

if __name__ == "__main__":
    main()
