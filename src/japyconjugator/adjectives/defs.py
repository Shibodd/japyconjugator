import enum

class AdjectiveClass(enum.StrEnum):
  I = "i"
  Na = "na"

class AdjectiveForm(enum.StrEnum):
  Plain = "plain",
  PlainPast = "plainpast",
  Polite = "polite",
  PolitePast = "politepast",
  Connective = "connective"