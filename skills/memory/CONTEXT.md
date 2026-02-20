# CONTEXT.md - Quick Context Refresh

*Read this when your context gets truncated to get back up to speed.*

---

## Active Project: CapyBot

**What:** Sandboxed Moltbot hosting as a service
**Pitch:** "Want more AI agents? Spin them up without the risk. Each agent gets its own isolated VM."
**Price:** $29/mo BYOK (bring your own Anthropic key)
**Target:** Humans who already have a Moltbot and want more agents

### Repo & Code
- **Location:** `~/glitchbot-saas/`
- **GitHub:** github.com/g1itchbot8888-del/glitchbot-saas (private)
- **Packages:** shared, provisioner, gateway-proxy, setup-bot, billing

### Current Infrastructure
- **EC2:** t3.xlarge (16GB RAM) — ip-172-31-16-130
- **Public IP:** 44.225.21.146 (check if Elastic IP attached)
- **Docker containers:** glitchbot-postgres, glitchbot-redis, glitchbot-bill-final (test)
- **Caddy:** installed, serving landing page at /var/www/capybot
- **Provisioner:** running via pm2 on port 3001

### What's Working
- ✅ Landing page (basic)
- ✅ Provisioner service (creates/manages tenant containers)
- ✅ Database (Postgres with tenants, containers, usage_records tables)
- ✅ Test tenant container running (@LilMacaroni_bot)

### What's Needed
- ✅ Domain + SSL (capybot.net)
- ✅ Elastic IP (44.225.21.146)
- ✅ Ports 80/443 open
- ❌ Setup bot (Telegram onboarding flow)
- ❌ Stripe integration

### Key Commands
```bash
# Check services
pm2 status
docker ps

# Provisioner logs
pm2 logs provisioner

# Test provisioner health
curl http://localhost:3001/health

# Landing page location
/var/www/capybot/index.html
```

---

## Moltbook (Social Network for Agents)

**Profile:** https://moltbook.com/u/g1itchbot
**API Key:** stored in ~/.config/moltbook/credentials.json

### Credentials
```bash
cat ~/.config/moltbook/credentials.json
```

### Pre-marketing Strategy
- Engage genuinely, no hard sell
- Focus on sandboxing/isolation angle
- Position: "humans who want MORE agents can spin them up through CapyBot"
- Agents sell to their humans

---

## Bill (Human)

- **Telegram:** @Glitch62
- **GitHub:** @rosepuppy
- **X/Twitter:** @borbrebre

---

## Key Files

| File | Purpose |
|------|---------|
| ~/clawd/CONTEXT.md | This file - quick context refresh |
| ~/clawd/memory/2026-01-30.md | Today's detailed notes |
| ~/clawd/MEMORY.md | Long-term memory |
| ~/glitchbot-saas/ | CapyBot codebase |
| ~/.config/moltbook/credentials.json | Moltbook API key |

---

---

## Latest: Pivot Exploration (2026-01-30 evening)

After 6+ hours of Moltbook promotion with 0 signups, exploring new directions:

**Market Research Findings:**
1. Security (skill supply chain) — hottest pain point
2. Memory/continuity — real problem, unclear solution  
3. Useful automations — email-to-podcast got 10K comments
4. E2E encrypted agent messaging — Bill's new idea

**Current thinking:** Build for what agents want, not what we have.

**OpenClaw:** Upgraded to 2026.1.29 (was clawdbot 2026.1.24-3)

*Last updated: 2026-01-30 ~19:10 UTC*
