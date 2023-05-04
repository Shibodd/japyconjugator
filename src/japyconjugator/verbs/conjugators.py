from . import conjugation_helpers as helpers
from .defs import VerbClass

def plain_affirmative(verb_dictform: str, verb_class: VerbClass):
  return verb_dictform

def plain_negative(verb_dictform: str, verb_class: VerbClass):
  return helpers.nai_stem(verb_dictform, verb_class) + 'ない'



def plainpast_affirmative(verb_dictform: str, verb_class: VerbClass):
  te_form = helpers.te_form(verb_dictform, verb_class)
  last_mora = te_form[-1]
  
  if last_mora == 'て':
    return te_form[:-1] + 'た'
  elif last_mora == 'で':
    return te_form[:-1] + 'だ'
  else:
    assert False # impossible unless the te_form helper is broken
    
def plainpast_negative(verb_dictform: str, verb_class: VerbClass):
  return helpers.nai_stem(verb_dictform, verb_class) + 'なかった'



def polite_affirmative(verb_dictform: str, verb_class: VerbClass):
  return helpers.masu_stem(verb_dictform, verb_class) + 'ます'

def polite_negative(verb_dictform: str, verb_class: VerbClass):
  return helpers.masu_stem(verb_dictform, verb_class) + 'ません'



def politepast_affirmative(verb_dictform: str, verb_class: VerbClass):
  return helpers.masu_stem(verb_dictform, verb_class) + 'ました'

def politepast_negative(verb_dictform: str, verb_class: VerbClass):
  return helpers.masu_stem(verb_dictform, verb_class) + 'ませんでした'
  


def teform_positive(verb_dictform: str, verb_class: VerbClass):
  return helpers.te_form(verb_dictform, verb_class)

def teform_negative(verb_dictform: str, verb_class: VerbClass):
  return helpers.nai_stem(verb_dictform, verb_class) + 'なくて'
  


def potential(verb_dictform: str, verb_class: VerbClass):
  return helpers.potential_form(verb_dictform, verb_class)



def volitional(verb_dictform: str, verb_class: VerbClass):
  return helpers.volitional_form(verb_dictform, verb_class)