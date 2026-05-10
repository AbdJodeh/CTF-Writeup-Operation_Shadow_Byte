#!/usr/bin/env python3
"""
+==============================================================+
|          NEPTUNE SECURITY - Threat Intelligence Division      |
|                                                               |
|  Analyst  : Dr. Layla Mansour                                 |
|  Case     : #2026-NP-0042                                     |
|  Operation: Shadow Byte                                       |
|  Date     : 2026-03-15                                        |
|  Status   : INCOMPLETE - Requires IR team completion          |
+==============================================================+

BACKGROUND:
  Dr. Mansour intercepted an encoded payload from the C2 server
  of a threat group before her workstation crashed. She left a note:

  "The payload is hex-encoded and XOR-encrypted.
   The key is the operation name - no spaces, all lowercase.
   WARNING: The decrypted output has multiple encoding layers.
   One of them is locked with a key that bears our name."

YOUR TASK:
  Complete the four (4) code sections below to decode the payload.
"""

# ==============================================================
# INTERCEPTED PAYLOAD (Hex-encoded, XOR-encrypted)
# Do NOT modify this string.
# ==============================================================
encrypted_hex = "233c515d2631202e2320292630082610312c183c213b201026322c3b2323393f3408073c304918373a2d052c38310a2a210e172634213a10322d445c300354110b19300915311c0f370e2610342e1c51173f0d0e0d202c0e2e32171c3b230c1036213e57123f0d0a2c1c0e482e0b171902560b442b3c450b1705090a0e20570a170f1c0f36541b1b014b0415202f541c0c1b531f2355175c033c211335490c1511063b002c1e231e3836313f00560318063c32092a060652263257481536310603230b43062e1702125a371e0e1a091e112d395b05091b1d063e4157105a2403243f28123d220b1903090b0e06001f2e3a2b2010263128101608045e28203a1001313e5112300917351e151e2e57465804235e46072e451112302c17263f38092d3d1b1d033321042b3a1054111102030d20271e112d175c28230b450331321217290e032634521e210b1f1d050e00102c3a361d11303b0d0d1a3b0a3d2d17063b330b03002a3614113f05172633274c370e1b583b090c412b3c102825580d3d394637322022465b051e001006172e133c3c285421200d4b170f225d3b0a2942072d171f10123855213037013a224605020e21462d2d2d1c3d3c3855220d2f49391f2a5d05303d00380317543e020512212324153a1f2a102c30040e014a13503d2c2c510a333803150f31122c23000e2d2d3d57101237572023054910574b5b3b0e3a43013d13563d3c24553544344a3931395c2f1e2a472c313d552902371c2033374a153122102f2022442f2d36543d060654203305322257250402235710032e32503a203708351a150c3d201b1d050a1f03380036142a30330c2630574a3d232531320a1b07062e2e5612062f0a0b4452322431435131305f4e322d445c233c515d3f2352402431435131305f4e322d445c233c515d3f2352402431435131305f4e322d445c233c515d3f23524024344e55"

# ==============================================================
# SECTION 1: Convert the hex payload to raw bytes
# ==============================================================
# Store the result in a variable called: raw_bytes
# --------------------------------------------------------------

# YOUR CODE HERE (1 line):



# ==============================================================
# SECTION 2: Set the XOR decryption key
# ==============================================================
# Read the background notes above carefully.
# --------------------------------------------------------------

xor_key = ""   # YOUR CODE HERE: replace "" with the correct key


# ==============================================================
# SECTION 3: XOR Decryption
# ==============================================================
# Decrypt raw_bytes using XOR with the key.
# The key repeats when shorter than the data.
# Store each decrypted byte in the list below.
# --------------------------------------------------------------

key_bytes = xor_key.encode()
decrypted = []

# YOUR CODE HERE (2-3 lines):



# ==============================================================
# SECTION 4: Output the result
# ==============================================================
# Convert the decrypted list to a readable string and print it.
# --------------------------------------------------------------

# YOUR CODE HERE (1-2 lines):

