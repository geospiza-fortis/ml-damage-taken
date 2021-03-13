import json

# https://forum.maplelegends.com/index.php?threads/nises-formula-compilation.36234/
text = """
BEGINNER
- Level 1: PDD = 7
- Level 5: PDD = 17
- Level 8: PDD = 19

WARRIOR
- Level 10: PDD = 54
- Level 12: PDD = 57
- Level 15: PDD = 83
- Level 20: PDD = 106
- Level 22: PDD = 109
- Level 25: PDD = 129
- Level 30: PDD = 154
- Level 35: PDD = 179
- Level 40: PDD = 203
- Level 47: PDD = 208
- Level 50: PDD = 261
- Level 55: PDD = 267
- Level 60: PDD = 305
- Level 65: PDD = 308
- Level 70: PDD = 359
- Level 75: PDD = 356
- Level 80: PDD = 382
- Level 85: PDD = 388
- Level 90: PDD = 440
- Level 95: PDD = 446
- Level 100: PDD = 494

MAGICIAN
- Level 8: PDD = 25
- Level 10: PDD = 31
- Level 13: PDD = 40
- Level 15: PDD = 49
- Level 18: PDD = 54
- Level 20: PDD = 56
- Level 25: PDD = 60
- Level 28: PDD = 64
- Level 30: PDD = 75
- Level 33: PDD = 91
- Level 35: PDD = 98
- Level 40: PDD = 99
- Level 48: PDD = 107
- Level 50: PDD = 131
- Level 55: PDD = 134
- Level 58: PDD = 142
- Level 60: PDD = 159
- Level 65: PDD = 162
- Level 68: PDD = 170
- Level 70: PDD = 184
- Level 75: PDD = 190
- Level 78: PDD = 198
- Level 80: PDD = 212
- Level 85: PDD = 218
- Level 88: PDD = 226
- Level 90: PDD = 240
- Level 95: PDD = 246
- Level 98: PDD = 254
- Level 100: PDD = 266

ARCHER
- Level 10: PDD = 32
- Level 15: PDD = 49
- Level 20: PDD = 65
- Level 25: PDD = 80
- Level 30: PDD = 95
- Level 35: PDD = 110
- Level 40: PDD = 125
- Level 50: PDD = 145
- Level 55: PDD = 148
- Level 60: PDD = 177
- Level 65: PDD = 180
- Level 70: PDD = 206
- Level 75: PDD = 212
- Level 80: PDD = 238
- Level 85: PDD = 244
- Level 90: PDD = 270
- Level 95: PDD = 276
- Level 100: PDD = 298

THIEF
- Level 10: PDD = 42
- Level 15: PDD = 60
- Level 20: PDD = 76
- Level 22: PDD = 85
- Level 25: PDD = 100
- Level 30: PDD = 115
- Level 32: PDD = 116
- Level 35: PDD = 131
- Level 37: PDD = 132
- Level 40: PDD = 147
- Level 50: PDD = 184
- Level 55: PDD = 187
- Level 60: PDD = 220
- Level 65: PDD = 223
- Level 70: PDD = 257
- Level 75: PDD = 263
- Level 80: PDD = 291
- Level 85: PDD = 297
- Level 90: PDD = 325
- Level 95: PDD = 331
- Level 100: PDD = 331

PIRATE
- Level 10: PDD = 24
- Level 15: PDD = 43
- Level 20: PDD = 56
- Level 25: PDD = 69
- Level 30: PDD = 82
- Level 35: PDD = 95
- Level 40: PDD = 108
- Level 50: PDD = 146
- Level 55: PDD = 149
- Level 60: PDD = 178
- Level 65: PDD = 181
- Level 70: PDD = 207
- Level 75: PDD = 213
- Level 80: PDD = 239
- Level 85: PDD = 245
- Level 90: PDD = 271
- Level 100: PDD = 309
"""

cur = ""
data = []
for line in [l.strip() for l in text.split("\n")]:
    if not line:
        continue
    if "-" not in line:
        cur = line.lower()
        continue
    # regular expression might be cleaner
    lhs, rhs = line.split(": ")
    data += [
        dict(job=cur.lower(), level=int(lhs.split()[-1]), pdd=int(rhs.split()[-1]))
    ]

print(json.dumps(data, indent=2))