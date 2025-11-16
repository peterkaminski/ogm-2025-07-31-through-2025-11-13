## Proposal for Token-Aware Workflow Design

Here's the hierarchical breakdown of the "Instructions for AI Assistant - Handling Many Calls Together" plan:

### **Level 0: Strategic Overview**

- **Purpose**: Create unified wiki from 15+ calls showing individual documentation AND synthesis of evolution/patterns/connections
- **Key Principle**: Both collection + synthesis (not just 15 separate wikis)
- **Estimated Scope**: 40-60 hours, 600-800 pages

### **Level 1: Major Phases**

```
Phase 0: Multi-Call Mapping (BEFORE any deep reading)
├── 0.1 Inventory all calls
├── 0.2 Map participants across calls  
├── 0.3 Topic clustering (initial)
└── 0.4 Check-in analysis

Phase 1: Per-Call Analysis
├── 1.1 Read each call completely
├── 1.2 Per-call documentation
└── 1.3 Build cross-call index while reading

Phase 2: Wiki Structure Design
├── 2.1 Multi-level structure (directories vs flat)
└── 2.2 Page templates (Call/Participant/Topic)

Phase 3: Hub Pages Creation
├── 3.1 Calls Hub
├── 3.2 Participants Hub
├── 3.3 Topics Hub
├── 3.4 Check-Ins Hub
└── 3.5 Start Here

Phase 4: Enhanced Processing Passes
├── Pass 1: Individual call processing
├── Pass 2: Participant synthesis
├── Pass 3: Topic synthesis
├── Pass 4: Pattern recognition
├── Pass 5: Cross-linking enhancement
└── Pass 6: Meta-synthesis

Phase 5: Navigation for Scale
├── 5.1 Multiple index pages (4+ types)
├── 5.2 Timeline/evolution pages
└── 5.3 Relationship maps

Phase 6: Quality Verification
├── 6.1 Cross-call consistency
├── 6.2 Completeness checks
└── 6.3 Attribution verification
```

### **Level 2: Deliverables Taxonomy**

```
Content Pages (~700 pages)
├── Call Pages (15)
├── Participant Profiles (50+)
└── Topic Synthesis Pages (100+)

Navigation Pages (~20 pages)
├── Hub Pages (5+)
├── Index Pages (4+)
└── Synthesis Pages (5+)

Meta Pages (~6 pages)
├── README/Start Here
├── About/Work Log
└── Scripts/_bin
```

## Token-Aware Workflow Design

Now, applying the insight that **we only need tokens for the current task**:

### **Critical Token Management Principles**

Update Todos

 Create hierarchical summary of current instructions

 Designing token-aware workflow improvements

### **Key Token Management Insights**

**The Problem with Current Approach:**

- Reading all 15 transcripts = potentially 500K+ tokens
- All participant data in context = another 100K+ tokens
- Trying to hold everything in memory for synthesis = context overflow

**The Solution - Hierarchical Artifact Creation:**

```
Work in Small Batches → Create Artifacts → Roll Up Summaries → Use Artifacts for Synthesis
```

### **Token-Efficient Workflow Redesign**

The key changes I'm proposing:

1. **Phase 0**: Create structured data files (CSV/JSON) instead of keeping everything in context
2. **Phase 1**: Process calls in batches of 3-5, creating artifacts after each batch
3. **Intermediate Artifacts**: Create rollup summaries at each level that can be used instead of re-reading everything
4. **Synthesis Work**: Use artifacts + targeted reads rather than loading full context
5. **Quality Checks**: Script-based validation using artifacts rather than manual context loading

#### **Phase 0: Multi-Call Mapping (Token-Efficient)**

**OLD APPROACH**: Read all transcripts to create maps → Massive token usage

**NEW APPROACH**: Create structured data artifacts from lightweight scans

**Step 0.1: Call Inventory**
```bash
# Create: _artifacts/call-inventory.csv
Call,Date,Topic,Participants,HasCheckIns,Type,TranscriptPath
01,2025-10-15,Curiosity in Education,12,Yes,Hybrid,/path/to/call01.txt
02,2025-10-22,AI and Learning,15,Yes,Topical,/path/to/call02.txt
...
```

**Token Impact**: ~1K tokens (CSV file) vs ~50K tokens (reading summaries)

**Step 0.2: Participant Attendance Matrix**
```bash
# Create: _artifacts/participant-attendance.csv
Participant,TotalCalls,FirstCall,LastCall,CallsList
Jerry Michalski,15,01,15,"01,02,03,04,05,06,07,08,09,10,11,12,13,14,15"
Pete Kaminski,14,01,15,"01,02,03,04,05,06,07,09,10,11,12,13,14,15"
...
```

**Token Impact**: ~2K tokens (CSV) vs ~20K tokens (narrative description)

**Step 0.3: Topic Clustering (Initial)**
```bash
# Create: _artifacts/topic-clusters.json
{
  "Education": {
    "calls": ["01", "05", "09"],
    "keywords": ["curiosity", "teaching", "learning"]
  },
  "AI/Technology": {
    "calls": ["02", "08", "12"],
    "keywords": ["AI", "ChatGPT", "technology"]
  }
}
```

**Token Impact**: ~1K tokens (JSON) vs ~10K tokens (narrative)

**Phase 0 Total**: 4K tokens with artifacts vs 80K tokens without

---

#### **Phase 1: Per-Call Analysis (Batched Processing)**

**OLD APPROACH**: Read all 15 calls, hold everything in context → Context overflow

**NEW APPROACH**: Process in batches of 3-5 calls, create artifacts, summarize, continue

**Batch Processing Pattern:**

```
Batch 1 (Calls 01-03):
  1. Read call 01 transcript
  2. Create: Calls/Call 01 - [Topic].md
  3. Extract to: _artifacts/call-01-data.json
  4. Read call 02 transcript
  5. Create: Calls/Call 02 - [Topic].md
  6. Extract to: _artifacts/call-02-data.json
  7. Read call 03 transcript
  8. Create: Calls/Call 03 - [Topic].md
  9. Extract to: _artifacts/call-03-data.json
  10. Create: _artifacts/batch-01-summary.md (rollup of calls 01-03)
  11. Update: _artifacts/running-topics.json
  12. Update: _artifacts/running-participants.json
  13. COMMIT artifacts and pages
  14. CLEAR CONTEXT (start fresh for next batch)

Batch 2 (Calls 04-06):
  1. Read: _artifacts/batch-01-summary.md (small context refresh)
  2. Process calls 04-06 (same pattern)
  3. Create: _artifacts/batch-02-summary.md
  4. Update running artifacts
  5. COMMIT
  6. CLEAR CONTEXT

[Repeat for batches 3, 4, 5]
```

**Token Impact per Batch**:
- Read 3 transcripts: ~30-50K tokens
- Create 3 call pages: ~10K tokens output
- Extract to JSON: ~5K tokens
- Previous batch summary: ~3K tokens
- **Total per batch**: ~50K tokens (manageable)

**Key Artifacts Created:**

1. **Call Data JSON** (`_artifacts/call-XX-data.json`):
```json
{
  "callNumber": "01",
  "date": "2025-10-15",
  "topic": "Curiosity in Education",
  "participants": ["Jerry", "Pete", "Victoria", ...],
  "checkIns": {
    "Jerry": "I'm excited about...",
    "Pete": "This week I..."
  },
  "mainTopics": ["curiosity", "education", "motivation"],
  "quotes": [
    {"speaker": "Jerry", "topic": "curiosity", "quote": "..."}
  ],
  "stories": [
    {"teller": "Kevin", "topic": "cobra", "summary": "..."}
  ],
  "frameworks": ["Framework X"],
  "questions": ["How do we measure curiosity?"]
}
```

2. **Batch Summary** (`_artifacts/batch-XX-summary.md`):
```markdown
# Batch 01 Summary (Calls 01-03)

## Calls Processed
- Call 01: Curiosity in Education (12 participants)
- Call 02: AI and Learning (15 participants)
- Call 03: Systems Thinking (10 participants)

## Emerging Topics
- Curiosity: Strong theme in calls 01, 03
- AI: Introduced in call 02
- Education: Present in all three

## New Participants This Batch
- First-timers: Jane (call 02), Alex (call 03)
- Regular attendees: Jerry, Pete, Victoria

## Topics for Cross-Call Tracking
- Curiosity: Needs topic page (appears 2+ times)
- AI/Education: Needs topic page (appears 2+ times)

## Questions to Watch
- "How do we measure curiosity?" (Call 01, unresolved)
```

3. **Running Topics JSON** (`_artifacts/running-topics.json`):
```json
{
  "curiosity": {
    "calls": ["01", "03"],
    "contributors": ["Jerry", "Pete", "Kevin"],
    "needsTopicPage": true
  },
  "AI": {
    "calls": ["02"],
    "contributors": ["Pete", "Alex"],
    "needsTopicPage": false
  }
}
```

**After All Batches Complete**:
- 15 call pages created ✓
- 15 call-data JSON files ✓
- 5 batch summaries ✓
- Updated running artifacts ✓
- Total tokens used: ~250K across 5 batches (vs 500K+ in one session)

---

#### **Phase 2 & 3: Structure & Hub Pages (Artifact-Driven)**

**OLD APPROACH**: Re-read calls to create hub pages → Re-reading = wasted tokens

**NEW APPROACH**: Use artifacts created in Phase 1

**Example: Creating Calls Hub**

```
Input artifacts:
- _artifacts/call-inventory.csv
- _artifacts/batch-01-summary.md through batch-05-summary.md
- _artifacts/topic-clusters.json

Token cost: ~10K (reading artifacts) vs ~100K (re-reading all calls)

Output: Hub - Calls.md
```

**Example: Creating Participants Hub**

```
Input artifacts:
- _artifacts/participant-attendance.csv
- _artifacts/running-participants.json
- Batch summaries (for context on who contributed what)

Token cost: ~8K vs ~80K
```

---

#### **Phase 4: Synthesis Passes (Targeted Artifact Use)**

**Pass 2: Participant Synthesis**

**OLD APPROACH**: Read all 15 calls to synthesize each participant → 500K+ tokens per participant

**NEW APPROACH**: Use call-data JSONs + targeted reads

```
For participant "Jerry Michalski":
1. Read: _artifacts/participant-attendance.csv → Get Jerry's call list
2. Read: All relevant call-XX-data.json files (only Jerry's sections)
3. Token cost: ~15K per participant
4. Create: Participants/Jerry Michalski.md
5. For quotes/verification: Targeted read of specific calls/sections
```

**Pass 3: Topic Synthesis**

```
For topic "Curiosity":
1. Read: _artifacts/running-topics.json → Get calls where discussed
2. Read: Relevant call-XX-data.json files (only curiosity sections)
3. Token cost: ~10K per topic
4. Create: Topics/Topic - Curiosity.md
5. For detailed quotes: Targeted read of specific calls
```

**Pass 4: Pattern Recognition**

```
Input artifacts:
- All batch summaries (~15K tokens total)
- running-topics.json
- running-participants.json
- call-inventory.csv

Token cost: ~20K vs ~500K for re-reading everything

Output: Synthesis/Patterns Across Calls.md
```

---

#### **Phase 6: Quality Verification (Script-Based)**

**OLD APPROACH**: Manual verification by re-reading → Massive tokens

**NEW APPROACH**: Automated scripts + targeted verification

**Script 1: Orphan Link Checker**
```python
# _bin/check-orphan-links.py
# Reads all .md files, finds [[links]], checks if targets exist
# Token cost: 0 (runs locally)
```

**Script 2: Attribution Verifier**
```python
# _bin/verify-attributions.py
# Checks participant-attendance.csv against claims
# Flags: "Person X said Y in Call Z" when X wasn't in Call Z
# Token cost: 0 (runs locally)
```

**Script 3: Completeness Checker**
```python
# _bin/check-completeness.py
# Verifies all calls have pages, all participants have profiles, etc.
# Token cost: 0 (runs locally)
```

---

### **Complete Token Budget Comparison**

| Phase | Old Approach | New Approach | Savings |
|-------|-------------|--------------|---------|
| Phase 0: Mapping | 80K | 4K | 76K |
| Phase 1: All calls (5 batches) | 500K+ | 250K | 250K+ |
| Phase 2-3: Hubs | 200K | 30K | 170K |
| Phase 4: Synthesis | 1000K+ | 100K | 900K+ |
| Phase 6: Quality | 200K | 10K | 190K |
| **TOTAL** | **~2000K** | **~400K** | **~1600K (80% savings)** |

---

### **Key Workflow Principles**

1. **Create Artifacts Early and Often**
   - Every time you process something, extract structured data
   - JSON for machine-readable, MD for human-readable summaries
   - Commit frequently so work can be resumed

2. **Batch Processing with Context Clearing**
   - Process 3-5 calls per batch
   - Create batch summary
   - Commit everything
   - Start fresh (previous batch = just read the summary)

3. **Use Structured Data Over Narrative**
   - CSV/JSON for facts (participants, dates, topics)
   - Markdown summaries for synthesis
   - Scripts for validation

4. **Targeted Reads Over Full Context**
   - When synthesizing, read only relevant sections
   - Use artifacts to know where to look
   - Don't re-read entire transcripts

5. **Intermediate Summaries as Stepping Stones**
   - Batch summaries prevent re-reading batches
   - Running artifacts track cumulative state
   - Each level summarizes the level below

6. **Commit Artifacts for Resumability**
   - Another AI (or same AI in new session) can pick up where you left off
   - Artifacts contain all the extracted knowledge
   - No need to re-process if interrupted

---

### **Artifact Directory Structure**

```
_artifacts/
├── call-inventory.csv          # Phase 0 output
├── participant-attendance.csv   # Phase 0 output
├── topic-clusters.json         # Phase 0 output
├── call-01-data.json           # Phase 1 per-call data
├── call-02-data.json
├── ...
├── call-15-data.json
├── batch-01-summary.md         # Phase 1 batch rollups
├── batch-02-summary.md
├── ...
├── batch-05-summary.md
├── running-topics.json         # Updated throughout Phase 1
├── running-participants.json   # Updated throughout Phase 1
├── synthesis-notes.md          # Phase 4 working notes
└── verification-log.md         # Phase 6 QA results
```

---

### **Updated Workflow Timeline**

**Week 1: Mapping + First Batch**
- Day 1-2: Phase 0 (create inventories, CSV files)
- Day 3-5: Batch 1 (calls 01-03)
- Tokens used: ~60K
- Commits: 3-4

**Week 2: Batches 2-3**
- Day 1-2: Batch 2 (calls 04-06)
- Day 3-5: Batch 3 (calls 07-09)
- Tokens used: ~100K
- Commits: 2

**Week 3: Batches 4-5 + Hubs**
- Day 1-2: Batch 4 (calls 10-12)
- Day 3: Batch 5 (calls 13-15)
- Day 4-5: Hub pages (using artifacts)
- Tokens used: ~120K
- Commits: 3

**Week 4: Synthesis**
- Day 1-2: Participant synthesis (using artifacts)
- Day 3-4: Topic synthesis (using artifacts)
- Day 5: Pattern recognition
- Tokens used: ~100K
- Commits: 5

**Week 5: Polish + Quality**
- Day 1-2: Cross-linking
- Day 3-4: Meta-synthesis pages
- Day 5: Quality verification (scripts)
- Tokens used: ~20K
- Commits: 3

**Total: ~400K tokens across 5 weeks** (vs ~2M tokens in old approach)

---

### **Resumability After Interruption**

If work is interrupted at any point:

1. **Read work-log.md** → See what was completed
2. **Read latest batch-summary.md** → Understand current state
3. **Check _artifacts/** → See what data exists
4. **Read detailed-todo-list.md** → See what's next
5. **Continue from next task** → No re-processing needed

**Token cost to resume**: ~5-10K (read summaries) vs 200K+ (re-read everything)

---

### **Implementation Checklist**

For AI assistants following this workflow:

- [ ] Start each phase by checking what artifacts exist
- [ ] Create artifacts BEFORE creating final pages
- [ ] Commit artifacts immediately when created
- [ ] Process calls in batches of 3-5, never all at once
- [ ] Create batch summaries after each batch
- [ ] Use artifacts for synthesis, not re-reading transcripts
- [ ] Update work-log.md after each session
- [ ] Update detailed-todo-list.md to track progress
- [ ] Write scripts for validation, not manual re-reading
- [ ] When resuming work, read artifacts first, not transcripts

---

## Summary

This token-aware workflow redesign makes the multi-call wiki process:

1. **Scalable**: Can handle 15 calls or 150 calls with same approach
2. **Resumable**: Can be picked up by any AI at any point
3. **Efficient**: Uses 80% fewer tokens through artifact creation
4. **Maintainable**: Structured data enables scripts and validation
5. **Auditable**: Clear artifacts show what was processed and when

The key insight: **We don't need all the data in context, we need the right data in context at the right time.** Artifacts enable this by providing structured, queryable representations of processed information.