from app.utils.url_parser import detect_platform


def test_detect_platform_tiktok() -> None:
    assert detect_platform("https://www.tiktok.com/@test/video/123") == "tiktok"
