import pytest

from vercel_kv import KV

@pytest.mark.asyncio
async def test():
    app = KV()
    print(app.has_auth())
    print(app.set(key="sss", value="asasd"))
    print(app.get("sss"))
