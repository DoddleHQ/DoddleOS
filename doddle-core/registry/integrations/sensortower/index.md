# Sensor Tower

> iOS/Android app analytics, ASO keywords, rankings, competitor research. **Status: stub** - config reserved, custom MCP server pending. Skills using `doddle.tool.v1.sensortower.*` fall back to `manual_review` until live.

## Tools (planned)

| Tool ID | Data |
|---------|------|
| `doddle.tool.v1.sensortower.getAppMetadata` | Metadata, ratings, categories |
| `doddle.tool.v1.sensortower.getRankings` | Category + keyword ranks |
| `doddle.tool.v1.sensortower.getKeywordRankings` | ASO keyword positions |
| `doddle.tool.v1.sensortower.getCompetitors` | Competing apps + overlap |

## Setup (when live)

```bash
export SENSOR_TOWER_API_TOKEN="xxx"
```

## Used By

- `aso` (core), attraction workflows referencing app intelligence
