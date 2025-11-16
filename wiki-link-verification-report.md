# Wiki Link Verification Report

**Date**: 2025-11-16
**Total markdown files scanned**: 63
**Total internal links checked**: 839
**Broken links found**: 72

---

## Summary

Overall link health: **91.4% working** (767 valid / 839 total)

### Issues by Type

1. **ANCHOR_NOT_FOUND**: 43 issues (59.7%)
2. **FILE_NOT_FOUND**: 29 issues (40.3%)

---

## Broken Link Details

### 1. Anchor Links (43 issues)

These are links where the target file exists but the anchor (section heading) doesn't match. This is primarily due to section headers in Topics Hub having call numbers appended.

**Common Patterns**:

#### In Frameworks.md (11 anchor issues):
- `#curiosity-and-epistemology` → should be `#curiosity-and-epistemology-calls-15-16`
- `#abundance` → should be `#abundance-call-08`
- `#third-places` → should be `#third-places-call-06`
- `#ai-as-conversation-participant` → should be `#ai-as-conversation-participant-call-10`
- `#collaboration-theory-and-practice` → should be `#collaboration-theory-and-practice-calls-02-07-09`
- `#information-trust-and-disinformation` → should be `#trust-and-information-calls-01-03-04-11`
- `#grief-and-trauma` → should be `#grief-and-trauma-processing-call-01`
- `#worldview-challenges-and-narratives` → should be `#worldview-challenges-and-narratives-calls-11-12-15`

#### In indexes/ files (32 anchor issues):
- Alphabetical-Index.md, Thematic-Index.md, Timeline.md all have similar anchor issues
- All pointing to Topics Hub sections that need call numbers appended

**Root Cause**: Topics Hub uses more specific anchor IDs (with call numbers) than what's referenced in links.

---

### 2. Missing Files (29 issues)

#### A. Artifact Files (18 issues)
Links to `../../_artifacts/` files that exist outside the wiki directory:

**Affected files**:
- Calls Hub.md: Links to all 6 batch summary files
- All 16 Call-*.md files: Each links to batch summary and call data JSON
- topics/*.md files: Link to batch summaries

**Files referenced but not in wiki**:
- `batch-01-summary.md` through `batch-06-summary.md`
- `call-01-data.json` through `call-16-data.json`
- `phase-0-summary.md`
- `running-topics.json`
- `participant-attendance.csv`

**Note**: These files exist at `/home/user/ogm-2025-07-31-through-2025-11-13/_artifacts/` but are outside the wiki directory structure.

#### B. Transcript Files (11 issues)
All Call-*.md files link to transcript .vtt files in parent directories:

**Pattern**: `../../2025-MM-DD OGM Call/GMT*.transcript.vtt`

**Note**: These transcripts exist in the parent directory but are outside wiki scope.

#### C. URL-Encoded Links (6 issues in topics/*.md files)

**Problem**: Links use `%20` for spaces instead of regular spaces

**Files affected**:
- topics/AI-and-Technology-Evolution.md
- topics/Definitions-Obsession.md
- topics/OGM-Identity-Journey.md
- topics/Trust-and-Information-Crisis.md

**Examples**:
- `../Calls%20Hub.md` → should be `../Calls Hub.md`
- `../Topics%20Hub.md` → should be `../Topics Hub.md`
- `../Participants%20Hub.md` → should be `../Participants Hub.md`

---

## Recommendations

### High Priority (Breaking Navigation)

1. **Fix URL-encoded links in topics/ files** (6 issues)
   - Replace `%20` with regular spaces in markdown links
   - Files: AI-and-Technology-Evolution.md, Definitions-Obsession.md, OGM-Identity-Journey.md, Trust-and-Information-Crisis.md

2. **Fix anchor links** (43 issues)
   - Update Frameworks.md anchor links to match Topics Hub section IDs
   - Update all index files to use correct anchor formats with call numbers

### Medium Priority (Documentation Links)

3. **Consider artifact file strategy**:
   - Option A: Copy relevant _artifacts files into wiki structure
   - Option B: Update links to point outside wiki (acknowledge external references)
   - Option C: Remove links to artifacts (keep wiki self-contained)

4. **Consider transcript file strategy**:
   - Option A: Move transcripts into wiki structure
   - Option B: Keep links (acknowledge external references)
   - Option C: Remove transcript links (wiki focuses on summaries)

### Low Priority (Enhancement)

5. **Add link validation to CI/CD**:
   - Run verification script on updates
   - Prevent broken links from being committed

---

## Files Requiring Updates

### Immediate Fixes Required

**High impact files with URL-encoding issues**:
1. `/home/user/ogm-2025-07-31-through-2025-11-13/wiki/topics/AI-and-Technology-Evolution.md`
2. `/home/user/ogm-2025-07-31-through-2025-11-13/wiki/topics/Definitions-Obsession.md`
3. `/home/user/ogm-2025-07-31-through-2025-11-13/wiki/topics/OGM-Identity-Journey.md`
4. `/home/user/ogm-2025-07-31-through-2025-11-13/wiki/topics/Trust-and-Information-Crisis.md`

**Files with anchor issues**:
1. `/home/user/ogm-2025-07-31-through-2025-11-13/wiki/Frameworks.md` (11 broken anchors)
2. `/home/user/ogm-2025-07-31-through-2025-11-13/wiki/indexes/Alphabetical-Index.md` (12 broken anchors)
3. `/home/user/ogm-2025-07-31-through-2025-11-13/wiki/indexes/Thematic-Index.md` (10 broken anchors)
4. `/home/user/ogm-2025-07-31-through-2025-11-13/wiki/indexes/Timeline.md` (10 broken anchors)

---

## Positive Findings

**What's working well**:
- All hub-to-hub navigation links work correctly
- All participant profile cross-links work correctly
- All call-to-call navigation works correctly
- All hub-to-participant links work correctly
- All hub-to-call links work correctly
- Internal wiki structure is solid and well-interconnected

**Coverage**:
- 91.4% of internal links are working correctly
- Issues are concentrated in specific areas (anchors and external references)
- No structural problems with the wiki architecture itself

---

## Next Steps

1. **Immediate**: Fix URL-encoded links in topics/ files (quick fix, high impact)
2. **Soon**: Update anchor links in Frameworks.md and index files
3. **Consider**: Strategy for external file references (_artifacts and transcripts)
4. **Future**: Add automated link checking to prevent regressions
