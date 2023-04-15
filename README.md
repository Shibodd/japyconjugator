# japyconjugator
A python package for conjugating verbs in the Japanese language

Usage:
```python3
import jp_verb_conjugator as conj
conj.conjugate("飲む", conj.VerbClass.Godan, conj.VerbForm.PlainPast, conj.VerbPolarity.Negative) # returns "飲まなかった"
```
