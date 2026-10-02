class HashMap:
    def __init__(self, items=None, capacity=8, load_factor=0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

        if items:
            self.update(items)

    # ---------- internos ----------
    def _bucket(self, key):
        return self.buckets[hash(key) % self.capacity]

    def _resize(self):
        old_items = list(self.items())
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for key, value in old_items:
            self[key] = value

    # ---------- operadores: m[k], m[k] = v, del m[k], k in m ----------
    def __setitem__(self, key, value):
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.size / self.capacity > self.load_factor:
            self._resize()

    def __getitem__(self, key):
        for k, v in self._bucket(key):
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key):
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(key)

    def __contains__(self, key):
        return any(k == key for k, _ in self._bucket(key))

    # ---------- métodos estilo dict ----------
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def pop(self, key, *default):
        try:
            value = self[key]
        except KeyError:
            if default:
                return default[0]
            raise
        del self[key]
        return value

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default
        return self[key]

    def update(self, other):
        pairs = other.items() if hasattr(other, "items") else other
        for key, value in pairs:
            self[key] = value

    def clear(self):
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

    # ---------- iteración ----------
    def items(self):
        for bucket in self.buckets:
            yield from bucket

    def keys(self):
        for k, _ in self.items():
            yield k

    def values(self):
        for _, v in self.items():
            yield v

    def __iter__(self):
        return self.keys()

    def __len__(self):
        return self.size

    # ---------- representación ----------
    def __repr__(self):
        inner = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return f"HashMap({{{inner}}})"

    def __eq__(self, other):
        if not isinstance(other, HashMap):
            return NotImplemented
        return len(self) == len(other) and all(
            k in other and other[k] == v for k, v in self.items()
        )