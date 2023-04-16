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


def masu_stem(verb_dictform, verb_class: VerbClass):
  if verb_class == VerbClass.Ichidan:
    # Remove る
    return __ichidan_remove_ru(verb_dictform)
  
  elif verb_class == VerbClass.Godan:
    # Transpose last mora to い-column
    MAP = {
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
    return __godan_map_last_mora(verb_dictform, MAP)
    
  else:
    raise UnsupportedVerbClassException(verb_class)


def nai_stem(verb_dictform, verb_class):
  if verb_class == VerbClass.Ichidan:
    # Remove る
    return __ichidan_remove_ru(verb_dictform)
  
  elif verb_class == VerbClass.Godan:
    # Transpose last mora to あ-column (except う goes to わ)
    MAP = {
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
    return __godan_map_last_mora(verb_dictform, MAP)
    
  else:
    raise UnsupportedVerbClassException(verb_class)


def te_form(verb_dictform, verb_class):
  if verb_class == VerbClass.Ichidan:
    # Remove る
    return __ichidan_remove_ru(verb_dictform) + 'て'
  
  elif verb_class == VerbClass.Godan:
    # Apply godan Te-form rules
    MAP = {
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
    return __godan_map_last_mora(verb_dictform, MAP)
    
  else:
    raise UnsupportedVerbClassException(verb_class)