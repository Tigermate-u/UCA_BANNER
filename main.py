import os
import time
import sys
import shutil
import platform
import random

# Tool: UCA-GOD-MODE (COLOR FIXED)
# Author: Mr.LEVIATHAN
# Fix: Fixed ANSI Escape Codes for Termux .bashrc

# --- PYTHON COLORS (Only for Python Preview) ---
R = '\033[1;31m'
G = '\033[1;32m'
C = '\033[1;36m'
Y = '\033[1;33m'
W = '\033[1;37m'
BK = '\033[1;30m'
RESET = '\033[0m'

system_os = platform.system()

try:
    import pyfiglet
except ImportError:
    pyfiglet = None

def get_cols():
    try:
        cols, _ = shutil.get_terminal_size()
    except:
        cols = 80
    return cols

def clear():
    if system_os == "Windows": os.system('cls')
    else: os.system('clear')

# --- HEADER ---
def print_header():
    logo = f"""
{C}██╗   ██╗ ██████╗ ██████╗ 
{C}██║   ██║██╔════╝██╔══██╗   {Y}[ UCA TERMINAL PRO ]
{C}██║   ██║██║     ███████║
{C}██║   ██║██║     ██╔══██║   {R}OWNER : Mr.LEVIATHAN
{C}╚██████╔╝╚██████╗██║  ██║   {G}STATUS: ONLINE
{C} ╚═════╝  ╚═════╝╚═╝  ╚═╝{RESET}
"""
    print(logo)

# --- FONT DB ---
font_db = [
    ("Bloody", "bloody"), ("Ansi Shadow", "ansi_shadow"), ("Graffiti", "graffiti"),
    ("Electronic", "electronic"), ("Sub-Zero", "sub-zero"), ("Calvin S", "calvin_s"),
    ("Slant", "slant"), ("Rectangles", "rectangles"), ("Larry 3D", "larry3d"),
    ("Delta Corps", "delta_corps_priest_1"), ("Standard", "standard"), ("Big", "big"),
    ("Script", "script"), ("Doom", "doom"), ("Speed", "speed")
]

# --- PREVIEW ---
def show_preview(name, font_file, font_name):
    clear()
    cols = get_cols()
    
    print(f"{C}╔{'═'*(cols-2)}╗")
    print(f"{C}║ {Y}PREVIEW MODE: {font_name.upper()} {C}".center(cols+18))
    print(f"{C}╚{'═'*(cols-2)}╝{RESET}\n")
    
    if system_os == "Windows":
        if pyfiglet:
            try:
                # Windows Mapping
                f_map = {"bloody": "larry3d", "ansi_shadow": "doom"}
                use_font = f_map.get(font_file, "standard")
                print(f"{C}{pyfiglet.figlet_format(name, font=use_font)}{RESET}")
            except: pass
    else:
        # Termux Download & Render
        path = f"/data/data/com.termux/files/usr/share/figlet/{font_file}.flf"
        if not os.path.exists(path):
             os.system(f"wget -q http://www.figlet.org/fonts/{font_file}.flf -O {path}")
             if not os.path.exists(path) or os.path.getsize(path) < 100:
                 os.system(f"wget -q https://github.com/xero/figlet-fonts/raw/master/{font_file}.flf -O {path}")
                 if font_file == "ansi_shadow": os.system(f"wget -q https://github.com/xero/figlet-fonts/raw/master/ANSI%20Shadow.flf -O {path}")
        
        os.system(f'figlet -f {font_file} -w {cols} -c "{name}" | lolcat')

    print(f"\n{C}╔{'═'*(cols-2)}╗")
    print(f"{C}║{f'{Y}>>> Made By Mr.LEVIATHAN <<<'.center(cols+8)}{C}║")
    print(f"{C}╚{'═'*(cols-2)}╝{RESET}")

# --- MAIN ---
def main():
    clear()
    print_header()

    try:
        print(f" {C}┌──[ {Y}IDENTITY {C}]")
        name = input(f" {C}└─➤ {W}ENTER USERNAME :: {Y}").strip()
    except: name = "LEVIATHAN"
    if not name: name = "LEVIATHAN"

    while True:
        clear()
        print_header()
        
        # Menu
        for i, (fname, ffile) in enumerate(font_db):
            print(f" {C}[{i+1:02}] {W}{fname}")

        try:
            choice = int(input(f"\n {C}└─➤ {W}SELECT ID :: {Y}"))
            if 1 <= choice <= len(font_db):
                sel_name, sel_file = font_db[choice-1]
            else: sel_name, sel_file = font_db[0]
        except: sel_name, sel_file = font_db[0]

        show_preview(name, sel_file, sel_name)
        
        confirm = input(f"\n {C}[?] APPLY? (y/n): {W}").lower()
        if confirm == 'y': break

    # --- BASHRC GENERATION (THE FIX) ---
    clear()
    print(f"{G}[*] FIXING COLOR CODES & INSTALLING...{RESET}")
    time.sleep(1)

    # Note: We use double backslashes \\033 to ensure they are written as \033 in the file
    bashrc_content = f"""
# --- UCA SYSTEM ---
clear

# 1. Colors Defined INSIDE Bash (Prevents Broken Codes)
# These are standard ANSI codes
C="\\033[1;36m"
R="\\033[1;31m"
G="\\033[1;32m"
Y="\\033[1;33m"
W="\\033[1;37m"
BK="\\033[1;30m"
RESET="\\033[0m"

# 2. Voice (Hidden Errors & Background Noise)
if command -v termux-tts-speak &> /dev/null; then
    termux-tts-speak "Welcome back {name}" > /dev/null 2>&1 &
    disown
fi

# 3. Prompt (Using \\[ \\] to prevent wrapping issues)
PS1='\\[$C\\]┌──(\\[$R\\]UCA💀PRO\\[$C\\])-[\\[$W\\]\\w\\[$C\\]]\\n\\[$C\\]└─\\[$Y\\]\\$\\[$RESET\\] '

# 4. Variables
COLS=$(tput cols)
DATE=$(date +"%I:%M %p")

# 5. Battery (Hidden Errors)
BAT="N/A"
if command -v termux-battery-status &> /dev/null; then
    # Suppress error if API fails
    BAT_DATA=$(termux-battery-status 2>/dev/null)
    if [ ! -z "$BAT_DATA" ]; then
        BAT=$(echo "$BAT_DATA" | grep percentage | awk -F': ' '{{print $2}}' | tr -d ',')00
    fi
fi

# --- DRAWING THE HUD (Using echo -e for safety) ---

# Top Border
echo -e "$C╔$(printf '═%.0s' $(seq 1 $((COLS-2))))╗"

# Info Panel
echo -e "$C║ $R● $W UCA SYSTEM $R● $C USER: $Y{name.upper()} $R● $C BAT: $Y$BAT"

# Separator
echo -e "$C╠$(printf '═%.0s' $(seq 1 $((COLS-2))))╣"

# Banner
echo ""
# We assume figlet is installed, else fallback to echo
if command -v figlet &> /dev/null; then
    echo -e "$C"
    figlet -f {sel_file} -w $COLS -c "{name}"
    echo -e "$RESET"
else
    echo -e "$C   {name}   $RESET"
fi

# Footer
echo -e "$Y"
MSG=">>> SYSTEM SECURE | MADE BY Mr.LEVIATHAN <<<"
# Centering logic in bash
printf "%*s\\n" $(( (${{#COLS}} + ${{#MSG}}) / 2)) "$MSG"
echo -e "$RESET"

# Bottom Border
echo -e "$C╚$(printf '═%.0s' $(seq 1 $((COLS-2))))╝$RESET"
echo ""

alias cls='clear'
alias update='pkg update && pkg upgrade'
"""

    if system_os != "Windows":
        home = os.environ.get('HOME', '/data/data/com.termux/files/home')
        path = os.path.join(home, '.bashrc')
        
        # Backup old one
        if os.path.exists(path): os.system(f"cp {path} {path}.bak")
        
        # Write new one
        with open(path, 'w') as f: f.write(bashrc_content)
        
        clear()
        print(f"\n{G}╔══════════════════════════════════════════╗")
        print(f"{G}║   FIX APPLIED SUCCESSFULLY!              ║")
        print(f"{G}║   PLEASE RESTART TERMUX NOW.             ║")
        print(f"{G}╚══════════════════════════════════════════╝{RESET}\n")

if __name__ == "__main__":
    main()
