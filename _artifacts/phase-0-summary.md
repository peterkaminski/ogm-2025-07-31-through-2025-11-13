# Phase 0 Summary: Multi-Call Mapping

Created: 2025-11-16
Status: Initial mapping complete (inventory created)

---

## Overview

This document summarizes the initial mapping work for the OGM multi-call wiki project.

### Scope
- **Total calls**: 16 (not 15 as initially estimated)
- **Date range**: July 31, 2025 to November 13, 2025 (3.5 months)
- **Call series**: Open Global Mind (OGM) calls

---

## Call Inventory Summary

### By Type
- **Hybrid calls**: 11 (calls 01, 03, 04, 05, 09, 10, 11, 12, 15, 16)
- **Check-in focused**: 3 (calls 02, 06, 14)
- **Topical discussions**: 3 (calls 07, 08, 13)
  - Call 07: On Collaboration
  - Call 08: Abundance
  - Call 13: Crony Capitalism

### Timeline
```
2025-07-31: Call 01 (First call)
2025-08-07: Call 02 (Check-in)
2025-08-14: Call 03
2025-08-21: Call 04
2025-08-28: Call 05
2025-09-04: Call 06 (Check-in)
2025-09-11: Call 07 (Topical: Collaboration)
2025-09-26: Call 08 (Topical: Abundance)
2025-10-02: Call 09
2025-10-09: Call 10
2025-10-16: Call 11
2025-10-23: Call 12
2025-10-30: Call 13 (Topical: Crony Capitalism)
2025-11-06: Call 14 (Check-in)
2025-11-13: Calls 15 & 16 (Split call, same date)
```

### Call Frequency
- Generally weekly calls
- One gap: Sept 11 → Sept 26 (15 days)
- One split call: Nov 13 (parts 1 & 2)

### Initial Topic Clusters (Preliminary)

Based on explicit topics in call names:

**Community & Connection:**
- Collaboration (Call 07)
- Check-in calls (Calls 02, 06, 14)

**Economics & Systems:**
- Abundance (Call 08)
- Crony Capitalism (Call 13)

**General OGM Calls:**
- Calls 01, 03, 04, 05, 09, 10, 11, 12, 15, 16 (topics TBD from transcripts)

---

## Available Artifacts per Call

Each call directory contains:

1. **VTT Transcript** (.transcript.vtt)
   - Full verbatim transcript with timestamps
   - Speaker identification
   - Primary source for quotes and attribution

2. **Chat Log** (newChat.txt)
   - Text chat during the call
   - May contain links, side conversations, resources
   - Secondary content to incorporate

3. **AI Summary PDF** (AI Summary.pdf)
   - Pre-generated summary (third-party AI)
   - Useful for quick overview
   - NOT to be used as primary source (must verify against transcript)

**Note**: Some calls have both .transcript.vtt and .cc.vtt (closed caption) files. The .transcript.vtt appears to be the more complete version.

---

## Next Steps in Phase 0

Still to complete:

1. **Participant Attendance Matrix** (_artifacts/participant-attendance.csv)
   - Requires scanning transcripts for participant names
   - Extract who attended which calls
   - Categorize as Regular/Frequent/Occasional/Guest

2. **Topic Clustering** (_artifacts/topic-clusters.json)
   - Scan transcripts/summaries for themes
   - Group related topics across calls
   - Identify recurring themes beyond explicit call titles

3. **Check-In Analysis**
   - For calls 02, 06, 14 (explicit check-ins)
   - Note if other calls also have check-in segments
   - Document check-in themes/prompts

---

## Estimated Work Remaining

### Phase 0 Completion
- Time: 3-5 hours
- Tokens: ~2-3K (lightweight scanning only)
- Next session should complete Phase 0

### Phase 1 Planning (After Phase 0)
- 16 calls ÷ batches of 3 = ~6 batches (not 5)
- Adjust batch plan:
  - Batch 1: Calls 01-03
  - Batch 2: Calls 04-06
  - Batch 3: Calls 07-09
  - Batch 4: Calls 10-12
  - Batch 5: Calls 13-15
  - Batch 6: Call 16 (just one, or combine with final review)
- Or use batches of 4 calls each = 4 batches

---

## Data Quality Notes

### Strengths
- Consistent file structure across all calls
- All transcripts and chats present
- AI summaries available for quick reference
- Clear dates and some explicit topics

### Considerations
- Nov 13 call split into 2 parts (may need special handling)
- Most calls titled "OGM Call" without explicit topic (need transcript analysis)
- Type categorization (Hybrid/Check-in/Topical) is preliminary - verify during Phase 1

---

## Artifacts Created

### This Session
- ✅ `_artifacts/call-inventory.csv` - Complete inventory of all 16 calls
- ✅ `_artifacts/phase-0-summary.md` - This document

### Still To Create (Phase 0)
- ⬜ `_artifacts/participant-attendance.csv`
- ⬜ `_artifacts/topic-clusters.json`
- ⬜ `_artifacts/check-in-analysis.md`

---

## Token Management Notes

Phase 0 work so far has used minimal tokens as designed:
- Reading file structure: negligible
- Creating inventory CSV: ~1K tokens
- Creating this summary: ~1K tokens

**Cumulative Phase 0 tokens**: ~2K (vs estimated 4K budget)

Following token-aware workflow principles:
- Created structured CSV instead of narrative description
- Documented in markdown for human readability
- Ready to commit for resumability

---

## Session Notes

- Repository name suggests date range: "ogm-2025-07-31-through-2025-11-13"
- This matches actual call date range exactly
- OGM = Open Global Mind (confirmed from directory names)
- Community appears to meet weekly
- Mix of structured topical discussions and open check-in calls
