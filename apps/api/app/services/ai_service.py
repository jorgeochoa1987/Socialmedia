import json

from vertexai import init
from vertexai.generative_models import GenerativeModel

from app.core.config import settings
from app.schemas.ai import (
    AnalyzeVideoRequest,
    AnalyzeVideoResponse,
    GenerateScriptRequest,
    GenerateScriptResponse,
    PredictGrowthRequest,
    PredictGrowthResponse,
)
from app.services.prompt_builder import build_analyze_prompt, build_growth_prompt, build_script_prompt


class AIService:
    def __init__(self) -> None:
        init(project=settings.gcp_project_id, location=settings.gcp_location)
        self.model = GenerativeModel(settings.vertex_model)

    def _generate_json(self, prompt: str) -> dict:
        response = self.model.generate_content(prompt)
        text = response.text.strip().removeprefix("```json").removesuffix("```").strip()
        return json.loads(text)

    def analyze_video(self, request: AnalyzeVideoRequest) -> AnalyzeVideoResponse:
        prompt = build_analyze_prompt(request.transcript, request.caption, request.metrics)
        data = self._generate_json(prompt)
        return AnalyzeVideoResponse(**data)

    def generate_script(self, request: GenerateScriptRequest) -> GenerateScriptResponse:
        prompt = build_script_prompt(request.niche, request.objective, request.duration_seconds)
        data = self._generate_json(prompt)
        return GenerateScriptResponse(**data)

    def predict_growth(self, request: PredictGrowthRequest) -> PredictGrowthResponse:
        prompt = build_growth_prompt(request.historical_metrics)
        data = self._generate_json(prompt)
        return PredictGrowthResponse(**data)
