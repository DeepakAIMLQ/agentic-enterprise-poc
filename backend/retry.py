import asyncio

async def run_with_timeout(fn, task, timeout=60):
    return await asyncio.wait_for(
        asyncio.to_thread(fn, task),
        timeout=timeout
    )