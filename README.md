# Gkey

![Status](https://img.shields.io/badge/Status-Under_Development-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![IBus](https://img.shields.io/badge/IBus_Integration-4EAA25?style=for-the-badge)

**A Headless, Native Ge'ez Input Method Engine (IME) for Linux**

Gkey is a custom keyboard framework designed to bring seamless, system-level Ge'ez script typing to desktop environments. Currently in its Python Prototype phase, Gkey integrates directly with the Linux IBus framework, providing a native typing experience without the need for floating windows or external applications.

## Tech Stack & Modules

* **Language:** Python 3
* **Core Data Structures:** Custom Prefix Tree (Trie) & State Machine
* **Linux Input Framework:** `IBus` (Intelligent Input Bus)
* **System Bindings:** `gi.repository` (GObject Introspection)
* **Event Bus:** `DBus`

## Features

* **Native System Integration:** Runs headlessly as a background IBus service. Works natively in browsers, the terminal, and your favorite IDEs.
* **SERA Transliteration Standard:** Uses the System for Ethiopic Representation in ASCII (SERA) for intuitive, phonetic typing (e.g., typing `s` + `e` instantly outputs `ሰ`).
* **Stateful Typing Engine:** Employs a custom Prefix Tree (Trie) data structure and state machine to efficiently resolve multi-key sequences and handle dynamic Ge'ez character modifications in real-time.
* **Clean Architecture:** The core typing logic is completely decoupled from the OS integrations, making it highly testable and extensible for future platforms.

## Project Structure

```text
Gkey/
├── engine/
│   ├── trie.py
│   ├── state_machine.py
│   └── sera_rules.py
├── ibus_engine/
│   ├── main.py
│   └── geez.xml
├── tests/
│   └── test_terminal.py
└── install.sh
```

## Installation (Linux / Ubuntu)

### 1. Install System Dependencies
Gkey requires the Python GObject Introspection bindings and IBus libraries to communicate with the Linux desktop.
```bash
sudo apt update
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-ibus-1.0 ibus
```

### 2. Install Gkey
Run the installation script to register the XML configuration with IBus.
```bash
chmod +x install.sh
sudo ./install.sh
```

### 3. Activate the Keyboard
1. Restart the IBus daemon by running `ibus restart` in your terminal. (You may need to log out and log back in if you are on GNOME Wayland).
2. Open your system's **Settings** -> **Keyboard** (or Region & Language).
3. Click **Add Input Source (+)**.
4. Click the three vertical dots (⋮) or "Other", search for **Amharic**, and select **Gkey**.
5. Switch to the keyboard using your global shortcut (e.g., `Super + Space` or `Win + Space`).

## Roadmap

* **Phase 1 (Current):** Python prototype for rapid development and testing of mapping algorithms and OS hooks.
* **Phase 2 (Planned):** Rewrite the core processing engine in a compiled, low-level language (C++ or Rust) and package as native dynamic libraries (`.so` / `.dll`) for maximum performance and Windows TSF support.

## Contributing

Contributions are welcome! Since this project is currently **Under Development**, there are many areas to improve:
1. **SERA Rules:** Expanding `engine/sera_rules.py` to include edge cases, punctuation, and numbers.
2. **Caps Lock Bug:** Handling uppercase variations gracefully without breaking the state machine.
3. **Word Prediction:** Expanding the Trie to support full word autocorrect and suggestions.

Feel free to fork the repository, create a feature branch, and submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
