from fastapi import APIRouter, Depends, Request

from app.core.rate_limit import limiter
from app.core.security import get_current_user
from app.schemas.ai import (
    AnalyzeVideoRequest,
    AnalyzeVideoResponse,
    GenerateScriptRequest,
    GenerateScriptResponse,
    PredictGrowthRequest,
    PredictGrowthResponse,
)
from app.services.ai_service import AIService

router = APIRouter(prefix="/ai", tags=["ai"])


def get_ai_service() -> AIService:
    return AIService()


@router.post("/analyze-video", response_model=AnalyzeVideoResponse)
@limiter.limit("20/minute")
def analyze_video(
    request: Request,
    payload: AnalyzeVideoRequest,
    _: dict = Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
) -> AnalyzeVideoResponse:
    return service.analyze_video(payload)


@router.post("/generate-script", response_model=GenerateScriptResponse)
@limiter.limit("20/minute")
def generate_script(
    request: Request,
    payload: GenerateScriptRequest,
    _: dict = Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
) -> GenerateScriptResponse:
    return service.generate_script(payload)


@router.post("/predict-growth", response_model=PredictGrowthResponse)
@limiter.limit("20/minute")
def predict_growth(
    request: Request,
    payload: PredictGrowthRequest,
    _: dict = Depends(get_current_user),
    service: AIService = Depends(get_ai_service),
) -> PredictGrowthResponse:
    return service.predict_growth(payload)
