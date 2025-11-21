---
name: Word Order Conversion
description: Convert Hebrew VSO word order to natural English SVO
version: 1.0
---

# Word Order Conversion Skill (Hebrew → English)

## The Problem

**Hebrew natural word order:** VSO (Verb-Subject-Object)
**English required order:** SVO (Subject-Verb-Object)

```
Hebrew VSO: "הלך הילד לבית"
Literal: "(Went) (the-boy) (to-house)"
↓
English SVO: "The boy went home"
NOT: "Went the boy to house"
```

## Hebrew VSO Pattern

### Typical Hebrew Sentence Structure

```
[Verb] [Subject] [Object] [Modifiers]

Example: "קרא דוד את הספר בספריה אתמול"
Breaking down:
- קרא = Read (verb)
- דוד = David (subject)
- את הספר = the book (object)
- בספריה = in the library (modifier)
- אתמול = yesterday (modifier)

Literal order: (Verb-Subject-Object-Modifiers)
```

## Conversion Process

### Step 1: Identify Components

```
Hebrew: "הלך הילד לבית"
↓
Identify:
- Verb: הלך (went)
- Subject: הילד (the boy)
- Object/Complement: לבית (to house)
```

### Step 2: Reorder to SVO

```
Components:
- S: הילד (the boy)
- V: הלך (went)
- O: לבית (to house)

Reorder: S-V-O
Result: "The boy went to house"
```

### Step 3: Make Natural English

```
"The boy went to house"
↓
More natural: "The boy went home"
(substitute "בית" = house with "home" for more natural English)
```

## Common Hebrew to English Conversions

### Narrative VSO
```
Hebrew: "עשה משהו גדול"
Literal: "(Did) (he) (something big)"
English SVO: "He did something big"
Natural: "He did something big"
```

### Past Tense VSO
```
Hebrew: "אכלה היא את הפאי"
Literal: "(Ate) (she) (the pie)"
English: "She ate the pie"
```

### Future VSO
```
Hebrew: "יבוא הרכבת בעוד דקה"
Literal: "(Will come) (the train) (in another minute)"
English: "The train will come in another minute"
```

## Modifiers and Adjectives

### Adjective Placement

Hebrew: Adjectives usually follow nouns
English: Adjectives usually precede nouns

```
Hebrew: "הילד הטוב"
Literal: "(The boy) (the good)"
English: "The good boy" ← adjective comes first
Hebrew structure: noun + adjective
English structure: adjective + noun
```

### Adverb Placement

Hebrew can place adverbs at beginning, English usually puts them after verb

```
Hebrew: "לאט הוא הלך"
Literal: "(Slowly) (he) (walked)"
English: "He walked slowly" ← adverb after verb
```

## Verb Tense Preservation

Hebrew tense markers must be preserved through word order change

```
Hebrew: "קרא הילד" (past)
English: "The boy read" (past preserved)
NOT: "The boy reads" ← wrong tense

Hebrew: "יקרא הילד" (future)
English: "The boy will read" (future preserved)
NOT: "The boy reads"
```

## Complex Sentences

### Multiple Clauses

Hebrew: Often uses VSO in each clause
English: Uses SVO in each clause

```
Hebrew: "ראה הילד את הכלב והילד רץ"
Parts:
1. "ראה הילד את הכלב" = (Saw) (the-boy) (the-dog)
2. "והילד רץ" = (and-the-boy) (ran)

English: "The boy saw the dog and the boy ran"
or more naturally: "The boy saw the dog and ran"
```

### Relative Clauses

```
Hebrew: "הספר שקרא הילד"
Breaking: "(The-book) (that-read) (the-boy)"

English: "The book that the boy read"
(subject "the boy" moved before verb in relative clause)
```

## Decision Flowchart

```
Hebrew sentence structure:

1. Identify main verb ← Find action word
2. Identify subject ← Find doer
3. Identify object/complement ← Find affected thing
4. Note tense markers ← Preserve tense
5. Reorder to S-V-O ← English structure
6. Place adjectives before nouns ← English style
7. Place adverbs appropriately ← After verb usually
8. Make natural English ← Adjust phrasing
```

## Quality Checklist

✓ Identified all sentence components (V, S, O)
✓ Reordered to SVO (not VSO in English)
✓ Preserved verb tense
✓ Adjusted adjective order (before nouns)
✓ Placed adverbs naturally
✓ Subject-verb agreement maintained
✓ Sounds like natural English
✓ No VSO structure remains

## Common Errors to Avoid

### Error 1: Keeping Hebrew VSO

❌ "Walked the boy home"
✓ "The boy walked home"

### Error 2: Wrong Tense
❌ "The boy reads home" (present instead of past)
✓ "The boy went home" (past preserved)

### Error 3: Adjective in Wrong Place
❌ "The intelligent girl" ← Hebrew: אישה חכמה
Actually this is correct for English!
Hebrew would be: "האישה החכמה"

### Error 4: Adverb in Wrong Place
❌ "Slowly walked the boy"
✓ "The boy walked slowly"

---

**Always convert Hebrew VSO to English SVO for natural, grammatical English.**
