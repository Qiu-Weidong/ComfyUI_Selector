

import folder_paths

class AlwaysEqualProxy(str):
  def __eq__(self, _):
    return True

  def __ne__(self, _):
    return False
    

class LoraSelector:
  def __init__(self):
    pass

  @classmethod
  def INPUT_TYPES(s):
    max_lora_num = 16
    inputs = {
      "required": {
        "num_loras": ("INT", {"default": 1, "min": 1, "max": max_lora_num}),
        "select": ("INT", {"min": 0, "max": max_lora_num - 1, "step": 1, "default": 0}),
      },
      "optional": {},
    }

    loras = folder_paths.get_filename_list("loras")

    for i in range(0, max_lora_num):
      inputs["optional"][f"lora_{i}_name"] = (loras, { "default": None})
    return inputs

  RETURN_TYPES = (AlwaysEqualProxy('*'),)
  RETURN_NAMES = ("lora_name",)
  FUNCTION = "select"

  CATEGORY = "Selector"

  def select(self,  num_loras: int, select: int, **kwargs):
    # 首先需要取余数以确保不会出现索引越界的情况
    assert(num_loras > 0)
    select = select % num_loras
    lora_name = kwargs.get(f"lora_{select}_name")
    return (lora_name, )


class CheckpointSelector:
  def __init__(self):
    pass

  @classmethod
  def INPUT_TYPES(s):
    max_ckpt_num = 16
    inputs = {
      "required": {
        "num_ckpts": ("INT", {"default": 1, "min": 1, "max": max_ckpt_num}),
        "select": ("INT", {"min": 0, "max": max_ckpt_num - 1, "step": 1, "default": 0}),
      },
      "optional": {},
    }

    ckpts = folder_paths.get_filename_list("checkpoints")

    for i in range(0, max_ckpt_num):
      inputs["optional"][f"ckpt_{i}_name"] = (ckpts, { "default": None})
    return inputs

  RETURN_TYPES = (AlwaysEqualProxy('*'),)
  RETURN_NAMES = ("ckpt_name",)
  FUNCTION = "select"

  CATEGORY = "Selector"

  def select(self,  num_ckpts: int, select: int, **kwargs):
    # 首先需要取余数以确保不会出现索引越界的情况
    assert(num_ckpts > 0)
    select = select % num_ckpts
    ckpt_name = kwargs.get(f"ckpt_{select}_name")
    return (ckpt_name, )



NODE_CLASS_MAPPINGS = {
  "lora selector": LoraSelector,
  "ckpt selector": CheckpointSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {

  "lora selector": "Lora Selector",
  "ckpt selector": "Checkpoint Selector",
}


