#python
# Match FK to IK joints
# Customize the item names and keywords in the constants section to match your rig
# Author: Jose Lopez Romo - Zhibade

import modo, utils

# Item names

# Rotation will be matched from SOURCE to TARGET
# NOTE: These have to be ordered by hierarchy (top to bottom) e.g. Shoulder, Elbow, Wrist
SOURCE_ITEM_MAPPING = ["Shoulder_IK_JNT", "Elbow_IK_JNT", "Wrist_IK_JNT"]
TARGET_ITEM_MAPPING = ["FK_Shoulder_CTRL", "FK_Elbow_CTRL", "FK_Wrist_CTRL"]

IK_CTRL_ITEMS = ["IK_Elbow_CTRL", "IK_Wrist_CTRL"] # These will be hidden
FK_CTRL_ITEMS = ["FK_Shoulder_CTRL", "FK_Elbow_CTRL", "FK_Wrist_CTRL"] # These will be shown

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

# Hide IK and show FK

for ik_ctrl in IK_CTRL_ITEMS:
  ctrl = utils.get_item(ik_ctrl)
  ctrl.channel(VISIBILITY_CHANNEL).set(VISIBILITY_HIDE)

for fk_ctrl in FK_CTRL_ITEMS:
  ctrl = utils.get_item(fk_ctrl)
  ctrl.channel(VISIBILITY_CHANNEL).set(VISIBILITY_SHOW)

# Match FK controls

for source, target in zip(SOURCE_ITEM_MAPPING, TARGET_ITEM_MAPPING):
  utils.match_rotation(source, target)

# Set constraint weights to FK

constraints = scene.items(CONSTRAINT_TYPE)

for constraint in constraints:
  if CONTRAINT_KEYWORD in constraint.name:
    fk_channels = constraint.channels("*" + FK_CHANNEL_KEYWORD + "*")
    ik_channels = constraint.channels("*" + IK_CHANNEL_KEYWORD + "*")

    for fk_chan in fk_channels:
      fk_chan.set(CONSTRAINT_ACTIVE)

    for ik_chan in ik_channels:
      ik_chan.set(CONSTRAINT_INACTIVE)
