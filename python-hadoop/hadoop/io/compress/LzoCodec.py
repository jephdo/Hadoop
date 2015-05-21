#!/usr/bin/env python

import lzo

from hadoop.io.InputStream import DataInputBuffer

class LzoCodec:

    def compress(self, data):
        return lzo.compress(data)

    def decompress(self, data):
        return lzo.decompress(data)

    def decompressInputStream(self, data):
        return DataInputBuffer(lzo.decompress(data))
