import copy


class FragileDict(object):
    def __init__(self, other_dict={}):
        self._lock = True
        self._data = copy.deepcopy(other_dict)

    def __getitem__(self, key):
        if self._lock:
            val = copy.deepcopy(self._data[key])
        else:
            if key not in self.back_copy:
                self.back_copy[key] = copy.deepcopy(self._data[key])
            elif key in self.new_copy:
                if self.new_copy[key] != self._data[key]:
                    self.back_copy[key] = copy.deepcopy(self._data[key])
            val = dict.__getitem__(self.back_copy, key)
        return val

    def __setitem__(self, key, val):
        if not self._lock:
            if key in self._data:
                if key not in self.new_copy:
                    self.new_copy[key] = copy.deepcopy(self._data[key])
            else:
                self.new_keys.append(key)
            dict.__setitem__(self._data, key, val)
        else:
            raise RuntimeError("Protected state")

    def __enter__(self):
        self._lock = False
        self.new_copy = {}
        self.new_keys = []
        self.back_copy = {}
        return self

    def __exit__(self, type, value, traceback):
        if type is not None and type is not KeyError:
            for key in self.new_copy:
                val = copy.deepcopy(self.new_copy[key])
                dict.__setitem__(self._data, key, val)
            for key in self.new_keys:
                del self._data[key]
            self.__delattr__('new_copy')
            self.__delattr__('new_keys')
            self.__delattr__('back_copy')
            self._lock = True
            print("Exception has been suppressed.")
            return True
        elif type is KeyError:
            for key in self.new_copy:
                val = copy.deepcopy(self.new_copy[key])
                dict.__setitem__(self._data, key, val)
            for key in self.new_keys:
                del self._data[key]
            self.__delattr__('new_copy')
            self.__delattr__('new_keys')
            self.__delattr__('back_copy')
            self._lock = True
            raise KeyError
        else:
            for key in self.back_copy:
                val = copy.deepcopy(self.back_copy[key])
                dict.__setitem__(self._data, key, val)
            self.__delattr__('new_copy')
            self.__delattr__('new_keys')
            self.__delattr__('back_copy')
            self._lock = True

    def __contains__(self, item):
        return dict.__contains__(self._data, item)
