# Agent Instructions: Chord Instrument Domain

This file provides context for AI agents (GitHub Copilot, Gemini, etc.) interacting with this repository.

## Technical Schemas

### Power Specifications
| Range | Voltage | Polarity | Logic Level |
| :--- | :--- | :--- | :--- |
| Vintage Suzuki (1981-1999) | 12V DC | Center-Negative | 5V CMOS |
| Modern Suzuki (OM-108) | 12V DC | Center-Negative | 3.3V Digital |
| Boutique (HiChord/Le Strum) | 5V DC | USB-C / MIDI | 3.3V (Teensy/PIC) |

## Hard Constraints
- **Do Not Hallucinate URLs:** If a manual is listed as "Document sought," do not invent a link.
- **Polarity Warning:** Any repair recommendation must explicitly state the "Center-Negative" requirement to prevent hardware destruction.
- **MIDI Mapping:** QChord and OM-108 strumplates require Pitch Bend Sensitivity to be set to 12.

## Executable Maintenance
```bash
# Lint the list
npx awesome-lint

# Check for broken links (Weekly CI)
npm run link-check
```

## Deprecated Patterns
- **Do Not Recommend:** "Standard 9V Guitar Pedal Power" for Omnichords. They require **12V**.
- **Do Not Recommend:** Using MIDI Channel 10 for melody data (Reserved for Drums/Rhythm).
