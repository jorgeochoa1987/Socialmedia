"use client";

import { FormEvent, useState } from "react";

export function UrlLoader() {
  const [url, setUrl] = useState("");
  const [platform, setPlatform] = useState("tiktok");
  const [status, setStatus] = useState<string | null>(null);

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setStatus("Procesando URL y extrayendo métricas...");

    // En producción: llamar endpoint POST /videos con token de Supabase.
    await new Promise((resolve) => setTimeout(resolve, 500));
    setStatus("Video encolado para análisis IA ✅");
  }

  return (
    <form onSubmit={onSubmit} className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
      <h2 className="text-lg font-semibold">Cargar URL de video</h2>
      <div className="mt-4 grid gap-3 md:grid-cols-[1fr_180px_120px]">
        <input
          className="rounded-md border border-slate-300 px-3 py-2"
          placeholder="https://..."
          value={url}
          onChange={(event) => setUrl(event.target.value)}
          required
        />
        <select
          className="rounded-md border border-slate-300 px-3 py-2"
          value={platform}
          onChange={(event) => setPlatform(event.target.value)}
        >
          <option value="tiktok">TikTok</option>
          <option value="youtube_shorts">YouTube Shorts</option>
          <option value="instagram_reels">Instagram Reels</option>
          <option value="facebook_video">Facebook Video</option>
        </select>
        <button className="rounded-md bg-brand-600 px-4 py-2 font-medium text-white hover:bg-brand-500" type="submit">
          Analizar
        </button>
      </div>
      {status && <p className="mt-3 text-sm text-slate-600">{status}</p>}
    </form>
  );
}
