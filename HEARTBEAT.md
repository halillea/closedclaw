# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Memory Auto-Capture (Every Heartbeat)
1. If meaningful conversation since last capture:
   - Run: `python3 skills/memory/scripts/capture.py --facts "fact1" "fact2"`
   - Update RECENT_CONTEXT.md with highlights
   - Update SESSION-STATE.md if task context changed
