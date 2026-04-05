from textwrap import dedent


def build_analyze_prompt(transcript: str, caption: str, metrics: dict) -> str:
    return dedent(
        f"""
        Eres un estratega senior de contenido para social media B2B.
        Analiza hook, CTA, retención y engagement del contenido.

        Transcript: {transcript}
        Caption: {caption}
        Metrics: {metrics}

        Responde en JSON con:
        hooks_score, cta_score, retention_insights, engagement_insights, recommendations.
        """
    ).strip()


def build_script_prompt(niche: str, objective: str, duration_seconds: int) -> str:
    return dedent(
        f"""
        Crea un guion para video corto ({duration_seconds}s).
        Nicho: {niche}
        Objetivo: {objective}

        Devuelve JSON con: hook, body (lista), cta.
        """
    ).strip()


def build_growth_prompt(historical_metrics: list[dict]) -> str:
    return dedent(
        f"""
        Predice crecimiento a 30 días usando estas métricas históricas:
        {historical_metrics}

        Devuelve JSON con: projected_followers_30d, projected_engagement_rate_30d,
        confidence (0-1) y reasoning.
        """
    ).strip()
