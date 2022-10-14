#!/usr/bin/python3
#
# Simple Bloom filter implementation in Python 3
# Copyright 2017 Hector Martin "marcan" <marcan@marcan.st>
# Licensed under the terms of the MIT license
# Adapted by Emily Dolson in 2022
#
# Use something like this to work out what 'm' and 'k' you need:
#   https://krisives.github.io/bloom-calculator/
#
# Examples:
#
#   $ python3
#   >>> from hashlib import sha1
#   >>> from bloom import BloomFilter
#   >>> filter = BloomFilter(1000, 1)
#   >>> filter.add("hi")
#   >>> filter.contains("hi")
#   True
#   >>> filter.contains("bye")
#   False

import mmap
from hashlib import md5


class BloomFilter(object):
    ALIGN = 65536
    THRESHOLD_HEADROOM = 2**16  # for uniformity, rehash after fewer bits left

    def __init__(self, m=None, k=None):
        self.bits = None
        self.create(m, k)

    def create(self, m, k):
        size = (m + 7) // 8
        size = (size + self.ALIGN - 1) & ~(self.ALIGN - 1)
        self.m = m
        self.k = k
        self.size = size
        self.offset = self.ALIGN
        self.threshold = 1
        while self.threshold < self.m:
            self.threshold *= 2
        self.threshold *= self.THRESHOLD_HEADROOM

        self.bits = mmap.mmap(-1, self.size, offset=self.offset)

    def hash(self, s):
        capacity = 0
        val = 0
        if isinstance(s, str):
            s = s.encode("utf-8")

        for i in range(self.k):
            if capacity < self.threshold:
                s = md5(s).digest()
                val = int.from_bytes(s, byteorder='big')
                capacity = 1 << 128
            h = val % self.m
            val //= self.m
            capacity //= self.m
            yield h

    def add(self, s):
        for h in self.hash(s):
            byte, bit = h >> 3, h & 7
            self.bits[byte] |= 1 << bit

    def update(self, iterable):
        for s in iterable:
            for h in self.hash(s):
                byte, bit = h >> 3, h & 7
                self.bits[byte] |= 1 << bit

    def contains(self, s):
        for h in self.hash(s):
            byte, bit = h >> 3, h & 7
            if not (self.bits[byte] & (1 << bit)):
                return False
        return True

    def sync(self):
        self.bits.flush()

    def __del__(self):
        if self.bits:
            self.bits.flush()
            self.bits.close()
