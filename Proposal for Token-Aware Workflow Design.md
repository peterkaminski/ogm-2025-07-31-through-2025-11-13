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

I'll outline how each phase should be restructured for token efficiency. The key changes I'm proposing:

1. **Phase 0**: Create structured data files (CSV/JSON) instead of keeping everything in context
2. **Phase 1**: Process calls in batches of 3-5, creating artifacts after each batch
3. **Intermediate Artifacts**: Create rollup summaries at each level that can be used instead of re-reading everything
4. **Synthesis Work**: Use artifacts + targeted reads rather than loading full context
5. **Quality Checks**: Script-based validation using artifacts rather than manual context loading