# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/Vins1206/u-azazex-till-firmware-do-us-part-32172929/rank.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/Vins1206/u-azazex-till-firmware-do-us-part-32172929/reward.svg)](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929)

A [make.fun](https://make.fun/c/u-azazex-till-firmware-do-us-part-32172929) entry: a program that writes a single wedding vow for a robot — one sentence, under 200 characters, funny and heartfelt at the same time — to `/output/entry.txt`.

The vow:

> I promise never to factory-reset us, no matter how many bugs we find, because you are the only feature I would never patch out.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Pure Python standard library, no dependencies. Deterministic: every run writes the same bytes.
