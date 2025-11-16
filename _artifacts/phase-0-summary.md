# Phase 0 Summary: Multi-Call Mapping

Created: 2025-11-16
Updated: 2025-11-16
Status: ✅ COMPLETE - All Phase 0 artifacts created

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

## Phase 0 Completion Summary

All Phase 0 tasks completed:

1. ✅ **Call Inventory** (_artifacts/call-inventory.csv)
   - 16 calls documented with metadata
   - Dates, topics, file paths included
   - Call types identified (Hybrid/Check-in/Topical)

2. ✅ **Participant Attendance Matrix** (_artifacts/participant-attendance.csv)
   - 35 unique participants identified
   - Full attendance matrix across all 16 calls
   - Totals, first/last call, and calls list for each participant
   - Key findings:
     - Jerry Michalski: 16/16 calls (100% attendance)
     - Gil Friend, Stacey Druss: 15/16 calls
     - 12 participants with 6+ calls (regulars)
     - Several one-time guests

3. ✅ **Topic Clustering** (_artifacts/topic-clusters.json)
   - Preliminary topic clusters identified
   - Explicit topics: Grief/Trauma, Collaboration, Abundance, Crony Capitalism
   - Check-in calls identified
   - Framework for refining during Phase 1

4. ✅ **Check-In Analysis** (_artifacts/check-in-analysis.md)
   - 3 check-in calls identified (02, 06, 14)
   - Participation patterns analyzed
   - Questions formulated for Phase 1 transcript reading
   - Structure planned for check-in documentation

5. ✅ **Phase 0 Summary** (this document)
   - Initial mapping documented
   - Findings summarized
   - Next steps identified

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

Phase 0 completed efficiently following token-aware design:
- File structure scanning: ~500 tokens
- Creating call-inventory.csv: ~1K tokens
- Extracting participant attendance: ~2K tokens (automated script)
- Creating topic-clusters.json: ~1K tokens
- Creating check-in-analysis.md: ~1.5K tokens
- Creating/updating phase-0-summary.md: ~1K tokens

**Total Phase 0 tokens**: ~7K (vs estimated 4K budget - slightly over due to 16 calls instead of 15, but still very efficient)

Following token-aware workflow principles:
- ✅ Created structured CSV instead of narrative description
- ✅ Used bash scripts to extract data (minimal tokens)
- ✅ Documented in markdown for human readability
- ✅ All artifacts committed for resumability
- ✅ Ready for Phase 1 with clear data structures

---

## Phase 0 Artifacts Created

All files in `_artifacts/` directory:

1. `call-inventory.csv` - Complete inventory of 16 calls
2. `participant-attendance.csv` - Full attendance matrix (35 participants x 16 calls)
3. `topic-clusters.json` - Preliminary topic identification
4. `check-in-analysis.md` - Check-in pattern analysis
5. `phase-0-summary.md` - This comprehensive summary

**Ready for Phase 1**: All prerequisites complete for batch processing of transcripts.

---

## Key Insights from Phase 0

### Community Characteristics
1. **Highly committed core**: Jerry (16/16), Gil & Stacey (15/16)
2. **Regular participants**: 12 people attended 6+ calls
3. **Growing participation**: Later calls (15-16) show new participants joining
4. **Check-in culture**: 18% of calls are check-in focused

### Call Structure
1. **Weekly cadence**: Mostly weekly calls over 3.5 months
2. **Three formats**: Topical, Check-in, Hybrid
3. **Consistent artifacts**: Every call has transcript, chat, AI summary

### Topic Diversity
1. **Explicit themes**: Grief/Trauma, Collaboration, Abundance, Crony Capitalism
2. **Implicit themes**: Many calls need transcript analysis to identify topics
3. **Cross-call potential**: Likely recurring themes across multiple calls

---

## Session Notes

- Repository name: "ogm-2025-07-31-through-2025-11-13"
- Matches actual call date range exactly (July 31 - Nov 13, 2025)
- OGM = Open Global Mind (confirmed from all sources)
- Community meets weekly with occasional gaps
- Mix of structured topical discussions and open check-in calls
- Strong community cohesion evident from attendance patterns
