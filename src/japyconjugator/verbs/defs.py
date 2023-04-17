import enum

class VerbClass(enum.StrEnum):
  Ichidan = "ichidan"
  Godan = "godan"

class VerbForm(enum.StrEnum):
  Plain = "plain",
  PlainPast = "plainpast",
  Polite = "polite",
  PolitePast = "politepast",
  Te = "te"