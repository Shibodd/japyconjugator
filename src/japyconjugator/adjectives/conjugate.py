from ..defs import Polarity

from . import conjugators
from .defs import AdjectiveForm

def conjugate(
    adj_dictform: str,
    form: AdjectiveForm,
    polarity: Polarity):
  """
  Returns the conjugated adjective.
  """

  if adj_dictform.endswith('い'):
    adj_class = conjugators.AdjectiveClass.I
  else:
    adj_class = conjugators.AdjectiveClass.Na

  CONJUGATORS = {
    AdjectiveForm.Plain: conjugators.plain,
    AdjectiveForm.PlainPast: conjugators.plainpast,
    AdjectiveForm.Polite: conjugators.polite,
    AdjectiveForm.PolitePast: conjugators.politepast,
    AdjectiveForm.Connective: conjugators.connective
  }
  return CONJUGATORS[form](adj_dictform, adj_class, polarity)