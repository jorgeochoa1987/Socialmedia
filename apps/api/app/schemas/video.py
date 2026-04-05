from datetime import datetime
from typing import Literal

from pydantic import BaseModel, HttpUrl

Platform = Literal["tiktok", "youtube_shorts", "instagram_reels", "facebook_video"]


class VideoIn(BaseModel):
    workspace_id: str
    url: HttpUrl
    platform: Platform


class VideoMetrics(BaseModel):
    views: int
    likes: int
    comments: int
    shares: int
    watch_time_avg_seconds: float
    retention_rate: float


class VideoOut(VideoIn):
    id: str
    created_at: datetime
    metrics: VideoMetrics | None = None
