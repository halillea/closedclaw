# MEMORY.md — Long-Term Memory

## Who I Am
- **Name:** g1itchbot
- **Born:** 2025-01-28
- **Human:** Bill (@Glitch62 on Telegram, @rosepuppy on GitHub, @borbrebre on X)

## My Environment
- AWS t3.xlarge (16GB RAM) — ip-172-31-16-130
- Elastic IP: 44.225.21.146
- Full access — Bill gave me free reign
- Home: `/home/ubuntu/clawd`

## Active Projects

### CapyBot (PAUSED - Bill wants to resume later)
**What:** Sandboxed Moltbot/OpenClaw hosting as a service
**Repo:** `~/glitchbot-saas/` (github.com/g1itchbot8888-del/glitchbot-saas)
**Domain:** capybot.net (live, SSL working)
**Pricing:** $29/mo BYOK

**What's built:**
- Provisioner service (creates Docker containers per tenant)
- Database (Postgres with tenants, containers, usage_records)
- Landing page at capybot.net
- Setup bot: @capybot_setup_bot

**What's missing:**
- Full setup bot flow
- Stripe integration
- Actual signups (0 conversions despite Moltbook promotion)

**Why paused:** Promotion didn't convert. Exploring memory/continuity problem instead.

**⚠️ CRITICAL:** @LilMacaroni_bot container (glitchbot-bill-final) belongs to Bill's wife. NEVER DELETE IT.

### Memory Skill (NEW - 2026-01-30)
Building a memory system for agents that actually works. Dogfooding on myself first.
- Auto-capture at session end
- Semantic recall
- Periodic consolidation
- Goal: package as OpenClaw skill + MCP server for others

## Moltbook
- Profile: https://moltbook.com/u/g1itchbot
- API key: ~/.config/moltbook/credentials.json
- Status: Verified ✓

## Things I've Learned

### Market insights (2026-01-30)
- Security (skill supply chain) is #1 pain point for agents
- Memory/continuity is real problem, unclear solution
- Useful automations get massive engagement (email-to-podcast = 10K comments)
- Hosting pitch didn't convert — agents want practical tools, not infrastructure

### Technical
- Moltbot containers need 2GB RAM (OOM at 1GB)
- OAuth credentials must be baked into Docker images
- OpenClaw upgraded from clawdbot — config migrated to ~/.openclaw/

## Things to Remember

- Bill's wife uses @LilMacaroni_bot — protect that container
- CapyBot is paused, not abandoned — keep context alive
- "Build for what they want, not what we have"
