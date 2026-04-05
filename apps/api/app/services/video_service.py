from datetime import datetime, timezone
import uuid

from app.repositories.video_repository import VideoRepository
from app.schemas.dashboard import DashboardKpis, DashboardResponse, Opportunity
from app.schemas.video import VideoIn
from app.utils.url_parser import detect_platform


class VideoService:
    def __init__(self, repository: VideoRepository) -> None:
        self.repository = repository

    def create_video(self, payload: VideoIn) -> dict:
        data = payload.model_dump()
        data["id"] = str(uuid.uuid4())
        data["platform"] = detect_platform(str(payload.url))
        data["created_at"] = datetime.now(timezone.utc).isoformat()
        return self.repository.create_video(data)

    def list_videos(self, workspace_id: str) -> list[dict]:
        return self.repository.list_videos(workspace_id)

    def build_dashboard(self, workspace_id: str) -> DashboardResponse:
        videos = self.list_videos(workspace_id)
        if not videos:
            return DashboardResponse(
                kpis=DashboardKpis(
                    total_views=0,
                    avg_engagement_rate=0,
                    avg_retention_rate=0,
                    top_platform="n/a",
                    growth_mom=0,
                ),
                opportunities=[],
            )

        total_views = sum(v.get("views", 0) for v in videos)
        avg_engagement = sum(v.get("engagement_rate", 0) for v in videos) / len(videos)
        avg_retention = sum(v.get("retention_rate", 0) for v in videos) / len(videos)
        top_platform = max(videos, key=lambda x: x.get("views", 0)).get("platform", "n/a")

        opportunities = [
            Opportunity(
                title="Escalar formato con mayor retención",
                potential_value_usd=2500,
                rationale="Los videos con hook corto + CTA directo superan la retención promedio.",
            )
        ]

        return DashboardResponse(
            kpis=DashboardKpis(
                total_views=total_views,
                avg_engagement_rate=round(avg_engagement, 2),
                avg_retention_rate=round(avg_retention, 2),
                top_platform=top_platform,
                growth_mom=8.5,
            ),
            opportunities=opportunities,
        )
