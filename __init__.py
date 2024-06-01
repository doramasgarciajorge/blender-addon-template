# -*- coding: utf-8 -*-

"""
------------------------------------------------------------
> BLENDER ADDON TEMPLATE

- AUTHOR:     Doramas García Jorge
- EMAIL:      dev.doramas@gmail.com
- GITHUB:     https://github.com/doramasgarciajorge
- REPOSITORY: https://github.com/doramasgarciajorge/blender-addon-template
------------------------------------------------------------
"""

# Blender modules
import bpy

# Blender Addon Template modules
from .user_interface import panels
from .controller import operators


bl_info = {
    "name": "Blender Addon Template",
    "author": "Doramas García Jorge",
    "version": (0, 0, 1),
    "blender": (4, 1, 1),
    "description": "Template used to start Blender addons repositories.",
    "location": "View3D > Sidebar > Blender Addon Template Tab",
    "warning": "This is an experimental under-development addon.",
    "category": "3D View"
}

classes = [
    # Panels
    panels.BLENDERADDONTEMPLATE_PT_main_panel,
    panels.BLENDERADDONTEMPLATE_PT_tools,

    # Operators
    operators.BLENDERADDONTEMPLATE_OT_create_object,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
