# japyconjugator
A python package for conjugating verbs and adjectives in the Japanese language

## Installation:

pip install japyconjugator

## Usage:
```python3
from japyconjugator import verbs
verbs.plainpast_negative('飲む', verbs.VerbClass.Godan) # returns '飲まなかった'

from japyconjugator import adjectives
adjectives.connective_affirmative('暑い', adjectives.AdjectiveClass.I) # returns '暑くて'
```
