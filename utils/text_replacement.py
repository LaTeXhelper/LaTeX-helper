import re
from typing import List

def replace(origin:str,source_list:List[str],target_list:List[str])->str:
    for source,target in zip(source_list,target_list):
        origin = re.sub(source,target,origin)
    return origin
