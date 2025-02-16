import os

# Ambil PRIVATE_KEY dari Environment Variables di Railway
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
RPC_URL = os.getenv("RPC_URL")
TOKEN_ADDRESS = os.getenv("TOKEN_ADDRESS")

def snipe():
    print(f"Bot sniper berjalan dengan private key: {PRIVATE_KEY[:5]}... (disensor)")
    print(f"RPC: {RPC_URL}")
    print(f"Token Address: {TOKEN_ADDRESS}")
    # Tambahkan logika trading di sini

if __name__ == "__main__":
    snipe()
