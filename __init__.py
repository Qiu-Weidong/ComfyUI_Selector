__version__ = "1.2.7"

import os
from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

cwd_path = os.path.dirname(os.path.realpath(__file__))

directory = "web"
WEB_DIRECTORY =  directory

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', "WEB_DIRECTORY"]

print(f'\033[34m[ComfyUI-Easy-Use] server: \033[0mv{__version__} \033[92mLoaded\033[0m')
print(f'\033[34m[ComfyUI-Easy-Use] web root: \033[0m{os.path.join(cwd_path, directory)} \033[92mLoaded\033[0m')
print(f'\033[34m[ComfyUI-Easy-Use] web root: \033[0m{NODE_CLASS_MAPPINGS} \033[92mLoaded\033[0m')
print(f'\033[34m[ComfyUI-Easy-Use] web root: \033[0m{NODE_DISPLAY_NAME_MAPPINGS} \033[92mLoaded\033[0m')
