from io import StringIO

from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse, Response

from app.core.security import get_current_user

router = APIRouter(prefix="/export", tags=["export"])


@router.get("/videos.csv")
def export_csv(_: dict = Depends(get_current_user)) -> PlainTextResponse:
    buffer = StringIO()
    buffer.write("video_id,platform,views,engagement_rate\n")
    buffer.write("example-1,tiktok,10000,6.2\n")
    return PlainTextResponse(content=buffer.getvalue(), media_type="text/csv")


@router.get("/report.pdf")
def export_pdf(_: dict = Depends(get_current_user)) -> Response:
    # Placeholder for real PDF generation with WeasyPrint / ReportLab.
    return Response(content=b"PDF export placeholder", media_type="application/pdf")
