from . import conjugation_helpers as helpers
from .defs import VerbClass, VerbPolarity


def plain(verb_dictform: str, verb_class: VerbClass, polarity: VerbPolarity):
  if polarity == VerbPolarity.Positive:
    return verb_dictform
  else:
    return helpers.nai_stem(verb_dictform, verb_class) + 'ない'


def plainpast(verb_dictform: str, verb_class: VerbClass, polarity: VerbPolarity):
  if polarity == VerbPolarity.Positive:
    te_form = helpers.te_form(verb_dictform, verb_class)
    last_mora = te_form[-1]
    
    if last_mora == 'て':
      return te_form[:-1] + 'た'
    elif last_mora == 'で':
      return te_form[:-1] + 'だ'
    else:
      assert False # impossible unless base_conjugators.te_form is broken
    
  else:
    return helpers.nai_stem(verb_dictform, verb_class) + 'なかった'


def polite(verb_dictform: str, verb_class: VerbClass, polarity: VerbPolarity):
  stem = helpers.masu_stem(verb_dictform, verb_class)
  
  if polarity == VerbPolarity.Positive:
    return stem + 'ます'
  else:
    return stem + 'ません'


def politepast(verb_dictform: str, verb_class: VerbClass, polarity: VerbPolarity):
  stem = helpers.masu_stem(verb_dictform, verb_class)

  if polarity == VerbPolarity.Positive:
    return stem + 'ました'
  else:
    return stem + 'ませんでした'
  

def teform(verb_dictform: str, verb_class: VerbClass, polarity: VerbPolarity):
  if polarity == VerbPolarity.Positive:
    return helpers.te_form(verb_dictform, verb_class)
  else:
    return helpers.nai_stem(verb_dictform, verb_class) + 'なくて'
