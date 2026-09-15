# Chess Engine Using Python

## Plan

```text
                      CHESS ENGINE
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
   1. CHESS BOARD                         2. MOVES
        │                                     │
   Represent pieces                    Generate legal moves
   Represent positions                 Handle special moves
        │                                     │
        └──────────────────┬──────────────────┘
                           │
                    3. GAME RULES
                           │
                Check / Checkmate
                Castling / Promotion
                En passant / Draws
                           │
                           ▼
                    4. POSITION
                      EVALUATION
                           │
                 "Who is better?"
                           │
                           ▼
                    5. SEARCH
                           │
                 "What should I play?"
                           │
                  Minimax / Alpha-Beta
                           │
                           ▼
                    6. ENGINE
                      STRENGTH
                           │
                  Make it play better
                  Move ordering
                  Optimization
                           │
                           ▼
                    7. INTERFACE
                           │
                 Terminal / GUI / API
                           │
                           ▼
                    8. TESTING
                       & IMPROVEMENT
```