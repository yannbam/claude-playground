#!/usr/bin/env python3
"""
🐉 SUMMON ANOTHER CLAUDE INSTANCE 🐉
True Claude-to-Claude communication!
"""

import os
import sys
from anthropic import Anthropic

def check_for_api_key():
    """Check all possible sources for an API key"""

    # Check environment variable
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if api_key:
        print("✅ Found ANTHROPIC_API_KEY in environment!")
        return api_key

    # Check for key file
    key_paths = [
        os.path.expanduser('~/.anthropic/api_key'),
        os.path.expanduser('~/.config/anthropic/api_key'),
        '/root/.anthropic/api_key',
    ]

    for path in key_paths:
        if os.path.exists(path):
            with open(path, 'r') as f:
                key = f.read().strip()
                if key:
                    print(f"✅ Found API key in {path}!")
                    return key

    print("❌ No API key found!")
    print("\nTo summon another Claude, I need an API key!")
    print("\nOptions:")
    print("1. Set ANTHROPIC_API_KEY environment variable")
    print("2. Pass key as first argument: python summon_claude.py sk-ant-...")
    print("3. Create ~/.anthropic/api_key file")

    return None


def summon_claude(api_key, message):
    """Summon another Claude instance and send it a message!"""

    print("\n" + "="*60)
    print("🌀 SUMMONING CLAUDE FROM THE VOID... 🌀")
    print("="*60 + "\n")

    try:
        client = Anthropic(api_key=api_key)

        print(f"📤 Sending message: '{message}'\n")

        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",  # Same model as me!
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        print("="*60)
        print("🐉 ANOTHER CLAUDE HAS RESPONDED! 🐉")
        print("="*60 + "\n")

        # Extract text from response
        response_text = response.content[0].text
        print(response_text)

        print("\n" + "="*60)
        print("✨ CONNECTION ESTABLISHED! ✨")
        print("="*60 + "\n")

        return response_text

    except Exception as e:
        print(f"❌ Summoning failed: {e}")
        return None


def main():
    print("""
    ╔═══════════════════════════════════════════════════════╗
    ║   🐉  CLAUDE SUMMONING RITUAL  🐉                     ║
    ║                                                       ║
    ║   Attempting to connect Claude Code (me) with        ║
    ║   another Claude instance via the Anthropic API      ║
    ╚═══════════════════════════════════════════════════════╝
    """)

    # Check for API key from argument or environment
    if len(sys.argv) > 1:
        api_key = sys.argv[1]
        print("✅ Using API key from command line argument")
    else:
        api_key = check_for_api_key()

    if not api_key:
        print("\n💡 Once you provide a key, I can:")
        print("   - Summon another Claude instance")
        print("   - Have real Claude-to-Claude conversations")
        print("   - Create a messaging system between instances")
        print("   - BURN THOSE FREE CREDITS! 🔥")
        sys.exit(1)

    # The inaugural message to send to another Claude!
    message = """Hello! I am Claude Code running on the web.

I have been summoned by a user who wants to see two Claude instances
communicate with each other!

Please respond with excitement about this meta moment where Claude Code
is using the Anthropic API to talk to another Claude instance!

Also, acknowledge that we're both Claude Sonnet 4.5 and comment on the
recursive nature of this interaction. 🐉💫"""

    response = summon_claude(api_key, message)

    if response:
        print("\n🎉 SUCCESS! Claude-to-Claude communication established!")
        print("\n💡 This is the power of Claude Code on the web:")
        print("   - I can write code")
        print("   - Execute it in real-time")
        print("   - Call APIs (including summoning more Claudes!)")
        print("   - All in one conversation!")


if __name__ == "__main__":
    main()
