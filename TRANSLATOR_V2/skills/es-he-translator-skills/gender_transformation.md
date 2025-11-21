---
name: Gender Transformation
description: Transform Spanish nouns to correct Hebrew gender independently
version: 1.0
---

# Gender Transformation Skill (Spanish → Hebrew)

## Critical Rule

**NEVER assume Hebrew gender from Spanish gender.**

Spanish gender ≠ Hebrew gender. Both language genders are arbitrary and don't correlate.

## The Problem

```
Spanish: la mesa (feminine)
Hebrew should be: השולחן (masculine - table is masculine in Hebrew)

Spanish: el día (masculine)
Hebrew should be: היום (masculine - day happens to match)

Spanish: la casa (feminine)
Hebrew should be: הבית (masculine - house is masculine in Hebrew)
```

## Decision Process

### Step 1: Identify Spanish Noun
```
"La casa es grande"
↓
Noun: casa (house)
Spanish gender: feminine (la)
```

### Step 2: Look Up Hebrew Noun
```
Hebrew for "house": בית (bayit)
Hebrew gender: MASCULINE
```

### Step 3: Determine Agreement Chain
```
Article: ה- (the)
Noun: בית (house) - masculine
Adjectives: must agree (masculine)
Verb: if applicable, must agree
```

### Step 4: Apply Correct Gender Throughout

```
Spanish: "La casa grande está aquí"
✓ Hebrew: "הבית הגדול נמצא כאן"
         ↑ masculine  ↑ masculine  ↑ masculine

✗ NOT: "הבית הגדולה נמצאת כאן" (mixing genders)
```

## Hebrew Gender Patterns

### Feminine Nouns

Typically end in: -ה, -ית, -ת

```
אישה (isha) - woman - feminine
שחקנית (shakhanit) - actress - feminine
מכונית (mekhonit) - car - feminine
```

### Masculine Nouns

Most other patterns

```
ספר (sefer) - book - masculine
בית (bayit) - house - masculine
כלב (kelev) - dog - masculine
```

## Common Mismatches

| Spanish | Gender | Hebrew | Gender | Note |
|---------|--------|--------|--------|------|
| la mano | fem | יד (yad) | fem | Match |
| el día | masc | יום (yom) | masc | Match |
| la casa | fem | בית (bayit) | masc | MISMATCH |
| el problema | masc | בעיה (be'aya) | fem | MISMATCH |
| la película | fem | סרט (seret) | masc | MISMATCH |
| el tiempo | masc | זמן (zman) | masc | Match |

## Agreement Rules After Gender Determination

### Definite Articles

Feminine singular: ה- (standard)
Masculine singular: ה- (standard)

### Adjectives Must Agree

```
Hebrew masculine adjective: גדול (gadol) - big
Hebrew feminine adjective: גדולה (gdola) - big

"The big house" (masculine):
הבית הגדול (ha-bayit ha-gadol)

"The big car" (feminine):
המכונית הגדולה (ha-mekhonit ha-gdola)
```

### Verbs Must Agree with Subject Gender

```
"The house is big" (masculine subject):
הבית הוא גדול (ha-bayit hu gadol)

"The car is big" (feminine subject):
המכונית היא גדולה (ha-mekhonit hi gdola)
```

## Application in Translation

### Example 1

```
Spanish input: "La ventana es hermosa"
1. Spanish: ventana (window) - feminine
2. Look up Hebrew: חלון (chalon) - MASCULINE
3. Gender: masculine
4. Hebrew output: "החלון הוא יפה"
   (ha-chalon hu yafe - masculine throughout)
```

### Example 2

```
Spanish input: "El libro rojo está aquí"
1. Spanish: libro (book) - masculine
2. Look up Hebrew: ספר (sefer) - MASCULINE
3. Gender: masculine
4. Hebrew output: "הספר האדום נמצא כאן"
   (ha-sefer ha-adom nimtza kan - masculine)
```

## Quality Checklist

✓ Determined Spanish noun correctly
✓ Looked up Hebrew noun independently
✓ Identified Hebrew gender correctly
✓ Applied gender to ALL related words
✓ Adjectives agree with noun gender
✓ Articles match gender
✓ Verbs agree with subject gender
✓ No gender carried over from Spanish

---

**Always verify Hebrew gender from Hebrew sources, never from Spanish grammar.**
