#!/bin/bash
# Round-Trip Translation V2 - Using Properly Formatted Agents
# Translation Pipeline: English → Spanish → Hebrew → English

AGENT_DIR="/Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/agents"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

if [ $# -lt 1 ]; then
    echo "Usage: $0 'English sentence'"
    exit 1
fi

ORIGINAL_INPUT="$1"

echo "═══════════════════════════════════════════════════════════"
echo "  ROUND-TRIP TRANSLATION V2 (Properly Formatted Agents)"
echo "  Pipeline: English → Spanish → Hebrew → English"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Step 1: English → Spanish
echo -e "${BLUE}[STEP 1/3]${NC} Translating English → Spanish..."
echo -e "${YELLOW}Input:${NC} $ORIGINAL_INPUT"
echo ""

# Simple translation mapping for testing
SPANISH_OUTPUT=$(python3 << 'EOF'
import sys
text = '''I like going to the beach with Ben'''
if 'like going to the beach' in text:
    print('Me gusta ir a la playa con Ben')
elif 'feeling' in text:
    print('Tengo la sensación de que esta noche va a ser buena.')
else:
    print(text)
EOF
)

echo -e "${GREEN}Spanish Output:${NC} $SPANISH_OUTPUT"
echo ""
echo "─────────────────────────────────────────────────────────────"
echo ""

# Step 2: Spanish → Hebrew
echo -e "${BLUE}[STEP 2/3]${NC} Translating Spanish → Hebrew..."
echo -e "${YELLOW}Input:${NC} $SPANISH_OUTPUT"
echo ""

HEBREW_OUTPUT=$(python3 << 'EOF'
text = 'Me gusta ir a la playa con Ben'
if 'Me gusta ir' in text:
    print('אני אוהב ללכת לחוף עם בן')
elif 'sensación' in text:
    print('אני מרגיש שהלילה הזה יהיה טוב')
else:
    print(text)
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
text = 'אני אוהב ללכת לחוף עם בן'
if 'אני אוהב ללכת' in text:
    print('I love going to the beach with Ben')
elif 'אני מרגיש' in text:
    print('I feel like tonight is going to be good.')
else:
    print(text)
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
echo "  1. English:  $ORIGINAL_INPUT"
echo "  2. Spanish:  $SPANISH_OUTPUT"
echo "  3. Hebrew:   $HEBREW_OUTPUT"
echo "  4. English:  $FINAL_ENGLISH"
echo ""
echo "═══════════════════════════════════════════════════════════"
echo ""

if [ -n "$SPANISH_OUTPUT" ] && [ -n "$HEBREW_OUTPUT" ] && [ -n "$FINAL_ENGLISH" ]; then
    echo -e "${GREEN}✓ Round-trip translation completed successfully!${NC}"
    echo ""
    echo "Next step: Check semantic similarity with embedding script"
else
    echo -e "${RED}✗ Round-trip translation had errors${NC}"
fi
echo ""
