SCRABBLE2 GAME ENGINE

My first ever University Project.
This repository contains the logic and main engine for a terminal-based Scrabble clone, defined within the file FP2526_P2.py. The script handles everything from board generation and vocabulary filtering to turn-based gameplay and algorithmic bot logic.

FEATURES:
- 2 to 4 player modes
- 3 tiers of AI Opponents: "FACIL", "MEDIO" and "DIFICIL"
- Portuguese Alphabet Intergration (custom portuguese letters, not available in English language)

GAME MECHANICS:
- J (jogar) : use syntax "J ^line^ ^column^ ^direction^ ^word^" (eg: J 3 8 H TESTE)
- T (trocar) : use "T" followed by the letters to exchange. The bag is required to have at least 7 letters remaining (eg: T A B C)
- P (passar) : Pass your current turn

NOTE:
This engine runs specifically on "vocab25.txt" (approx: 25000 words, in PORTUGUESE ONLY!!). For other languages/larger vocabularies, specify directly in scrabble2() on game function.
