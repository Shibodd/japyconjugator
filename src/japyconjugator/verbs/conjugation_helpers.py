from .defs import VerbClass

class WrongVerbClassException(Exception):
  def __init__(self, verb, verb_class):
    self.verb = verb
    self.verb_class = verb_class

    super().__init__(f'Wrong verb class "{verb_class}" for verb "{verb}".')

class UnsupportedVerbClassException(Exception):
  def __init__(self, verb_class):
    self.verb_class = verb_class
    super().__init__(f'Unsupported verb class "{verb_class}".')


def __ichidan_remove_ru(verb_dictform):
  # Remove る
  if verb_dictform[-1] != 'る':
    raise WrongVerbClassException(verb_dictform, VerbClass.Ichidan)
  
  return verb_dictform[:-1]


def __godan_map_last_mora(verb_dictform, mora_map: dict):
  # Transform the last mora with mora_map
  transformed = mora_map.get(verb_dictform[-1])
  if transformed is None:
    raise WrongVerbClassException(verb_dictform, VerbClass.Godan)
  
  return verb_dictform[:-1] + transformed


def __common(verb_dictform, verb_class: VerbClass, ichidan_suffix, godan_map: dict):
  if verb_class ==  VerbClass.Ichidan:
    return __ichidan_remove_ru(verb_dictform) + ichidan_suffix
  
  elif verb_class == VerbClass.Godan:
    return __godan_map_last_mora(verb_dictform, godan_map)


def masu_stem(verb_dictform, verb_class: VerbClass):
  ICHIDAN_SUFFIX = ''
  GODAN_MAP = {
    'う': 'い',
    'つ': 'ち',
    'る': 'り',
    'む': 'み',
    'ぶ': 'び',
    'ぬ': 'に',
    'く': 'き',
    'ぐ': 'ぎ',
    'す': 'し'
  }
  return __common(verb_dictform, verb_class, ICHIDAN_SUFFIX, GODAN_MAP)


def nai_stem(verb_dictform, verb_class):
  ICHIDAN_SUFFIX = ''
  GODAN_MAP = {
    'う': 'わ',
    'つ': 'た',
    'る': 'ら',
    'む': 'ま',
    'ぶ': 'ば',
    'ぬ': 'な',
    'く': 'か',
    'ぐ': 'が',
    'す': 'さ'
  }
  return __common(verb_dictform, verb_class, ICHIDAN_SUFFIX, GODAN_MAP)


def te_form(verb_dictform, verb_class):
  ICHIDAN_SUFFIX = 'て'
  GODAN_MAP = {
    'う': 'って',
    'つ': 'って',
    'る': 'って',
    'む': 'んで',
    'ぶ': 'んで',
    'ぬ': 'んで',
    'く': 'いて',
    'ぐ': 'いで',
    'す': 'して'
  }
  return __common(verb_dictform, verb_class, ICHIDAN_SUFFIX, GODAN_MAP)


def potential_form(verb_dictform, verb_class):
  ICHIDAN_SUFFIX = 'られる'
  GODAN_MAP = {
    'う': 'え',
    'つ': 'て',
    'る': 'れ',
    'む': 'め',
    'ぶ': 'べ',
    'ぬ': 'ね',
    'く': 'け',
    'ぐ': 'げ',
    'す': 'せ'
  }
  return __common(verb_dictform, verb_class, ICHIDAN_SUFFIX, GODAN_MAP) + 'る'


def volitional_form(verb_dictform, verb_class):
  ICHIDAN_SUFFIX = 'よ'
  GODAN_MAP = {
    'う': 'お',
    'つ': 'と',
    'る': 'ろ',
    'む': 'も',
    'ぶ': 'ぼ',
    'ぬ': 'の',
    'く': 'こ',
    'ぐ': 'ご',
    'す': 'そ'
  }
  return __common(verb_dictform, verb_class, ICHIDAN_SUFFIX, GODAN_MAP) + 'う'