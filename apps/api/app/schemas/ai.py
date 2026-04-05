from pydantic import BaseModel, Field


class AnalyzeVideoRequest(BaseModel):
    workspace_id: str
    video_id: str
    transcript: str
    caption: str
    metrics: dict[str, float | int]


class AnalyzeVideoResponse(BaseModel):
    hooks_score: int = Field(ge=0, le=100)
    cta_score: int = Field(ge=0, le=100)
    retention_insights: list[str]
    engagement_insights: list[str]
    recommendations: list[str]


class GenerateScriptRequest(BaseModel):
    workspace_id: str
    niche: str
    objective: str
    duration_seconds: int = Field(default=30, ge=10, le=180)


class GenerateScriptResponse(BaseModel):
    hook: str
    body: list[str]
    cta: str


class PredictGrowthRequest(BaseModel):
    workspace_id: str
    historical_metrics: list[dict[str, float | int]]


class PredictGrowthResponse(BaseModel):
    projected_followers_30d: int
    projected_engagement_rate_30d: float
    confidence: float
    reasoning: str
