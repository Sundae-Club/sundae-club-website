const YOUTUBE_ID = /^[A-Za-z0-9_-]{11}$/;

export function youtubeEmbedBase(id: string): string {
  if (!YOUTUBE_ID.test(id)) {
    throw new Error(`Invalid YouTube id: ${id}`);
  }
  return `https://www.youtube-nocookie.com/embed/${id}`;
}

export function youtubeEmbedUrl(
  id: string,
  options: { start?: number; end?: number; autoplay?: boolean } = {},
): string {
  const params = new URLSearchParams();
  params.set("rel", "0");
  if (options.start != null) params.set("start", String(options.start));
  if (options.end != null) params.set("end", String(options.end));
  if (options.autoplay) params.set("autoplay", "1");
  return `${youtubeEmbedBase(id)}?${params.toString()}`;
}
