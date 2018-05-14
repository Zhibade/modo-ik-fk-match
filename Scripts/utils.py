#python
# Generic MODO TD-SDK utils
# Author: Jose Lopez Romo - Zhibade

import modo

# Constants

WORLD_ROT_MATRIX_CHANNEL = "wrotMatrix"

# API

def get_item(name):
  """
  Gets an item in the MODO scene using the exact name.

  Displays a warning dialog if not found

  Params:
    name :: string - Item's name
  """

  item = None

  try:
    item = modo.Scene().item(name)
    return item
  except:
    show_warning("No item found with the name: " + name)


def match_rotation(source, target):
  """
  Matches the rotation from source to target

  Params:
    source :: MODO item - Source item
    target :: MODO item - Target item
  """

  source_item = get_item(source)
  target_item = get_item(target)

  # Reset TARGET rotation to get Rotation Zero values, and then 
  # negate the rotation from the SOURCE world rotation matrix
  target_item.rotation.set((0,0,0))

  target_zero_rot = modo.Matrix4(target_item.channel(WORLD_ROT_MATRIX_CHANNEL).get())
  source_rot = modo.Matrix4(source_item.channel(WORLD_ROT_MATRIX_CHANNEL).get())

  final_rot = source_rot * target_zero_rot.inverted()

  target_item.rotation.set(final_rot.asEuler(True), None, False, 'edit', True)


def show_warning(msg):
  """
  Displays a warning dialog with the given message

  Params:
    msg :: string - Dialog message
  """
  lx.eval("dialog.setup warning")
  lx.eval("dialog.title Warning")
  lx.eval("dialog.msg {0}".format("{" + msg + "}"))
  lx.eval('dialog.result ok')
  lx.eval('dialog.open')