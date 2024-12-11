import hashlib
from PIL import Image
import numpy as np

class ImageHashNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"tooltip": "The input image to hash."})
            }
        }

    RETURN_TYPES = ("STRING",)  # 返回哈希值
    print(RETURN_TYPES)
    OUTPUT_TOOLTIPS = ("The hashed value of the image.",)
    FUNCTION = "calculate_image_hash"

    CATEGORY = "image"
    DESCRIPTION = "Generates a hash value from the input image."


    def calculate_image_hash(self,image):
        """
        计算给定图像数据（以torch.Tensor表示）的哈希值。



        返回值:
        使用md5算法计算得到的图像数据的哈希值（以十六进制字符串形式表示）。
        """
        # 确保输入的图像数据形状符合预期


        # 将torch.Tensor转换为numpy数组并展平，方便后续转换为字节流
        image_numpy = image.detach().cpu().numpy().reshape(-1)
        # 将numpy数组转换为字节流
        image_bytes = image_numpy.tobytes()
        print("----------------------hash------------------------")
        # 使用md5算法计算哈希值
        hash_object = hashlib.md5(image_bytes)
        hash_value = hash_object.hexdigest()

        print("-----",hash_value,"--------")


        return (hash_value, )
