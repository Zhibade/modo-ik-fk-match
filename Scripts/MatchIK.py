#python
# Match IK to FK joints
# Customize the item names and keywords in the constants section to match your rig
# Author: Jose Lopez Romo - Zhibade

import modo, utils

# Item names

# Rotation will be matched from SOURCE to TARGET
SOURCE_ITEM_MAPPING = ["IK_PoleVector_Match", "FK_Wrist_CTRL"]
TARGET_ITEM_MAPPING = ["IK_Elbow_CTRL", "IK_Wrist_CTRL"]
# Which items should be translated and/or rotated
ITEM_TRANSLATION_MAPPING = [True, True]
ITEM_ROTATION_MAPPING = [False, True]

IK_CTRL_ITEMS = ["IK_Elbow_CTRL", "IK_Wrist_CTRL"] # These will be shown
FK_CTRL_ITEMS = ["FK_Shoulder_CTRL", "FK_Elbow_CTRL", "FK_Wrist_CTRL"] # These will be hidden

# Constants

CONTRAINT_KEYWORD = "Bind"
FK_CHANNEL_KEYWORD = "FK"
IK_CHANNEL_KEYWORD = "IK"

CONSTRAINT_ACTIVE = 1.0
CONSTRAINT_INACTIVE = 0.0

VISIBILITY_SHOW = 0
VISIBILITY_HIDE = 2
VISIBILITY_CHANNEL = "visible"

CONSTRAINT_TYPE = "cmTransformConstraint"

# Initialization

scene = modo.Scene()

# Hide FK and show IK

for ik_ctrl in IK_CTRL_ITEMS:
  ctrl = utils.get_item(ik_ctrl)
  ctrl.channel(VISIBILITY_CHANNEL).set(VISIBILITY_SHOW)

for fk_ctrl in FK_CTRL_ITEMS:
  ctrl = utils.get_item(fk_ctrl)
  ctrl.channel(VISIBILITY_CHANNEL).set(VISIBILITY_HIDE)

# Match IK controls

mapping = zip(SOURCE_ITEM_MAPPING, TARGET_ITEM_MAPPING, ITEM_TRANSLATION_MAPPING, ITEM_ROTATION_MAPPING)

for source, target, translate, rotate in mapping:
  if translate:
    utils.match_translation(source, target)
  if rotate:
    utils.match_rotation(source, target)

# Set constraint weights to IK

constraints = scene.items(CONSTRAINT_TYPE)

for constraint in constraints:
  if CONTRAINT_KEYWORD in constraint.name:
    fk_channels = constraint.channels("*" + FK_CHANNEL_KEYWORD + "*")
    ik_channels = constraint.channels("*" + IK_CHANNEL_KEYWORD + "*")

    for fk_chan in fk_channels:
      fk_chan.set(CONSTRAINT_INACTIVE)

    for ik_chan in ik_channels:
      ik_chan.set(CONSTRAINT_ACTIVE)
