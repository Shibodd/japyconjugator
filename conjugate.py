from .defs import VerbClass, VerbPolarity, VerbForm
from . import conjugators as conjugators

def conjugate(
    verb_dictform: str,
    verb_class: VerbClass,
    form: VerbForm,
    polarity: VerbPolarity):
  """
  Calls the appropriate conjugator in jp_verb_conjugator.conjugators, and returns the conjugated verb.
  """
  CONJUGATORS = {
    VerbForm.Te: conjugators.teform,
    VerbForm.Plain: conjugators.plain,
    VerbForm.PlainPast: conjugators.plainpast,
    VerbForm.Polite: conjugators.polite,
    VerbForm.PolitePast: conjugators.politepast
  }
  return CONJUGATORS[form](verb_dictform, verb_class, polarity)