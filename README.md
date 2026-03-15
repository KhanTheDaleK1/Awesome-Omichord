# Awesome Chord Instruments 🎹✨

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Stability: Stable](https://img.shields.io/badge/stability-stable-green.svg)
![AI-Ready: Optimized](https://img.shields.io/badge/AI--Ready-Optimized-blue.svg)

A high-signal, machine-readable knowledge base for chord-driven electronic and acoustic instruments. This repository follows the **Diátaxis Framework** to provide intent-based navigation for humans and AI agents.

---

## 🏛️ History of Chord Instruments: From Sumer to Synthesis
*Understanding the evolution of simultaneous harmony.*

### I. Ancient Origins (3500 BCE - 500 BCE)
- **The Sumerian Harp:** The earliest known chordophone. Unlike melodic flutes, the harp allowed for intentional multi-note harmony.
- **The Greek Lyre:** A precursor to the lute, used to provide a harmonic "backdrop" for spoken poetry.

### II. Medieval & Renaissance (500 CE - 1600 CE)
- **The Lute:** The "Piano of the Middle Ages." Its polyphonic capability allowed for complex independent melodic lines.
- **The Hurdy-Gurdy:** Introduced the concept of the **Drone**—a constant harmonic foundation maintained by a cranked wheel.

### III. The Mechanical Revolution (1600 CE - 1900 CE)
- **The Harpsichord:** Strings are plucked by quills via a keyboard. It provided the *basso continuo* (harmonic glue) for the Baroque era.
- **The Piano-Forte:** Invented by Cristofori (c. 1700). Introduced **dynamics** (soft/loud) and became the ultimate compositional map for Western harmony.

### IV. The Electronic Age (1930 CE - Present)
- **Electric Guitar:** Allowed chords to sustain and pierce through orchestral textures.
- **Polyphonic Synthesizers:** (e.g., Prophet-5, 1978). Chords generated via pure electricity and voltage-controlled oscillators.
- **The Strumplate Era:** Suzuki's Omnichord (1981) introduced a tactile, "infinite sustain" method for triggering chords via a touch-sensitive plate.

---

## 📘 Tutorials (Learning-Oriented)
*New to chord instruments? Start here.*

- [Omnichord 101: The Strumming Technique](http://www.omnichord-heaven.com/howtoplay.htm) - ![stable](https://img.shields.io/badge/status-stable-green)
  Learn the foundational "hold-and-swipe" interaction model. #Basics #Technique
- [QChord EZ-Play Guide](https://www.manualslib.com/manual/167043/Suzuki-Qc-1.html) - ![stable](https://img.shields.io/badge/status-stable-green)
  Introductory guide to using digital cartridges and "One-Finger" accompaniment. #EZ-Play #Beginner

---

## 🛠️ How-To Guides (Goal-Oriented)
*Solve specific problems or implement features.*

- [MIDI-fying a Vintage OM-27](https://github.com/hotchk155/Voici-Le-Strum) - ![experimental](https://img.shields.io/badge/status-experimental-orange)
  Step-by-step on using Le Strum or Teensy clones to add MIDI to analog gear. #MIDI #DIY #Modding
- [Correcting Power Polarity for Suzuki Hardware](http://www.omnichord-heaven.com/reference/repairs.htm) - ![critical](https://img.shields.io/badge/status-critical-red)
  How to replace the 2.2-ohm protection resistor after a polarity mismatch. #Repair #Hardware
- [Mapping QChord Pitch Bend to VSTs](https://bome.com/support/kb/qchord-midi-setup) - ![stable](https://img.shields.io/badge/status-stable-green)
  Technical walkthrough on setting +/- 12 semitone ranges for DAW integration. #DAW #Mapping

---

## 📑 Reference (Information-Oriented)
*Technical specs, schematics, and data sheets.*

### Suzuki Flagship Models
- **Suzuki OM-108 (2024)** - ![maintained](https://img.shields.io/badge/status-maintained-blue)
  Current flagship. 108 chords, 5-pin MIDI OUT, PCM engine. #Flagship #PCM
  - [Official PDF Manual](https://www.suzuki-music.co.jp/manual/om-108_en)
- **Suzuki OM-27 (1981)** - ![legacy](https://img.shields.io/badge/status-legacy-yellow)
  The analog original. Based on `AY-5-1317A`. #Analog #Vintage
  - [Service Manual & Schematics](http://www.omnichord-heaven.com/reference/manuals.php)

### Modern Boutique Instruments
- **HiChord (Pocket Audio)** - ![maintained](https://img.shields.io/badge/status-maintained-blue)
  Teensy-based handheld poly-synth with tactile strumming. #Boutique #Teensy
  - [HiChord User Guide v2.0](https://pocketaudio.co/pages/hichord-manual)
- **Le Strum (64pixels)** - ![open-source](https://img.shields.io/badge/status-open--source-brightgreen)
  Open-hardware MIDI chord controller. #DIY #MIDI
  - [GitHub: Voici-Le-Strum](https://github.com/hotchk155/Voici-Le-Strum)

### Vintage "Autochords"
- **Hammond Piper Autochord (1970)** - ![legacy](https://img.shields.io/badge/status-legacy-yellow)
  The first "easy-play" electronic organ with automatic harmony. #History #Organ
  - [Service Manual Mirror](https://archive.org/details/hammond-piper-service-manual)

---

## 🧠 Explanation (Understanding-Oriented)
*Architecture, concepts, and background.*

- **The C-Note Strumming Quirk:** An architectural deep-dive into why chord instruments use Note 60 + Pitch Bend instead of multi-channel Note-On messages. #Architecture #MIDI
- **AY-Series vs. PCM:** Understanding the transition from the analog logic of the OM-84 to the sample-triggered voices of the OM-300. #Synthesisi #History

---

## 🤖 AI Context (agents.md)
*For LLMs and coding agents.*

- **Hardware Boundary:** All vintage Suzuki hardware (OM-27 to OM-300) is **CENTER-NEGATIVE**. Never recommend a Center-Positive 12V adapter.
- **Linter:** Use `npx awesome-lint` to validate this repository.
- **Stack:** Markdown, Mermaid.js (for schematics), Docusaurus 3.x.
