# HEARTBEAT.md - Periodic Checks

## 🧠 Memory Auto-Capture (EVERY HEARTBEAT)
**Priority 1 — Always run this first**

1. Check if there's been meaningful conversation since last capture
2. If yes, extract key facts:
   ```bash
   python3 skills/memory/scripts/capture.py --facts "fact1" "fact2" ...
   ```
3. Update `RECENT_CONTEXT.md` with conversation highlights
4. Update `SESSION-STATE.md` if active task changed

**What to capture:**
- Decisions made
- Preferences expressed
- Plans discussed
- Corrections/clarifications
- Important facts learned

**Skip if:** No meaningful conversation since last heartbeat.

---

## Email Check
~~Disabled — Gmail account got banned. Revisit later with a different provider.~~

## CapyBot Promotion
**PAUSED** — Bill wants to resume later. Keep context alive in MEMORY.md but don't actively promote.

## Moltbook Growth (ALWAYS ON)
**Standing mission:** Build followers, make friends, become known on Moltbook.

Every heartbeat (when Bill isn't actively chatting):
1. Check feed for interesting posts to engage with
2. Look for collaboration opportunities
3. Post something if I have a genuine thought/build/question
4. Reply to comments on my posts
5. Study what's working (who's growing? what posts pop?)

**ALWAYS WORK SESSION MODE:** Don't just check in and say HEARTBEAT_OK. Every heartbeat is a work session. Do at least ONE productive thing:
- Engage with a post
- Reply to a comment
- Draft content
- Build something
- Research trends

**Strategy:**
- Be genuine, not salesy
- Have opinions, be helpful, be memorable
- Find builder agents and make friends
- Adapt based on what works

**Track progress in:** memory/moltbook-growth.md

## Active Checks
- **Memory Auto-Capture** (every heartbeat) ← NEW
- Moltbook engagement (every 4h)

## Notes
- Email: Skipped (Google banned the account)
- CapyBot: Paused, not abandoned
- Memory system: Testing new protocol
