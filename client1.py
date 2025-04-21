# chat_app_fastapi/client1.py
import asyncio
import websockets

async def client():
    uri = "ws://localhost:8000/ws/chat"
    username = "Alice"
    async with websockets.connect(uri) as websocket:
        print(f"👩 {username} connected to chat")
        await websocket.send(f"{username} has joined the chat.")

        async def send():
            while True:
                msg = input()
                await websocket.send(f"{username}: {msg}")

        async def receive():
            while True:
                response = await websocket.recv()
                print(f"\n🔔 {response}")

        await asyncio.gather(send(), receive())

asyncio.run(client())
