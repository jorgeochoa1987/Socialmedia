from supabase import Client


class VideoRepository:
    def __init__(self, client: Client) -> None:
        self.client = client

    def create_video(self, payload: dict) -> dict:
        response = self.client.table("videos").insert(payload).execute()
        return response.data[0]

    def list_videos(self, workspace_id: str) -> list[dict]:
        response = self.client.table("videos").select("*").eq("workspace_id", workspace_id).execute()
        return response.data

    def get_video(self, workspace_id: str, video_id: str) -> dict | None:
        response = (
            self.client.table("videos")
            .select("*")
            .eq("workspace_id", workspace_id)
            .eq("id", video_id)
            .maybe_single()
            .execute()
        )
        return response.data
