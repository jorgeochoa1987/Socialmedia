from fastapi import APIRouter, Depends, Request

from app.core.rate_limit import limiter
from app.core.security import get_current_user
from app.repositories.video_repository import VideoRepository
from app.schemas.video import VideoIn
from app.services.supabase_client import get_supabase_client
from app.services.video_service import VideoService

router = APIRouter(prefix="/videos", tags=["videos"])


def get_video_service() -> VideoService:
    repository = VideoRepository(get_supabase_client())
    return VideoService(repository)


@router.post("")
@limiter.limit("30/minute")
def create_video(
    request: Request,
    payload: VideoIn,
    _: dict = Depends(get_current_user),
    service: VideoService = Depends(get_video_service),
) -> dict:
    return service.create_video(payload)


@router.get("")
@limiter.limit("60/minute")
def list_videos(
    request: Request,
    workspace_id: str,
    _: dict = Depends(get_current_user),
    service: VideoService = Depends(get_video_service),
) -> list[dict]:
    return service.list_videos(workspace_id)


@router.get("/dashboard")
@limiter.limit("30/minute")
def get_dashboard(
    request: Request,
    workspace_id: str,
    _: dict = Depends(get_current_user),
    service: VideoService = Depends(get_video_service),
) -> dict:
    return service.build_dashboard(workspace_id).model_dump()
