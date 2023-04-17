from ..defs import Polarity
from .defs import AdjectiveClass, AdjectiveForm
from . import conjugators

def conjugate(
    adj_dictform: str,
    adj_class: AdjectiveClass,
    form: AdjectiveForm,
    polarity: Polarity):
  """
  Returns the conjugated adjective.
  """
  CONJUGATORS = {
    AdjectiveForm.Plain: conjugators.plain,
    AdjectiveForm.PlainPast: conjugators.plainpast,
    AdjectiveForm.Polite: conjugators.polite,
    AdjectiveForm.PolitePast: conjugators.politepast,
    AdjectiveForm.Connective: conjugators.connective
  }
  return CONJUGATORS[form](adj_dictform, adj_class, polarity)