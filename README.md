The purpose of this two hash file is to skip calling the graph-generated text model when manipulating the image using a loop, and use the hash table to output the cached nodes.

The nodes file is provided to load the completed node
It can also be loaded manually:
	from hash import ImageHashNode  # 导入 ImageHashNode 类

	NODE_CLASS_MAPPINGS.update({
    	"ImageHashNode": ImageHashNode,
	})

	NODE_DISPLAY_NAME_MAPPINGS.update({
   	 "ImageHashNode": "Image Hash Generator",
	})
	from hash_table import HashTableNode  # 导入哈希表

	NODE_CLASS_MAPPINGS.update({
	    "HashTableNode": HashTableNode,
	})

	NODE_DISPLAY_NAME_MAPPINGS.update({
	    "HashTableNode": "Hash Table Manager",
	})
