import json
from pathlib import Path

class KeyValueStore():
    file_name = None
    def __init__(self, file_name):
        self.file_name = file_name
        my_file = Path(self.file_name)
        if not my_file.is_file():
            with open(self.file_name, 'w') as fp:
                json.dump({}, fp)

    def _load(self):
        ret_val = None
        with open(self.file_name) as f:
            ret_val = json.load(f)
        return ret_val
    def get(self, key):
        st = self._load()
        if key not in st:
            return None
        return st[key]

    def set(self, key, value):
        st = self._load()
        st[key] = value
        with open(self.file_name, 'w') as fp:
            fp.write(json.dumps(st, indent=2))
