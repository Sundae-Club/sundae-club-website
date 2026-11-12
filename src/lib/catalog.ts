import { getCollection, type CollectionEntry } from "astro:content";
import { utcDateISO } from "./time";

const STREAM_SLUG = /^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$/;
const TOPIC_SLUG = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

export type StreamEntry = CollectionEntry<"streams">;
export type TopicEntry = CollectionEntry<"topics">;

export async function loadCatalog(): Promise<{
  streams: StreamEntry[];
  topics: TopicEntry[];
  topicById: Map<string, TopicEntry>;
}> {
  const [streams, topics] = await Promise.all([
    getCollection("streams"),
    getCollection("topics"),
  ]);

  for (const topic of topics) {
    if (!TOPIC_SLUG.test(topic.id)) {
      throw new Error(
        `Topic "${topic.id}" must be named slug.md so it is served at /topics/slug.`,
      );
    }
    if (!topic.body?.trim()) {
      throw new Error(`Topic "${topic.id}" needs a short answer in the Markdown body.`);
    }
  }

  const topicById = new Map(topics.map((topic) => [topic.id, topic]));

  for (const stream of streams) {
    if (!STREAM_SLUG.test(stream.id)) {
      throw new Error(
        `Stream "${stream.id}" must be named YYYY-MM-DD-slug.md so it is served at /streams/YYYY-MM-DD-slug.`,
      );
    }
    const iso = utcDateISO(stream.data.date);
    if (!stream.id.startsWith(`${iso}-`)) {
      throw new Error(`Stream "${stream.id}" does not start with its date ${iso}.`);
    }
    for (const topicSlug of stream.data.topics) {
      if (!topicById.has(topicSlug)) {
        throw new Error(`Stream "${stream.id}" links to missing topic "${topicSlug}".`);
      }
    }
  }

  streams.sort((a, b) => {
    const byDate = b.data.date.valueOf() - a.data.date.valueOf();
    if (byDate !== 0) return byDate;
    if (a.id === b.id) return 0;
    return a.id < b.id ? 1 : -1;
  });

  topics.sort((a, b) => a.data.title.localeCompare(b.data.title, "en"));

  return { streams, topics, topicById };
}
