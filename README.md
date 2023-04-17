# japyconjugator
A python package for conjugating verbs and adjectives in the Japanese language

Usage:
```python3
import japyconjugator.verbs as verbs
verbs.conjugate('飲む', verbs.VerbClass.Godan, verbs.VerbForm.PlainPast, verbs.Polarity.Negative) # returns "飲まなかった"

import japyconjugator.adjectives as adj
adj.conjugate('元気', adj.AdjectiveForm.PolitePast, adj.Polarity.Negative) # returns '元気じゃなかったです'
```
