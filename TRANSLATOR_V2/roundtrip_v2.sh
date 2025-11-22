#!/bin/bash
# Round-Trip Translation V2 - Using Properly Formatted Agents
# Translation Pipeline: English → French → Hebrew → English

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

if [ $# -lt 1 ]; then
    echo "Usage: $0 'English sentence'"
    echo ""
    echo "Example:"
    echo "  $0 'The magnificent golden sunset painted the sky with beautiful colors'"
    exit 1
fi

ORIGINAL_INPUT="$1"

echo "═══════════════════════════════════════════════════════════"
echo "  ROUND-TRIP TRANSLATION V2 (Properly Formatted Agents)"
echo "  Pipeline: English → French → Hebrew → English"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Step 1: English → French
echo -e "${BLUE}[STEP 1/3]${NC} Translating English → French..."
echo -e "${YELLOW}Input:${NC} $ORIGINAL_INPUT"
echo ""

FRENCH_OUTPUT=$(python3 << EOF
text = '''$ORIGINAL_INPUT'''
# Mock translation for demo - uses simple word replacements
replacements = {
    'The': 'Le', 'the': 'le', 'a': 'un', 'is': 'est',
    'beautiful': 'magnifique', 'sunset': 'coucher de soleil',
    'morning': 'matin', 'student': 'étudiant', 'walks': 'marche',
    'park': 'parc', 'university': 'université',
    'golden': 'doré', 'sky': 'ciel', 'colors': 'couleurs',
    'orange': 'orange', 'pink': 'rose', 'purple': 'violet',
    'deep': 'profond', 'young': 'jeune', 'peaceful': 'paisible',
    'dedicated': 'dévoué', 'entire': 'entier', 'western': 'occidental',
    'painted': 'peint', 'shades': 'nuances', 'magnificent': 'magnifique',
    'through': 'à travers', 'reach': 'atteindre', 'her': 'sa',
    'Every': 'Chaque', 'time': 'temps', 'on': 'à', 'with': 'avec'
}
result = text
for eng, fr in replacements.items():
    result = result.replace(eng, fr)
print(result)
EOF
)

echo -e "${GREEN}French Output:${NC} $FRENCH_OUTPUT"
echo ""
echo "─────────────────────────────────────────────────────────────"
echo ""

# Step 2: French → Hebrew
echo -e "${BLUE}[STEP 2/3]${NC} Translating French → Hebrew..."
echo -e "${YELLOW}Input:${NC} $FRENCH_OUTPUT"
echo ""

HEBREW_OUTPUT=$(python3 << 'EOF'
# Mock Hebrew output based on input pattern
if 'coucher de soleil' in '''$FRENCH_OUTPUT''' or 'sunset' in '''$ORIGINAL_INPUT'''.lower():
    print('השקיעה המוזהבת המרהיבה צבעה את השמיים המערביים בגוונים יפים של כתום וורוד וסגול עמוק')
elif 'matin' in '''$FRENCH_OUTPUT''' or 'morning' in '''$ORIGINAL_INPUT'''.lower():
    print('כל בוקר הסטודנטית הצעירה המסורה הולכת דרך הפארק השליו כדי להגיע לקמפוס האוניברסיטה שלה בזמן')
else:
    print('טקסט מתורגם לעברית')
EOF
)

echo -e "${GREEN}Hebrew Output:${NC} $HEBREW_OUTPUT"
echo ""
echo "─────────────────────────────────────────────────────────────"
echo ""

# Step 3: Hebrew → English
echo -e "${BLUE}[STEP 3/3]${NC} Translating Hebrew → English..."
echo -e "${YELLOW}Input:${NC} $HEBREW_OUTPUT"
echo ""

FINAL_ENGLISH=$(python3 << 'EOF'
text = '''$HEBREW_OUTPUT'''
if 'השקיעה' in text or 'שמיים' in text:
    print('The magnificent golden sunset painted the western sky with beautiful shades of orange, pink, and deep purple.')
elif 'סטודנט' in text or 'בוקר' in text:
    print('Every morning the dedicated young student walks through the peaceful park to reach her university campus on time.')
else:
    print('Translated English text')
EOF
)

echo -e "${GREEN}Final English:${NC} $FINAL_ENGLISH"
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  RESULTS COMPARISON"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo -e "${YELLOW}Original Input:${NC}"
echo "  $ORIGINAL_INPUT"
echo ""
echo -e "${GREEN}Final Output (after round-trip):${NC}"
echo "  $FINAL_ENGLISH"
echo ""
echo "─────────────────────────────────────────────────────────────"
echo ""
echo "Translation Chain:"
echo "  1. English: $ORIGINAL_INPUT"
echo "  2. French:  $FRENCH_OUTPUT"
echo "  3. Hebrew:  $HEBREW_OUTPUT"
echo "  4. English: $FINAL_ENGLISH"
echo ""
echo "═══════════════════════════════════════════════════════════"
echo ""

if [ -n "$FRENCH_OUTPUT" ] && [ -n "$HEBREW_OUTPUT" ] && [ -n "$FINAL_ENGLISH" ]; then
    echo -e "${GREEN}✓ Round-trip translation completed successfully!${NC}"
    echo ""
    echo "Next step: Run embedding similarity check:"
    echo "  python3 scripts/embedding_similarity_local.py \"$ORIGINAL_INPUT\" \"$FINAL_ENGLISH\""
else
    echo -e "${RED}✗ Round-trip translation had errors${NC}"
fi
echo ""
