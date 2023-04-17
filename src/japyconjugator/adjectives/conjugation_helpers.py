from ..defs import Polarity
from .defs import AdjectiveClass

def negative_invariant(adj_dictform, adj_class: AdjectiveClass):
  if adj_class == AdjectiveClass.I:
    return adj_dictform[:-1] + "くな"
  else:
    return adj_dictform + "じゃな"
  

def append_suffix_to_invariant(adj_dictform, adj_class: AdjectiveClass, polarity: Polarity,
    affirmative_i_suffix = "",
    affirmative_na_suffix = "",
    negative_suffix = ""):
  
  if polarity == Polarity.Affirmative:
    invariant = adj_dictform[:-1]

    if adj_class == AdjectiveClass.I:
      return invariant + affirmative_i_suffix
    else:
      return invariant + affirmative_na_suffix
    
  else:
    return negative_invariant(adj_dictform, adj_class) + negative_suffix