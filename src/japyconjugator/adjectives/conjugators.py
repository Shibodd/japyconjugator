from .defs import AdjectiveClass
from . import conjugation_helpers as helpers


def plain_affirmative(adj_dictform, adj_class: AdjectiveClass):
  return helpers.invariant_with_suffix(adj_dictform, adj_class,
    i_suffix = "い")

def plain_negative(adj_dictform, adj_class: AdjectiveClass):
  return helpers.negative_invariant(adj_dictform, adj_class) + "い"



def plainpast_affirmative(adj_dictform, adj_class: AdjectiveClass):
  return helpers.invariant_with_suffix(adj_dictform, adj_class,
    i_suffix = "かった",
    na_suffix="だった")

def plainpast_negative(adj_dictform, adj_class: AdjectiveClass):
  return helpers.negative_invariant(adj_dictform, adj_class) + "かった"



def polite_affirmative(adj_dictform, adj_class: AdjectiveClass):
  return plain_affirmative(adj_dictform, adj_class) + "です"

def polite_negative(adj_dictform, adj_class: AdjectiveClass):
  return plain_negative(adj_dictform, adj_class) + "です"



def politepast_affirmative(adj_dictform, adj_class: AdjectiveClass):
  return helpers.invariant_with_suffix(adj_dictform, adj_class,
    i_suffix = "かったです",
    na_suffix="でした")

def politepast_negative(adj_dictform, adj_class: AdjectiveClass):
  return helpers.negative_invariant(adj_dictform, adj_class) + "かったです"



def connective_affirmative(adj_dictform, adj_class: AdjectiveClass):
  return helpers.invariant_with_suffix(adj_dictform, adj_class,
    i_suffix = "くて",
    na_suffix = "で")

def connective_negative(adj_dictform, adj_class: AdjectiveClass):
  return helpers.negative_invariant(adj_dictform, adj_class) + "くて"