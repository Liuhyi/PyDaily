import os
import traceback
from collections import defaultdict


class Solution:
    def count_files_by_type(self, dir):
        map = defaultdict(int)
        try:
            items = os.listdir(dir)
        except PermissionError:
            traceback.print_exc()
            return map
        except Exception:
            traceback.print_exc()
            return map
        for filename in items:
            path = os.path.join(dir, filename)
            try:
                if os.path.isdir(path):
                    sub_map = self.count_files_by_type(path)
                    for key, value in sub_map.items():
                        map[key] += value
                else:
                    extensions = filename.split(".")[-1] if '.' in filename else "NoExtensionFile"
                    map[extensions] += 1
            except PermissionError:
                traceback.print_exc()
            except Exception:
                traceback.print_exc()
        return map


if __name__ == '__main__':
    dir = r"D:\\"
    res = Solution().count_files_by_type(dir)
    print(res)
