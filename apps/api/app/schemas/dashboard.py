from pydantic import BaseModel


class DashboardKpis(BaseModel):
    total_views: int
    avg_engagement_rate: float
    avg_retention_rate: float
    top_platform: str
    growth_mom: float


class Opportunity(BaseModel):
    title: str
    potential_value_usd: float
    rationale: str


class DashboardResponse(BaseModel):
    kpis: DashboardKpis
    opportunities: list[Opportunity]
