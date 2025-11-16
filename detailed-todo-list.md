# Detailed Todo List - Multi-Call Wiki Project

This file tracks all tasks for the project. Update status as work progresses.

**Legend:**
- ✅ Completed
- ⏳ In Progress
- ⬜ Pending
- ⏸️ Blocked
- ❌ Cancelled

Last updated: 2025-11-16

---

## Meta Tasks

- [✅] Read and validate Token-Aware Workflow Design proposal
- [✅] Complete the proposal with implementation details
- [✅] Incorporate token management into Instructions document
- [✅] Create work-log.md for session tracking
- [✅] Create detailed-todo-list.md (this file)
- [⬜] Push completed work to remote branch

---

## Phase 0: Multi-Call Mapping

**Goal**: Create structured data artifacts before deep reading. Token budget: ~4K

### Setup
- [⬜] Create _artifacts/ directory
- [⬜] Check what call transcripts/artifacts are available in the repository
- [⬜] Document available source materials

### 0.1 Call Inventory
- [⬜] Create _artifacts/call-inventory.csv
  - Columns: Call, Date, Topic, Participants, HasCheckIns, Type, TranscriptPath
  - List all 15 calls with metadata
- [⬜] Verify all transcript paths are accessible

### 0.2 Participant Attendance Matrix
- [⬜] Create _artifacts/participant-attendance.csv
  - Columns: Participant, TotalCalls, FirstCall, LastCall, CallsList
  - Extract from lightweight scan of transcripts
- [⬜] Categorize participants (Regulars, Frequent, Occasional, Guests)

### 0.3 Topic Clustering (Initial)
- [⬜] Create _artifacts/topic-clusters.json
  - Initial topic clusters from call titles/descriptions
  - Keywords for each cluster
  - Calls associated with each cluster

### 0.4 Check-In Analysis
- [⬜] Document check-in patterns across calls
- [⬜] Note structured vs freeform check-ins

### Phase 0 Completion
- [⬜] Verify all Phase 0 artifacts created
- [⬜] Commit Phase 0 artifacts
- [⬜] Update work-log.md
- [⬜] Update this todo list

**Estimated tokens**: 4K | **Estimated time**: 4-6 hours

---

## Phase 1: Per-Call Analysis (Batched)

**Goal**: Process all 15 calls in 5 batches, creating call pages and structured artifacts. Token budget: ~250K total.

### Batch 1: Calls 01-03

- [⬜] Read call 01 transcript completely
  - [⬜] Read transcript file
  - [⬜] Read chat log (if available)
  - [⬜] Review any visual artifacts
- [⬜] Create Calls/Call 01 - [Topic].md (full summary page)
- [⬜] Create _artifacts/call-01-data.json (structured extraction)
- [⬜] Update _artifacts/running-topics.json
- [⬜] Update _artifacts/running-participants.json

- [⬜] Read call 02 transcript completely
- [⬜] Create Calls/Call 02 - [Topic].md
- [⬜] Create _artifacts/call-02-data.json
- [⬜] Update running artifacts

- [⬜] Read call 03 transcript completely
- [⬜] Create Calls/Call 03 - [Topic].md
- [⬜] Create _artifacts/call-03-data.json
- [⬜] Update running artifacts

- [⬜] Create _artifacts/batch-01-summary.md (rollup of calls 01-03)
- [⬜] Commit Batch 1 artifacts and pages
- [⬜] Update work-log.md
- [⬜] Update this todo list

**Estimated tokens**: 50K | **Estimated time**: 8-10 hours

### Batch 2: Calls 04-06

- [⬜] Read _artifacts/batch-01-summary.md (context refresh)
- [⬜] Process call 04 (transcript → page → JSON → update running artifacts)
- [⬜] Process call 05
- [⬜] Process call 06
- [⬜] Create _artifacts/batch-02-summary.md
- [⬜] Commit Batch 2 artifacts and pages
- [⬜] Update work-log.md
- [⬜] Update this todo list

**Estimated tokens**: 50K | **Estimated time**: 8-10 hours

### Batch 3: Calls 07-09

- [⬜] Read _artifacts/batch-02-summary.md
- [⬜] Process calls 07-09 (same pattern)
- [⬜] Create _artifacts/batch-03-summary.md
- [⬜] Commit Batch 3
- [⬜] Update logs

**Estimated tokens**: 50K | **Estimated time**: 8-10 hours

### Batch 4: Calls 10-12

- [⬜] Read _artifacts/batch-03-summary.md
- [⬜] Process calls 10-12
- [⬜] Create _artifacts/batch-04-summary.md
- [⬜] Commit Batch 4
- [⬜] Update logs

**Estimated tokens**: 50K | **Estimated time**: 8-10 hours

### Batch 5: Calls 13-15

- [⬜] Read _artifacts/batch-04-summary.md
- [⬜] Process calls 13-15
- [⬜] Create _artifacts/batch-05-summary.md
- [⬜] Commit Batch 5
- [⬜] Update logs

**Estimated tokens**: 50K | **Estimated time**: 6-8 hours

### Phase 1 Completion
- [⬜] Verify all 15 call pages created
- [⬜] Verify all 15 call-data.json files created
- [⬜] Verify all 5 batch summaries created
- [⬜] Verify running-topics.json is complete
- [⬜] Verify running-participants.json is complete

**Total Phase 1**: ~250K tokens | ~40-50 hours

---

## Phase 2: Wiki Structure Design

**Goal**: Set up directory structure and page templates. Token budget: ~5K

- [⬜] Decide on directory structure (Option A: Flat with prefixes, Option B: Directories)
- [⬜] Create directory structure
  - [⬜] Calls/ (or use flat with "Call XX -" prefix)
  - [⬜] Participants/
  - [⬜] Topics/
  - [⬜] CheckIns/
  - [⬜] Indexes/
  - [⬜] Synthesis/
- [⬜] Create template files or documentation for:
  - [⬜] Call summary page template
  - [⬜] Participant profile template
  - [⬜] Topic synthesis template
  - [⬜] Hub page template
- [⬜] Commit structure
- [⬜] Update logs

**Estimated tokens**: 5K | **Estimated time**: 2-3 hours

---

## Phase 3: Hub Pages Creation

**Goal**: Create navigation hub pages using artifacts (NOT re-reading transcripts). Token budget: ~15K

### 3.1 Calls Hub
- [⬜] Create Calls Hub.md or Hub - Calls.md
  - Input: call-inventory.csv, batch summaries
  - Sections: All calls by date, By topic cluster, By type, Timeline view

### 3.2 Participants Hub
- [⬜] Create Participants Hub.md
  - Input: participant-attendance.csv, running-participants.json
  - Sections: Regulars, Frequent, Occasional, Guests, Attendance matrix

### 3.3 Topics Hub
- [⬜] Create Topics Hub.md
  - Input: running-topics.json, topic-clusters.json
  - Sections: Core recurring topics, Topic clusters, Evolution map

### 3.4 Check-Ins Hub
- [⬜] Create Check-Ins Hub.md
  - Input: call-data.json files (checkIns sections)
  - Sections: By call, By participant, Themes in check-ins

### 3.5 Start Here
- [⬜] Create Start Here.md
  - Navigation guide with 5+ curated paths
  - Quick stats
  - Browse by options

### Phase 3 Completion
- [⬜] Verify all 5 hub pages created
- [⬜] Commit hub pages
- [⬜] Update logs

**Estimated tokens**: 15K | **Estimated time**: 4-6 hours

---

## Phase 4: Enhanced Processing Passes (Synthesis)

**Goal**: Create participant profiles, topic pages, and pattern analysis using artifacts. Token budget: ~100K

### Pass 2: Participant Synthesis

- [⬜] Identify all unique participants from participant-attendance.csv
- [⬜] For each regular participant (attend >60%):
  - [⬜] Read participant-attendance.csv for their call list
  - [⬜] Read relevant call-XX-data.json files
  - [⬜] Create Participants/[Name].md with evolution across calls
  - [⬜] Include: contributions, check-ins, topics engaged, stories told
- [⬜] For frequent participants (30-60%), create profiles
- [⬜] For occasional participants (10-30%), create profiles or add to hub
- [⬜] Document guest participants in hub only

**Estimated tokens**: ~15K per participant (targeted reads)
**Estimated time**: 8-12 hours for all participants

### Pass 3: Topic Synthesis

- [⬜] Identify all recurring topics from running-topics.json
- [⬜] For each topic that appears in 2+ calls:
  - [⬜] Read running-topics.json for call list
  - [⬜] Read relevant call-XX-data.json files (topic sections only)
  - [⬜] Create Topics/Topic - [Name].md
  - [⬜] Show evolution across calls
  - [⬜] Document key contributors
  - [⬜] Track unresolved questions

**Estimated tokens**: ~10K per topic (targeted reads)
**Estimated time**: 8-12 hours for all topics

### Pass 4: Pattern Recognition

- [⬜] Read all batch summaries (batch-01 through batch-05)
- [⬜] Read running-topics.json and running-participants.json
- [⬜] Identify patterns:
  - [⬜] Recurring debates
  - [⬜] Evolution of thinking
  - [⬜] Topic relationships
  - [⬜] Participant relationships
  - [⬜] Check-in patterns
  - [⬜] Seasonal variations
- [⬜] Create Synthesis/Patterns Across Calls.md
- [⬜] Create Synthesis/Evolution of Ideas.md
- [⬜] Create topic relationship map
- [⬜] Create participant collaboration network

**Estimated tokens**: ~20K
**Estimated time**: 6-8 hours

### Phase 4 Completion
- [⬜] Verify all participant profiles created
- [⬜] Verify all topic synthesis pages created
- [⬜] Verify pattern/synthesis pages created
- [⬜] Commit all synthesis work
- [⬜] Update logs

**Total Phase 4**: ~100K tokens | ~25-35 hours

---

## Phase 5: Navigation for Scale

**Goal**: Create index pages and navigation aids. Token budget: ~15K

### 5.1 Index Pages

- [⬜] Create Indexes/By Date.md (chronological view)
- [⬜] Create Indexes/By Topic.md (thematic organization)
- [⬜] Create Indexes/By Participant.md (who said what)
- [⬜] Create Indexes/Alphabetical Index.md (A-Z of everything)

### 5.2 Timeline/Evolution Pages

- [⬜] Create timeline visualization or markdown timeline
- [⬜] For key topics, create evolution pages showing development over time

### 5.3 Relationship Maps

- [⬜] Create topic relationship map (if not done in Phase 4)
- [⬜] Create participant collaboration network (if not done in Phase 4)

### Phase 5 Completion
- [⬜] Verify all index pages created
- [⬜] Verify navigation paths work
- [⬜] Commit navigation work
- [⬜] Update logs

**Estimated tokens**: 15K | **Estimated time**: 4-6 hours

---

## Phase 6: Quality Verification & Cross-Linking

**Goal**: Verify quality, add cross-links, run validation scripts. Token budget: ~10K

### 6.1 Cross-Call Consistency

- [⬜] Verify participant names are consistent across all pages
- [⬜] Verify topic names are consistent
- [⬜] Verify dates and chronology are accurate
- [⬜] Verify call number references are correct
- [⬜] Verify "previous call" and "next call" links work

### 6.2 Completeness Checks

- [⬜] Verify every call has a summary page
- [⬜] Verify every participant has profile (or is listed in hub)
- [⬜] Verify recurring topics have synthesis pages
- [⬜] Verify all check-ins are captured
- [⬜] Verify all hub pages exist
- [⬜] Verify all index pages exist

### 6.3 Attribution Verification

- [⬜] Spot-check attributions against transcripts
- [⬜] Verify "Person X said Y in Call Z" matches attendance
- [⬜] Verify evolution claims have support across calls

### 6.4 Cross-Linking Enhancement

- [⬜] Add "Discussed in these calls" to topic pages
- [⬜] Add "Related topics" to call pages
- [⬜] Add "Also discussed by" to participant pages
- [⬜] Create bidirectional "See also" sections
- [⬜] Build navigation paths

### 6.5 Scripts and Automation

- [⬜] Create _bin/ directory
- [⬜] Write _bin/check-orphan-links.py (find broken [[links]])
- [⬜] Write _bin/verify-attributions.py (check attendance vs claims)
- [⬜] Write _bin/check-completeness.py (verify all pages exist)
- [⬜] Run all scripts and fix issues
- [⬜] Document results in _artifacts/verification-log.md

### Phase 6 Completion
- [⬜] All quality checks passed
- [⬜] All scripts created and run
- [⬜] Zero orphan links
- [⬜] All cross-references verified
- [⬜] Commit quality improvements
- [⬜] Update logs

**Estimated tokens**: 10K | **Estimated time**: 6-8 hours

---

## Final Documentation

**Goal**: Create user-facing documentation. Token budget: ~10K

- [⬜] Create README.md
  - Overview of the wiki
  - What's included (15 calls, dates, participants)
  - How to navigate
  - Link to Start Here.md
- [⬜] Create About This Wiki.md
  - Explanation of structure
  - How it was created
  - Token-aware workflow used
  - Attribution principles
- [⬜] Update work-log.md with final summary
- [⬜] Review this todo list and mark all items complete

**Estimated tokens**: 10K | **Estimated time**: 2-4 hours

---

## Project Completion

- [⬜] Final review of all pages
- [⬜] Final commit of all work
- [⬜] Push to remote branch
- [⬜] Create summary report of what was accomplished
- [⬜] Document token usage vs estimates

---

## Token Budget Summary

| Phase | Estimated Tokens | Actual Tokens | Estimated Time | Actual Time |
|-------|-----------------|---------------|----------------|-------------|
| Setup & Meta | 50K | 46K (partial) | 4 hours | [TBD] |
| Phase 0: Mapping | 4K | [TBD] | 4-6 hours | [TBD] |
| Phase 1: Batch 1 | 50K | [TBD] | 8-10 hours | [TBD] |
| Phase 1: Batch 2 | 50K | [TBD] | 8-10 hours | [TBD] |
| Phase 1: Batch 3 | 50K | [TBD] | 8-10 hours | [TBD] |
| Phase 1: Batch 4 | 50K | [TBD] | 8-10 hours | [TBD] |
| Phase 1: Batch 5 | 50K | [TBD] | 6-8 hours | [TBD] |
| Phase 2: Structure | 5K | [TBD] | 2-3 hours | [TBD] |
| Phase 3: Hubs | 15K | [TBD] | 4-6 hours | [TBD] |
| Phase 4: Synthesis | 100K | [TBD] | 25-35 hours | [TBD] |
| Phase 5: Navigation | 15K | [TBD] | 4-6 hours | [TBD] |
| Phase 6: Quality | 10K | [TBD] | 6-8 hours | [TBD] |
| Final Docs | 10K | [TBD] | 2-4 hours | [TBD] |
| **TOTAL** | **~450K** | **[TBD]** | **80-110 hours** | **[TBD]** |

---

## Notes

- This todo list should be updated after every work session
- Mark items complete as soon as they're done
- Add new items if unexpected tasks arise
- Update token and time estimates based on actual usage
- Use this list to resume work after any interruption
