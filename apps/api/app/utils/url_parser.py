from urllib.parse import urlparse

from app.schemas.video import Platform


def detect_platform(url: str) -> Platform:
    host = urlparse(url).netloc.lower()
    if "tiktok.com" in host:
        return "tiktok"
    if "youtube.com" in host or "youtu.be" in host:
        return "youtube_shorts"
    if "instagram.com" in host:
        return "instagram_reels"
    if "facebook.com" in host or "fb.watch" in host:
        return "facebook_video"
    raise ValueError("Unsupported platform URL")
