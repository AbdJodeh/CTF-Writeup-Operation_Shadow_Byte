#!/usr/bin/env python3
"""
Operation Shadow Byte — Full Solver
CYSC Campus CTF @ Al Hussein Technical University (HTU)

Author: Abd Al-Rahman Jodeh
"""

import base64
import hashlib

# ──────────────────────────────────────────────────────────────
# Intercepted payload (provided in decoder.py)
# ──────────────────────────────────────────────────────────────
ENCRYPTED_HEX = (
    "233c515d2631202e2320292630082610312c183c213b201026322c3b2323393f34"
    "08073c304918373a2d052c38310a2a210e172634213a10322d445c300354110b19"
    "300915311c0f370e2610342e1c51173f0d0e0d202c0e2e32171c3b230c1036213e"
    "57123f0d0a2c1c0e482e0b171902560b442b3c450b1705090a0e20570a170f1c0f"
    "36541b1b014b0415202f541c0c1b531f2355175c033c211335490c1511063b002c"
    "1e231e3836313f00560318063c32092a060652263257481536310603230b43062e17"
    "02125a371e0e1a091e112d395b05091b1d063e4157105a2403243f28123d220b19"
    "03090b0e06001f2e3a2b2010263128101608045e28203a1001313e5112300917351e"
    "151e2e57465804235e46072e451112302c17263f38092d3d1b1d033321042b3a10"
    "54111102030d20271e112d175c28230b450331321217290e032634521e210b1f1d05"
    "0e00102c3a361d11303b0d0d1a3b0a3d2d17063b330b03002a3614113f05172633"
    "274c370e1b583b090c412b3c102825580d3d394637322022465b051e001006172e13"
    "3c3c285421200d4b170f225d3b0a2942072d171f10123855213037013a22460502"
    "0e21462d2d2d1c3d3c3855220d2f49391f2a5d05303d00380317543e020512212324"
    "153a1f2a102c30040e014a13503d2c2c510a333803150f31122c23000e2d2d3d5710"
    "1237572023054910574b5b3b0e3a43013d13563d3c24553544344a3931395c2f1e2a"
    "472c313d552902371c2033374a153122102f2022442f2d36543d060654203305322257"
    "250402235710032e32503a203708351a150c3d201b1d050a1f03380036142a30330c"
    "2630574a3d232531320a1b07062e2e5612062f0a0b4452322431435131305f4e322d"
    "445c233c515d3f2352402431435131305f4e322d445c233c515d3f23524024314351"
    "31305f4e322d445c233c515d3f23524024344e55"
)


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """Decrypt a Vigenère-encrypted string with the given key."""
    key_upper = key.upper()
    result = []
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key_upper[key_index % len(key_upper)]) - ord("A")
            base = ord("A") if char.isupper() else ord("a")
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


def solve():
    print("=" * 60)
    print("  Operation Shadow Byte — Solver")
    print("=" * 60)

    # Layer 1: Hex → bytes → XOR decrypt
    raw_bytes = bytes.fromhex(ENCRYPTED_HEX)
    xor_key = b"shadowbyte"
    xor_decrypted = bytes(
        [raw_bytes[i] ^ xor_key[i % len(xor_key)] for i in range(len(raw_bytes))]
    )

    print("\n[Layer 1] XOR Decryption (key: 'shadowbyte')")
    print(f"  Output preview: {xor_decrypted.decode()[:60]}...")

    # Layer 2: Base64 decode
    b64_decoded = base64.b64decode(xor_decrypted).decode()

    print("\n[Layer 2] Base64 Decode")
    print(f"  Output preview: {b64_decoded[:60]}...")

    # Layer 3: Vigenère decrypt
    plaintext = vigenere_decrypt(b64_decoded, "NEPTUNE")

    print("\n[Layer 3] Vigenère Decrypt (key: 'NEPTUNE')")
    print("-" * 60)
    print(plaintext)
    print("-" * 60)

    # Layer 4: Verify the password against the hash
    password = "CrimsonVeil_Aqaba1967"
    salt = "CYSTECH"
    computed_hash = hashlib.sha512((password + salt).encode()).hexdigest()

    expected_hash = (
        "cbb9245f6e49bbfe73f654a14abc3b962565334369a4cc7527b51a761192de94"
        "39d6ff0f0f2926d5d984cb7b58c87515cfd12d7144e4b5d857e4143710f6e488"
    )

    print(f"\n[Layer 4] Hash Verification")
    print(f"  Password:  {password}")
    print(f"  Salt:      {salt}")
    print(f"  SHA-512:   {computed_hash}")
    print(f"  Match:     {'YES' if computed_hash == expected_hash else 'NO'}")

    print(f"\n{'=' * 60}")
    print(f"  FLAG: HTU{{{password}}}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    solve()
