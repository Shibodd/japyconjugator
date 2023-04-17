from ..defs import Polarity
from .defs import AdjectiveClass

def invariant_with_suffix(adj_dictform, adj_class: AdjectiveClass, na_suffix = '', i_suffix = ''):
  if adj_class == AdjectiveClass.I:
    return adj_dictform[:-1] + i_suffix
  else:
    return adj_dictform + na_suffix

def negative_invariant(adj_dictform, adj_class: AdjectiveClass):
  return invariant_with_suffix(adj_dictform, adj_class, 
    i_suffix = 'くな',
    na_suffix = 'じゃな')

def common_logic(adj_dictform, adj_class: AdjectiveClass, polarity: Polarity,
    affirmative_i_suffix = '',
    affirmative_na_suffix = '',
    negative_suffix = ''):
  
  if polarity == Polarity.Affirmative:
    return invariant_with_suffix(adj_dictform, adj_class,
      i_suffix = affirmative_i_suffix,
      na_suffix = affirmative_na_suffix)
  else:
    return negative_invariant(adj_dictform, adj_class) + negative_suffix