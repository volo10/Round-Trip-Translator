---
name: Natural Phrasing Preservation
description: Ensure natural, idiomatic Spanish phrasing without awkward literal translations
version: 1.0
---

# Natural Phrasing Preservation Skill

## Objective

Transform English sentences into natural, idiomatic Spanish that sounds like a native speaker wrote it, avoiding word-for-word literal translations that sound awkward.

## The Problem

English structure ≠ Spanish structure

Literal word-for-word translation produces awkward Spanish:

```
English: "I like very much going to the beach"
Literal: "Yo me gusta muy mucho ir a la playa"
Natural: "Me encanta ir a la playa"

Why: Different word order, emphasis placement, and intensity markers
```

## Core Principles

### 1. Verb Order and Subject Pronouns

**English:** Subject-Verb-Object (strict)
**Spanish:** Can be flexible, but SVO is default

#### Rule: Omit Subject Pronouns When Clear

```
English: "I eat apples"
Literal: "Yo como manzanas" ← awkward, redundant
Natural: "Como manzanas" ← clear from verb form

English: "They speak Spanish"
Literal: "Ellos hablan español" ← awkward
Natural: "Hablan español" ← clear from verb form
```

#### When to INCLUDE Pronouns

- For **contrast:** "Yo trabajo, tú descansas" (I work, you rest)
- For **emphasis:** "Yo lo hice" (I did it - me specifically)
- For **clarity:** "¿Quién habla? Yo." (Who's speaking? Me.)

### 2. Emphasis and Intensity

**English:** Uses adverbs (very, really, so, etc.)
**Spanish:** Uses different markers

#### Natural Intensity Expressions

| English | Awkward Spanish | Natural Spanish |
|---------|-----------------|-----------------|
| I really love it | Yo verdaderamente amo | Me encanta |
| I very much like | Yo muy mucho gusta | Me encanta / Me gusta mucho |
| I really hate it | Yo realmente odio | Odio / Detesto |
| I so love this | Yo tan amo esto | Me encanta esto |
| It's super nice | Es súper agradable | Es muy bonito / Está hermoso |

### 3. Reflexive Verbs for Common Actions

Many English verb + noun combinations use reflexive verbs in Spanish:

#### Common Conversions

| English | Literal (Awkward) | Natural Spanish |
|---------|-------------------|-----------------|
| Take a shower | Tomar una ducha | Ducharse |
| Take a break | Tomar un descanso | Tomarse un descanso |
| Take a walk | Dar un paseo / Tomar un paseo | Pasear / Dar un paseo |
| Go to bed | Ir a la cama | Acostarse |
| Go to sleep | Ir a dormir | Dormirse |
| Go crazy | Volverse loco | Volverse loco |
| Get tired | Obtener cansancio | Cansarse |
| Get angry | Obtener ira | Enojarse |

### 4. Preposition and Article Combinations

**English:** Separate words
**Spanish:** Can combine via prefixes or merge

#### Prefix Combinations

```
English: "in the house"
Parts: "in" + "the" + "house"
Spanish merge: "en la casa" ← stays separate
But sometimes: "from the book" = "del libro" (de + el)
```

### 5. Word Order for Naturalness

#### Adjective Placement

```
English: "The intelligent girl"
Structure: Article + Adjective + Noun
Spanish: Article + Noun + Adjective (usually)
Natural: "La chica inteligente"
```

#### Adverb Placement

```
English: "I slowly walked home"
Structure: Adverb + Verb + Object
Natural Spanish: "Caminé lentamente a casa"
or: "Lentamente caminé a casa" (for emphasis)
```

### 6. Idiomatic Expressions

Translate meaning, not words:

| English Expression | Literal (Wrong) | Idiomatic Spanish |
|-------------------|-----------------|------------------|
| "It's raining cats and dogs" | "Llueven gatos y perros" | "Llueve a cántaros" |
| "Piece of cake" | "Pedazo de pastel" | "Pan comido" |
| "Cost an arm and a leg" | "Cuesta un brazo y una pierna" | "Cuesta un ojo de la cara" |
| "Break the ice" | "Rompe el hielo" | "Romper el hielo" |
| "Once in a blue moon" | "Una vez en luna azul" | "De vez en cuando" / "Muy raramente" |

## Naturalness Checklist

✓ Sounds like a native Spanish speaker wrote it
✓ No word-for-word translation visible
✓ Proper verb conjugation and tense
✓ Appropriate subject pronouns (or omitted)
✓ Subject-verb agreement
✓ Gender and number agreement
✓ Proper preposition usage
✓ Idiomatic expressions used
✓ Emphasis placed naturally
✓ Registers/formality maintained

## Decision Tree for Natural Phrasing

```
Input: English sentence

1. Are subject pronouns needed?
   ├─ Clarity required? YES → Include (ej: Yo lo hizo)
   ├─ Contrast needed? YES → Include (ej: Yo trabajo, tú descansas)
   └─ Otherwise? NO → Omit (ej: Como pan)

2. Is there emphasis in English?
   ├─ "Very/really/so" markers? → Use Spanish intensity (me encanta, es muy...)
   ├─ Sentence stress? → Adjust word order
   └─ Question/negation? → Place naturally

3. Is it a common "verb + noun" phrase?
   ├─ Take + action? → Check reflexive version
   ├─ Go + location? → Check if reflexive
   └─ Otherwise? → Use standard verb + object

4. Does it have an idiom?
   ├─ English idiom exists? → Find Spanish equivalent
   ├─ No exact match? → Translate meaning
   └─ Very cultural? → Paraphrase with explanation

5. Are adjectives positioned?
   ├─ Color/size/shape? → After noun
   ├─ Quality/opinion? → After noun (usually)
   └─ Special emphasis? → Before noun (rare)
```

## Example Transformations

### Example 1: Emphasis and Reflexive

```
English: "I really love taking showers"
Structure breakdown:
  - Emphasis: "really love" → me encanta
  - Action: "taking showers" → duchas/ducharse

Natural Spanish: "Me encanta ducharme"
or: "Me encanta darme una ducha"

NOT: "Yo verdaderamente amo tomar duchas" ← too literal
```

### Example 2: Word Order and Pronouns

```
English: "I am working very hard on this project"
Breakdown:
  - Subject pronoun? NO (clear from conjugation)
  - Emphasis: "very hard" → muy duro / duro
  - Structure: Activity + object

Natural Spanish: "Estoy trabajando muy duro en este proyecto"
or: "Trabajo duro en este proyecto"

NOT: "Yo estoy trabajando muy mucho duro en este proyecto"
```

### Example 3: Idiomatic Expression

```
English: "This exam is going to be a piece of cake"
Expression: "piece of cake" = easy

Natural Spanish: "Este examen va a ser pan comido"
NOT: "Este examen va a ser un pedazo de pastel" ← too literal
```

### Example 4: Reflexive Verb

```
English: "I need to go to bed early"
Breakdown:
  - "go to bed" → reflexive "acostarse"
  - Negation: "need to" → "tengo que"

Natural Spanish: "Tengo que acostarme temprano"
NOT: "Necesito ir a la cama temprana" ← too literal
```

## Common Naturalness Errors

### Error 1: Direct Subject Pronoun Overuse

❌ "Yo como pan"
✓ "Como pan"

### Error 2: Wrong Verb + Noun Construction

❌ "Tomar una ducha"
✓ "Ducharse" (when appropriate)

### Error 3: Preserving English Word Order

❌ "La chica inteligente"... wait, that's correct!
❌ "Amo mucho verdaderamente" (emphasis in wrong place)
✓ "Me encanta" (natural emphasis)

### Error 4: Translating Idioms Literally

❌ "Llueven gatos y perros"
✓ "Llueve a cántaros"

### Error 5: Not Using Reflexive for State Changes

❌ "Se pone triste"... actually that works
❌ "Ir a la cama" (when "acostarse" is more natural)
✓ "Acostarse"

## Intensity and Emphasis Rules

### Expressing "Really/Very"

```
Regular: Me gusta → I like
Emphatic: Me encanta → I love/adore
Emphatic: Me gusta mucho → I like very much
Emphatic: Me gusta un montón → I like a ton
Emphatic: Me gusta muchísimo → I like a LOT
```

### Negation with Emphasis

```
Mild: No me gusta
Emphatic: No me gusta nada → I don't like it AT ALL
Emphatic: Odio → I hate
Emphatic: Detesto → I detest
```

## Integration into Translation Pipeline

### When Processing English Sentence

1. **Remove subject pronouns** (unless needed for clarity/contrast)
2. **Identify English emphasis markers** (very, really, so, etc.)
3. **Find natural Spanish equivalent** (me encanta, es muy, etc.)
4. **Check for reflexive verbs** (shower → ducharse, etc.)
5. **Place adverbs naturally** (usually after verb or before)
6. **Adjust word order** (adjectives after nouns usually)
7. **Look for idioms** (translate meaning not words)
8. **Final check** (sounds like native speaker?)

---

**This skill ensures natural, idiomatic Spanish translations that don't sound translated at all.**
