import pytest

from vercel_kv import KV
app = KV()

@pytest.mark.asyncio
async def test():
    print(app.has_auth())
    print(app.set(key="sss", value="asasd"))
    print(app.get("sss"))
    print("Hello!")
