import os
import time
import sys
import shutil
import platform
import random

# Tool: UCA-TERMINAL-PRO
# Author: Mr.LEVIATHAN
# Version: 11.0 (Final)

# --- COLORS ---
R = '\033[1;31m'  # Red
G = '\033[1;32m'  # Green
C = '\033[1;36m'  # Cyan
Y = '\033[1;33m'  # Yellow
P = '\033[1;35m'  # Purple
W = '\033[1;37m'  # White
BK = '\033[1;30m' # Black
RESET = '\033[0m'

system_os = platform.system()

# Check Pyfiglet
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

# --- DEPENDENCY CHECK ---
def check_deps():
    if system_os != "Windows":
        pkgs = ["figlet", "wget", "termux-api"]
        for p in pkgs:
            if os.system(f"command -v {p} > /dev/null 2>&1") != 0:
                print(f"{Y}[*] INSTALLING {p.upper()}...{RESET}")
                os.system(f"pkg install {p} -y > /dev/null 2>&1")

# --- THEMES ---
THEMES = {
    1: {"name": "NEON CYAN",   "main": "\033[1;36m", "accent": "\033[1;33m", "text": "\033[1;37m", "alert": "\033[1;31m"},
    2: {"name": "MATRIX GREEN","main": "\033[1;32m", "accent": "\033[1;37m", "text": "\033[1;32m", "alert": "\033[1;33m"},
    3: {"name": "CYBER RED",   "main": "\033[1;31m", "accent": "\033[1;33m", "text": "\033[1;37m", "alert": "\033[1;36m"},
    4: {"name": "ROYAL GOLD",  "main": "\033[1;33m", "accent": "\033[1;36m", "text": "\033[1;37m", "alert": "\033[1;31m"},
    5: {"name": "DEEP PURPLE", "main": "\033[1;35m", "accent": "\033[1;36m", "text": "\033[1;37m", "alert": "\033[1;31m"}
}

# --- HEADER (YOUR LOGO) ---
def print_uca_header():
    logo = f"""
{C}██╗   ██╗ ██████╗ ██████╗ 
{C}██║   ██║██╔════╝██╔══██╗   {Y}[ UCA TERMINAL PRO ]
{C}██║   ██║██║     ███████║
{C}██║   ██║██║     ██╔══██║   {R}OWNER : Mr.LEVIATHAN
{C}╚██████╔╝╚██████╗██║  ██║   {G}STATUS: ONLINE
{C} ╚═════╝  ╚═════╝╚═╝  ╚═╝{RESET}
"""
    print(logo)
    print(f"{BK}========================================{RESET}")

# --- INTRO ---
def intro():
    clear()
    print(f"\n{BK} [SYSTEM] CONNECTING TO UCA CORE...{RESET}")
    time.sleep(1)
    logs = ["ENCRYPTING_CONNECTION", "LOADING_MODULES", "VERIFYING_ACCESS", "LAUNCHING_INTERFACE"]
    for log in logs:
        sys.stdout.write(f"\r {C}:: PROCESS >> {log:<25} {Y}[WAIT]")
        time.sleep(0.2)
        sys.stdout.write(f"\r {C}:: PROCESS >> {log:<25} {G}[OK]  \n")
    clear()

# --- FONT DB ---
font_db = [
    ("Bloody", "bloody"), ("Ansi Shadow", "ansi_shadow"), ("Graffiti", "graffiti"),
    ("Electronic", "electronic"), ("Sub-Zero", "sub-zero"), ("Calvin S", "calvin_s"),
    ("Slant", "slant"), ("Rectangles", "rectangles"), ("Larry 3D", "larry3d"),
    ("Delta Corps", "delta_corps_priest_1"), ("Standard", "standard"), ("Big", "big"),
    ("Script", "script"), ("Doom", "doom"), ("Speed", "speed"),
    ("Alligator", "alligator"), ("Cyber Large", "cyberlarge"), ("Digital", "digital"),
    ("Epic", "epic"), ("Fender", "fender"), ("Ghost", "ghost"),
    ("Isometric1", "isometric1"), ("Hollywood", "hollywood"), ("Invita", "invita"), 
    ("Letters", "letters"), ("Linux", "linux"), ("Marquee", "marquee"), ("Maxfour", "maxfour"),
    ("Mike", "mike"), ("Mini", "mini"), ("Mirror", "mirror"), ("Ogre", "ogre"),
    ("Pawp", "pawp"), ("Peaks", "peaks"), ("Poison", "poison"), ("Puffy", "puffy"), 
    ("Pyramid", "pyramid"), ("Relief", "relief"), ("Roman", "roman"), ("Rot13", "rot13"), 
    ("Rounded", "rounded"), ("Rowan Cap", "rowancap"), ("Serif Cap", "serifcap")
]

# --- PREVIEW ---
def show_preview(name, font_file, font_name, theme_id):
    clear()
    cols = get_cols()
    th = THEMES[theme_id]
    MC, AC, TC, RC = th["main"], th["accent"], th["text"], th["alert"]
    
    print(f"{MC}╔{'═'*(cols-2)}╗")
    status = f"{RC}● {TC}SYSTEM: {MC}ONLINE   {RC}● {TC}STYLE: {AC}{font_name.upper()}"
    print(f"{MC}║{status.center(cols+25)}{MC}║")
    print(f"{MC}╠{'═'*(cols-2)}╣")
    print(f"{MC}║{' '*(cols-2)}║")
    
    if system_os == "Windows":
        if pyfiglet:
            try:
                f_map = {"bloody": "larry3d", "ansi_shadow": "doom", "electronic": "computer", "sub-zero": "slant"}
                use_font = f_map.get(font_file, "standard")
                art = pyfiglet.figlet_format(name, font=use_font, justify="center", width=cols)
                print(f"{MC}{art}{RESET}")
            except: print(f"{RC}[PREVIEW ERROR]{RESET}")
        else: print(f"{RC}[INSTALL PYFIGLET]{RESET}")
    else:
        path = f"/data/data/com.termux/files/usr/share/figlet/{font_file}.flf"
        if not os.path.exists(path):
             os.system(f"wget -q http://www.figlet.org/fonts/{font_file}.flf -O {path}")
             if not os.path.exists(path) or os.path.getsize(path) < 100:
                 os.system(f"wget -q https://github.com/xero/figlet-fonts/raw/master/{font_file}.flf -O {path}")
                 if font_file == "ansi_shadow": os.system(f"wget -q https://github.com/xero/figlet-fonts/raw/master/ANSI%20Shadow.flf -O {path}")
        print(f"{MC}")
        os.system(f'figlet -f {font_file} -w {cols} -c "{name}"') 
        print(f"{RESET}")

    print(f"{MC}║{' '*(cols-2)}║")
    print(f"{MC}╚{'═'*(cols-2)}╝{RESET}")

# --- MAIN ---
def main():
    check_deps()
    intro()
    print_uca_header()

    # 1. Identity
    try:
        print(f" {C}┌──[ {Y}IDENTITY {C}]")
        name = input(f" {C}└─➤ {W}ENTER USERNAME :: {Y}").strip()
    except: name = "LEVIATHAN"
    if not name: name = "LEVIATHAN"

    # 2. Security
    print(f"\n {C}┌──[ {Y}SECURITY {C}]")
    print(f" {C}│ {R}Leave empty for no password.")
    password = input(f" {C}└─➤ {W}SET PASSWORD :: {Y}").strip()

    # 3. Theme
    print(f"\n {C}┌──[ {Y}THEME {C}]")
    for k, v in THEMES.items():
        print(f" {C}│ {v['main']}[{k}] {v['name']}{RESET}")
    try:
        t_choice = int(input(f" {C}└─➤ {W}SELECT ID :: {Y}"))
        if t_choice not in THEMES: t_choice = 1
    except: t_choice = 1

    # Loop
    while True:
        clear()
        th = THEMES[t_choice]
        print_uca_header()
        print(f"{th['main']} [ USER: {name.upper()} ]{RESET}\n")
        
        # Menu
        rows = (len(font_db) // 3) + 1
        for i in range(rows):
            i1, i2, i3 = i, i+rows, i+(rows*2)
            s1 = f"{th['main']}[{i1+1:02}] {th['text']}{font_db[i1][0]:<14}" if i1 < len(font_db) else ""
            s2 = f"{th['main']}[{i2+1:02}] {th['text']}{font_db[i2][0]:<14}" if i2 < len(font_db) else ""
            s3 = f"{th['main']}[{i3+1:02}] {th['text']}{font_db[i3][0]:<14}" if i3 < len(font_db) else ""
            print(f" {s1} {s2} {s3}")

        print(f"\n {th['main']}┌──[ {th['accent']}CONFIG {th['main']}]")
        try:
            choice = int(input(f" {th['main']}└─➤ {th['text']}ENTER ID :: {th['accent']}"))
            if 1 <= choice <= len(font_db):
                sel_name, sel_file = font_db[choice-1]
            else: sel_name, sel_file = font_db[0]
        except: sel_name, sel_file = font_db[0]

        show_preview(name, sel_file, sel_name, t_choice)
        
        print(f"\n {th['alert']}[?] {th['accent']}CONFIRM? {th['alert']}(y/n)")
        confirm = input(f" {th['main']}└─➤ {th['text']}").strip().lower()
        if confirm == 'y': break

    # --- INSTALL ---
    clear()
    th = THEMES[t_choice]
    print(f"\n{th['main']}[*] INSTALLING LEVIATHAN OS...{RESET}\n")
    time.sleep(1)
    
    steps = ["ENCRYPTING_DATA", "CONFIGURING_VOICE", "FINALIZING_HUD", "SYSTEM_REBOOT"]
    for step in steps:
        for x in "|/-\\":
            sys.stdout.write(f"\r {th['accent']}:: {step} ... {th['main']}[{x}]")
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f"\r {th['accent']}:: {step} ... {th['text']}[OK]   \n")

    # --- BASHRC ---
    MC, AC, TC, RC = th['main'].replace('[','\\['), th['accent'].replace('[','\\['), th['text'].replace('[','\\['), th['alert'].replace('[','\\[')
    
    pass_script = ""
    if password:
        pass_script = f"""
echo -e "{RC}🔒 SYSTEM LOCKED"
read -s -p "🔑 ENTER KEY: " input_pass
echo ""
if [ "$input_pass" != "{password}" ]; then
    echo -e "{RC}ACCESS DENIED."
    sleep 1
    exit
fi
echo -e "{MC}ACCESS GRANTED."
clear
"""

    bashrc_content = f"""
# --- UCA TERMINAL PRO ---
clear
{pass_script}

# Voice
if command -v termux-tts-speak &> /dev/null; then
    termux-tts-speak "Welcome back {name}. System Online." &
fi

PS1='{MC}┌──({RC}UCA💀PRO{MC})-[{TC}\\w{MC}]\\n{MC}└─{AC}\\${RESET} '
COLS=$(tput cols)
DATE=$(date +"%I:%M %p")
BAT="N/A"
if command -v termux-battery-status &> /dev/null; then
    BAT=$(termux-battery-status | grep percentage | awk -F': ' '{{print $2}}' | tr -d ',')00
fi

printf "{MC}╔"
for ((i=1; i<=COLS-2; i++)); do printf "═"; done
printf "╗\\n"

printf "{MC}║ {RC}● {TC}USER: {MC}{name.upper()}   {RC}● {TC}TIME: {MC}$DATE   {RC}● {TC}BAT: {MC}$BAT"
printf "\\n"

printf "{MC}╠"
for ((i=1; i<=COLS-2; i++)); do printf "═"; done
printf "╣\\n"

echo ""
echo -e "{MC}"
figlet -f {sel_file} -w $COLS -c "{name}"
echo -e "{RESET}"

echo -e "{AC}"
MSG=">>> SYSTEM SECURE | MADE BY Mr.LEVIATHAN <<<"
printf "%*s\\n" $(( (${{#COLS}} + ${{#MSG}}) / 2)) "$MSG"
echo -e "{RESET}"

printf "{MC}╚"
for ((i=1; i<=COLS-2; i++)); do printf "═"; done
printf "╝\\n"
echo ""

alias cls='clear'
alias update='pkg update && pkg upgrade'
"""

    if system_os != "Windows":
        home = os.environ.get('HOME', '/data/data/com.termux/files/home')
        path = os.path.join(home, '.bashrc')
        if os.path.exists(path): os.system(f"cp {path} {path}.bak")
        with open(path, 'w') as f: f.write(bashrc_content)
        
        clear()
        print(f"\n{th['alert']}╔══════════════════════════════════════════╗")
        print(f"{th['alert']}║ {th['text']}  INSTALLATION SUCCESSFUL!                {th['alert']}║")
        print(f"{th['alert']}║ {th['text']}  RESTART TERMUX TO START UCA SYSTEM      {th['alert']}║")
        print(f"{th['alert']}╚══════════════════════════════════════════╝{RESET}\n")

if __name__ == "__main__":
    main()
