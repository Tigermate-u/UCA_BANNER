import os
import time
import sys
import shutil
import platform

# Tool: LEVIATHAN-ULTIMATE-CROSS-PLATFORM
# Author: Mr.LEVIATHAN
# Description: Works on Windows (Simulation) & Termux (Real)

# --- SYSTEM SETTINGS ---
system_os = platform.system()

# Check Pyfiglet for Windows Preview
try:
    import pyfiglet
except ImportError:
    pyfiglet = None

def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

width = get_width()

# --- COLORS ---
R = '\033[1;31m'
G = '\033[1;32m'
C = '\033[1;36m'
Y = '\033[1;33m'
W = '\033[1;37m'
BK = '\033[1;30m'
RESET = '\033[0m'

# --- UTILS ---
def clear():
    os.system('cls' if system_os == "Windows" else 'clear')

def loader(text):
    for x in range(0, 101, 5):
        sys.stdout.write(f"\r {C}:: {text} ... {Y}[{x}%]")
        sys.stdout.flush()
        time.sleep(0.02)
    print(f"\r {C}:: {text} ... {G}[COMPLETE]   ")

# --- DATA ---
THEMES = {
    1: {"name": "NEON CYAN",   "code": "36"},
    2: {"name": "HACKER GREEN","code": "32"},
    3: {"name": "ALERT RED",   "code": "31"},
    4: {"name": "ROYAL GOLD",  "code": "33"},
    5: {"name": "DEEP PURPLE", "code": "35"},
}

FONTS = [
    ("Ansi Shadow", "ansi_shadow"), ("Bloody", "bloody"), ("Graffiti", "graffiti"),
    ("Electronic", "electronic"), ("Sub-Zero", "sub-zero"), ("Slant", "slant"),
    ("Rectangles", "rectangles"), ("Standard", "standard"), ("Small", "small"),
    ("Script", "script"), ("Doom", "doom"), ("Big", "big")
]

# --- 1. BOOT SEQUENCE ---
def boot():
    clear()
    print(f"\n{BK} [KERNEL] DETECTED OS: {system_os.upper()}...{RESET}")
    time.sleep(1)
    
    logs = ["LOADING_MODULES", "CHECKING_COMPATIBILITY", "STARTING_INTERFACE"]
    for log in logs:
        sys.stdout.write(f"\r {C}:: SYSTEM >> {log:<25} {Y}[...]")
        time.sleep(0.2)
        sys.stdout.write(f"\r {C}:: SYSTEM >> {log:<25} {G}[OK]  \n")
    clear()

# --- 2. HEADER UI ---
def header(color=C):
    print(f"{color}██╗   ██╗ ██████╗ ██████╗ ")
    print(f"{color}██║   ██║██╔════╝██╔══██╗   {Y}[ PREMIUM EDITION ]")
    print(f"{color}██║   ██║██║     ███████║   {R}DEV: Mr.LEVIATHAN")
    print(f"{color}██║   ██║██║     ██╔══██║   {G}VER: 12.5 (FIXED)")
    print(f"{color}╚██████╔╝╚██████╗██║  ██║")
    print(f"{color} ╚═════╝  ╚═════╝╚═╝  ╚═╝{RESET}")
    print(f"{BK}{'='*width}{RESET}")

# --- WINDOWS PREVIEW GENERATOR ---
def get_windows_art(text, font_file):
    if not pyfiglet:
        return "[!] Install 'pyfiglet' to see art on Windows"
    
    # Mapping Termux font names to Pyfiglet names
    f_map = {
        "ansi_shadow": "doom", "bloody": "larry3d", "graffiti": "graffiti",
        "electronic": "computer", "sub-zero": "slant", "slant": "slant",
        "rectangles": "rectangles", "standard": "standard", "small": "small",
        "script": "script", "doom": "doom", "big": "big"
    }
    use_font = f_map.get(font_file, "standard")
    try:
        return pyfiglet.figlet_format(text, font=use_font, width=width, justify="center")
    except:
        return pyfiglet.figlet_format(text)

# --- MAIN WORKFLOW ---
def main():
    boot()
    header()

    # --- STEP 1: IDENTITY ---
    print(f"\n {C}┌──[ {Y}STEP 1: IDENTITY {C}]")
    try:
        name = input(f" {C}└─➤ {W}ENTER USERNAME :: {Y}").strip()
    except: name = "LEVIATHAN"
    if not name: name = "LEVIATHAN"

    # --- STEP 2: SECURITY ---
    print(f"\n {C}┌──[ {Y}STEP 2: LOCK SCREEN {C}]")
    print(f" {C}│ {BK}Leave empty for auto-login.")
    password = input(f" {C}└─➤ {W}SET PASSWORD :: {Y}").strip()

    # --- STEP 3: THEME ---
    print(f"\n {C}┌──[ {Y}STEP 3: SELECT THEME {C}]")
    for k, v in THEMES.items():
        col = f"\033[1;{v['code']}m"
        print(f" {C}│ {col}[{k}] {v['name']}{RESET}")
    
    try:
        t_id = int(input(f" {C}└─➤ {W}ENTER ID :: {Y}"))
        if t_id not in THEMES: t_id = 1
    except: t_id = 1
    
    sel_theme = THEMES[t_id]
    
    # --- STEP 4: FONT PREVIEW LOOP ---
    while True:
        clear()
        TC = f"\033[1;{sel_theme['code']}m" # Selected Theme Color
        
        header(TC)
        print(f"{TC} [ USER: {name.upper()} ]   [ THEME: {sel_theme['name']} ]{RESET}\n")
        
        # Grid Menu
        for i, (fname, ffile) in enumerate(FONTS):
            print(f" {TC}[{i+1:02}] {W}{fname}")
        
        print(f"\n {TC}┌──[ {Y}FONT CONFIG {TC}]")
        try:
            f_id = int(input(f" {TC}└─➤ {W}ENTER ID :: {Y}"))
            if 1 <= f_id <= len(FONTS):
                sel_font_name, sel_font_file = FONTS[f_id-1]
            else:
                sel_font_name, sel_font_file = FONTS[0]
        except: sel_font_name, sel_font_file = FONTS[0]

        # --- PREVIEW LOGIC ---
        clear()
        print(f"\n{BK}Rendering Preview...{RESET}")
        
        # UI Box
        print(f"{TC}╔{'═'*(width-2)}╗")
        print(f"{TC}║ {Y}PREVIEW MODE: {sel_font_name.upper()} {TC}".center(width+15))
        print(f"{TC}╠{'═'*(width-2)}╣")
        print(f"{TC}║{' '*(width-2)}║")
        
        print(f"{TC}")
        
        # SMART RENDERER (Windows vs Termux)
        if system_os == "Windows":
            print(get_windows_art(name, sel_font_file))
        else:
            # Termux: Download if missing
            path = f"/data/data/com.termux/files/usr/share/figlet/{sel_font_file}.flf"
            os.system("pkg install figlet -y > /dev/null 2>&1") # Silent install
            
            if not os.path.exists(path):
                os.system(f"wget -q http://www.figlet.org/fonts/{sel_font_file}.flf -O {path}")
                if not os.path.exists(path) or os.path.getsize(path) < 100:
                     os.system(f"wget -q https://github.com/xero/figlet-fonts/raw/master/{sel_font_file}.flf -O {path}")
            
            os.system(f'figlet -f {sel_font_file} -w {width} -c "{name}"')
            
        print(f"{RESET}")
        
        print(f"{TC}║{' '*(width-2)}║")
        print(f"{TC}╚{'═'*(width-2)}╝{RESET}")
        
        print(f"\n {R}[?] {Y}INSTALL THIS LAYOUT? {R}(y/n)")
        confirm = input(f" {TC}└─➤ {W}").strip().lower()
        if confirm == 'y': break

    # --- INSTALLATION ---
    clear()
    
    if system_os == "Windows":
        print(f"\n{TC}[*] SIMULATION COMPLETE!{RESET}")
        print(f"{G}[✔] The code works perfectly.{RESET}")
        print(f"{Y}[!] Transfer this file to Termux to apply the dashboard.{RESET}\n")
        return # Stop here on Windows

    print(f"\n{TC}[*] INSTALLING PREMIUM DASHBOARD...{RESET}\n")
    loader("CONFIGURING UI")
    loader("WRITING CONFIG")

    # --- GENERATING .BASHRC ---
    t_code = sel_theme['code']
    
    pass_script = ""
    if password:
        pass_script = f"""
echo -e "\\033[1;31m🔒 SECURE SYSTEM LOCKED"
read -s -p "🔑 ENTER PASSWORD: " pass
echo ""
if [ "$pass" != "{password}" ]; then
    echo -e "\\033[1;31m[!] WRONG PASSWORD. BYE."
    sleep 1
    exit
fi
echo -e "\\033[1;32m[✔] ACCESS GRANTED."
clear
"""

    bashrc_content = f"""
# --- LEVIATHAN PREMIUM DASHBOARD ---
clear

{pass_script}

# --- THEME CONFIG ---
MAIN="\\033[1;{t_code}m"
WHITE="\\033[1;37m"
GRAY="\\033[1;30m"
RED="\\033[1;31m"
RESET="\\033[0m"

PS1='${{MAIN}}┌──(${{RED}}UCA💀PRO${{MAIN}})-[${{WHITE}}\\w${{MAIN}}]\\n${{MAIN}}└─${{WHITE}}\\$$RESET '

COLS=$(tput cols)
DATE=$(date +"%d-%b-%Y")
TIME=$(date +"%I:%M %p")

# --- DRAW HUD ---
echo -e "${{MAIN}}╔$(printf '═%.0s' $(seq 1 $((COLS-2))))╗"
echo -e "${{MAIN}}║ ${{RED}}● ${{WHITE}}SYSTEM: ${{MAIN}}ONLINE   ${{RED}}● ${{WHITE}}USER: ${{MAIN}}{name.upper()}   ${{RED}}● ${{WHITE}}TIME: ${{MAIN}}$TIME"
echo -e "${{MAIN}}╠$(printf '═%.0s' $(seq 1 $((COLS-2))))╣"

echo ""
if [ -f /data/data/com.termux/files/usr/share/figlet/{sel_font_file}.flf ]; then
    echo -e "${{MAIN}}"
    figlet -f {sel_font_file} -w $COLS -c "{name}"
    echo -e "$RESET"
else
    echo -e "${{MAIN}}"
    figlet -w $COLS -c "{name}"
    echo -e "$RESET"
fi

echo -e "${{WHITE}}"
MSG=">>> SYSTEM CREATED BY Mr.LEVIATHAN <<<"
printf "%*s\\n" $(( (${{#COLS}} + ${{#MSG}}) / 2)) "$MSG"
echo -e "$RESET"

echo -e "${{MAIN}}╚$(printf '═%.0s' $(seq 1 $((COLS-2))))╝$RESET"
echo ""

alias cls='clear'
alias update='pkg update && pkg upgrade'
alias uca='python banner.py'
"""

    home = os.environ.get('HOME', '/data/data/com.termux/files/home')
    path = os.path.join(home, '.bashrc')
    
    if os.path.exists(path): os.system(f"cp {path} {path}.bak")
    
    with open(path, 'w') as f:
        f.write(bashrc_content)
        
    clear()
    print(f"\n{TC}╔══════════════════════════════════════════╗")
    print(f"{TC}║ {W}  SETUP COMPLETED SUCCESSFULLY!           {TC}║")
    print(f"{TC}║ {W}  PLEASE RESTART TERMUX NOW.              {TC}║")
    print(f"{TC}╚══════════════════════════════════════════╝{RESET}\n")

if __name__ == "__main__":
    main()
