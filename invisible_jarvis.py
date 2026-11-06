import asyncio
import threading
import keyboard
import pystray
from PIL import Image, ImageDraw
from core.manager_agent import jarvis_app
from core.config import config
from agents.voice_agent import voice_agent

# Setup simple notification/overlay logic (simulated for now)
def show_overlay(text):
    print(f"\n[JARVIS OVERLAY]: {text}")

class JarvisInvisibleMode:
    def __init__(self):
        self.is_active = False
        self.loop = asyncio.new_event_loop()
        
    def start_async_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    async def process_command(self, text):
        print(f"\n👤 User: {text}")
        inputs = {"input": text, "agent_results": []}
        result = await jarvis_app.ainvoke(inputs)
        response = result.get("final_response", "Sorry bhai, kuch samajh nahi aaya.")
        print(f"🤖 JARVIS: {response}")
        # Use voice agent to speak the response
        await voice_agent.handle_task(response)

    def on_hotkey(self):
        print("\n[System] Hotkey pressed! Listening for command...")
        # In a real scenario, this would trigger a small UI or voice record
        # For now, we'll use a simple input in terminal to simulate the overlay
        user_text = input("🎤 Speak/Type to JARVIS: ")
        asyncio.run_coroutine_threadsafe(self.process_command(user_text), self.loop)

    def create_tray_icon(self):
        # Create a simple blue circle icon for the system tray
        image = Image.new('RGB', (64, 64), color=(0, 102, 255))
        draw = ImageDraw.Draw(image)
        draw.ellipse((10, 10, 54, 54), fill=(0, 242, 255))
        
        menu = (
            pystray.MenuItem('Open Chat', lambda: print("Chat opened!")),
            pystray.MenuItem('Exit', self.stop_system),
        )
        icon = pystray.Icon("JARVIS", image, "JARVIS Invisible Mode", menu)
        icon.run()

    def stop_system(self, icon):
        icon.stop()
        self.loop.stop()
        os._exit(0)

if __name__ == "__main__":
    jarvis = JarvisInvisibleMode()
    
    # Start the async loop in a background thread
    threading.Thread(target=jarvis.start_async_loop, daemon=True).start()
    
    # Global Hotkey: Ctrl+Space to trigger JARVIS
    keyboard.add_hotkey('ctrl+space', jarvis.on_hotkey)
    
    print("\n" + "="*50)
    print("🚀 JARVIS INVISIBLE MODE ACTIVE 🚀")
    print("- Press 'Ctrl + Space' to trigger JARVIS")
    print("- Look for the Blue Orb in your System Tray (bottom right)")
    print("="*50 + "\n")
    
    # Start system tray icon
    jarvis.create_tray_icon()
