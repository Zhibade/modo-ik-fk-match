# MODO Tool - IK/FK Match
## Overview
MODO scripts that allow you to match FK to IK and vice versa.

The script will match the controls to the corresponding target and hide/show
the appropriate controls. It will also automatically adjust the constraints
to use the corresponding mode (FK or IK).

**NOTE:** It only works with the standard 3 joint chain setup (one for FK, one for IK and one for binding to the mesh)
It won't work with the default MODO IK/FK blending.

**NOTE:** This is intended mostly as a template for more specific or advanced IK/FK matching, not as a catch-all solution.
You will need to adjust the scripts to suit your needs (more info on the *How to Install* section)

## How to Install
- Clone/Download this repository
- Copy the whole folder to your *Contents/Kits* folder (In MODO go to *System - Open Content Folder*)
- Open the *MatchFK.py* and *MatchIK.py* scripts and adjust the item names under *Item Names* comment (line 8) to match your rig
- Adjust the constraint and channel keyword constants as well (line 20) so that the script can find the proper constraints and
their channels
- Restart MODO

## How to Use
- *IK* and *FK* buttons will appear on the *Animate* layout, below the local/world coordinates buttons
- Clicking on those buttons will enable the corresponding controls and match them to the current position
- If you wish to move these buttons, you can do so by using the *Form Editor* and moving the
button controls under the *zbIkFkMatch* group, and removing them from the *Animate Coords* tail category

Please refer to the included sample scene to see how it was set up and how the naming and keywords match the scripts
