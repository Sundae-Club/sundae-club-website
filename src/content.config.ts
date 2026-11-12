import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const youtubeId = z
  .string()
  .regex(/^[A-Za-z0-9_-]{11}$/, "YouTube id must be 11 characters.");

const slug = z
  .string()
  .regex(/^[a-z0-9]+(?:-[a-z0-9]+)*$/, "Use a lowercase slug.");

function utcDay(value: unknown): Date {
  if (value instanceof Date && !Number.isNaN(value.valueOf())) {
    return new Date(Date.UTC(value.getUTCFullYear(), value.getUTCMonth(), value.getUTCDate()));
  }
  if (typeof value === "string") {
    const dateOnly = /^(\d{4})-(\d{2})-(\d{2})$/.exec(value);
    if (dateOnly) {
      return new Date(Date.UTC(Number(dateOnly[1]), Number(dateOnly[2]) - 1, Number(dateOnly[3])));
    }
    const parsed = new Date(value);
    if (!Number.isNaN(parsed.valueOf())) {
      return new Date(Date.UTC(parsed.getUTCFullYear(), parsed.getUTCMonth(), parsed.getUTCDate()));
    }
  }
  return new Date(NaN);
}

const streamDate = z.preprocess(utcDay, z.date());

const streams = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/content/streams",
    generateId: ({ entry }) => entry.replace(/\.[^.]+$/, "").replace(/\\/g, "/"),
  }),
  schema: z.object({
    title: z.string().min(1),
    date: streamDate,
    youtubeId,
    summary: z.string().min(1),
    topics: z.array(slug).default([]),
    sample: z.boolean().default(false),
    chapters: z
      .array(
        z.object({
          title: z.string().min(1),
          start: z.number().int().nonnegative(),
        }),
      )
      .default([]),
  }),
});

const topics = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/content/topics",
    generateId: ({ entry }) => entry.replace(/\.[^.]+$/, "").replace(/\\/g, "/"),
  }),
  schema: z.object({
    title: z.string().min(1),
    sample: z.boolean().default(false),
    clips: z
      .array(
        z
          .object({
            title: z.string().min(1),
            youtubeId,
            start: z.number().int().nonnegative(),
            end: z.number().int().positive(),
          })
          .refine((clip) => clip.end > clip.start, {
            message: "Clip end must be later than its start.",
            path: ["end"],
          }),
      )
      .min(1),
  }),
});

export const collections = { streams, topics };
