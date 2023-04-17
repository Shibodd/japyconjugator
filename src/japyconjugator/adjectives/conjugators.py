from ..defs import Polarity
from .defs import AdjectiveClass
from .conjugation_helpers import common_logic


def plain(adj_dictform, adj_class: AdjectiveClass, polarity: Polarity):
  return common_logic(adj_dictform, adj_class, polarity, 
    affirmative_i_suffix=adj_dictform[-1], # restore last mora
    negative_suffix="い")


def plainpast(adj_dictform, adj_class: AdjectiveClass, polarity: Polarity):
  return common_logic(adj_dictform, adj_class, polarity, 
    affirmative_i_suffix="かった",
    affirmative_na_suffix="だった",
    negative_suffix="かった")


def polite(adj_dictform, adj_class: AdjectiveClass, polarity: Polarity):
  return plain(adj_dictform, adj_class, polarity) + "です"


def politepast(adj_dictform, adj_class: AdjectiveClass, polarity: Polarity):
  return common_logic(adj_dictform, adj_class, polarity, 
    affirmative_i_suffix="かったです",
    affirmative_na_suffix="でした",
    negative_suffix="かったです")


def connective(adj_dictform, adj_class: AdjectiveClass, polarity: Polarity):
  return common_logic(adj_dictform, adj_class, polarity, 
    affirmative_i_suffix="くて",
    affirmative_na_suffix="で",
    negative_suffix="くて")
