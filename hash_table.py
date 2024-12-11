import hashlib


class HashTableNode:
    # 创建一个静态哈希表
    hash_table = {}

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "hash_input": ("STRING", {"tooltip": "Input hash value to retrieve bound text."}),
            },
            "optional": {
                "text_input": ("STRING", {"multiline": True, "dynamicPrompts": True,
                                          "tooltip": "Input text to bind with the hash value."}),
                # "image_info": ("IMAGE", {"tooltip": "Pass existing image information."}),
            }

        }

    RETURN_TYPES = ("STRING","BOOLEAN")  # 第一种输出为文本，第二种为非干预信息
    RETURN_NAMES = ("Text","BOOLEAN")
    FUNCTION = "process"

    CATEGORY = "Custom Nodes"
    DESCRIPTION = "Node for managing a hash table with text bindings."

    def process(self, hash_input, text_input=None):
        is_first_time = hash_input not in self.hash_table

        # 如果有新的文本输入，将哈希值和文本绑定
        if text_input:
            self.hash_table[hash_input] = text_input
            print(f"Added binding: {hash_input} -> {text_input}")


        # 从哈希表中检索文本
        retrieved_text = self.hash_table.get(hash_input, "No binding found.")

        return (retrieved_text,is_first_time)  # 返回文本和图像信息
