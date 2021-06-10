# coding:utf-8

import asyncio
from tornado import gen


@gen.coroutine
def foo(param1):
    yield asyncio.sleep(0.5)  # processing time
    print(param1.decode())
    return 'hah'
