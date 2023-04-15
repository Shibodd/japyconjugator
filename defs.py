from enum import Enum

class VerbClass(Enum):
  Ichidan = "ichidan"
  Godan = "godan"

class VerbForm(Enum):
  Plain = "plain",
  PlainPast = "plainpast",
  Polite = "polite",
  PolitePast = "politepast",
  Te = "te"

class VerbPolarity(Enum):
  Positive = "positive",
  Negative = "negative"