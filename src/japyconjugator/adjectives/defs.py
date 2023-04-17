import enum

class AdjectiveClass(enum.Enum):
  I = "i"
  Na = "na"

class AdjectiveForm(enum.Enum):
  Plain = "plain",
  PlainPast = "plainpast",
  Polite = "polite",
  PolitePast = "politepast",
  Connective = "connective"