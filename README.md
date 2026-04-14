reco

A simple CLI tool for spaced repetition (reviewing concepts over time).

It helps you remember things by scheduling reviews and tracking your progress.

---

Features

- Add new concepts
- Automatically generate review dates
- Mark reviews as done
- Show all concepts in a clean table
- Show today's due reviews

---

Installation

git clone <https://github.com/dev-echo-echo/reco.git>
cd reco
chmod +x install.sh
./install.sh

Make sure this directory is in your PATH:

~/.local/bin

---

Usage

Add a concept

reco --add "trigonometric functions"

---

Show all concepts

reco --show

---

Show today's reviews

reco --today

---

Mark a review as done

reco --mark

---

Data Storage

Data is stored in:

~/.local/share/reco/data.json

---

Notes

- Do not manually edit the data file unless you know what you are doing.
- Do not delete the installation directory after installing.

---

Future Ideas

- Add support for categories (roots and branches)
- add simple progress stats (done vs missed vs due)
- show completion percentage all reviews
