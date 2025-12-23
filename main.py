import os
import time
import sys
import shutil
import platform
import random

# Tool: UCA-Dashboard-Ultimate
# Author: Mr.LEVIATHAN
# Description: Intro Animation, 5-Step Loader & Visual Preview

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

# Check Pyfiglet for Windows Preview
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

# --- 1. INTRO BOOT ANIMATION ---
def intro_animation():
    clear()
    cols = get_cols()
    print(f"\n{BK} [INIT] ESTABLISHING CONNECTION TO UCA SERVER...{RESET}")
    time.sleep(0.5)
    
    # Fake Matrix Rain / Boot Log
    logs = [
        "LOADING_KERNEL_MODULES",
        "VERIFYING_USER_PERMISSIONS",
        "FETCHING_THEME_DATABASE",
        "OPTIMIZING_GRAPHIC_INTERFACE",
        "ACCESS_GRANTED_UCA_CORE"
    ]
    
    for log in logs:
        sys.stdout.write(f"\r {C}:: SYSTEM_BOOT >> {log:<30} {Y}[WAIT]")
        time.sleep(0.2)
        sys.stdout.write(f"\r {C}:: SYSTEM_BOOT >> {log:<30} {G}[OK]  \n")
        time.sleep(0.1)
    
    time.sleep(0.5)
    clear()

# --- 2. SETUP LOADING ANIMATION (5 STEPS) ---
def install_loaders():
    clear()
    print(f"\n{G}[*] INITIALIZING INSTALLATION PROTOCOLS...{RESET}\n")
    time.sleep(0.5)
    
    steps = [
        "CONFIGURING DASHBOARD LAYOUT",
        "DOWNLOADING HIGH-RES ASSETS",
        "INJECTING BASH CONFIGURATION",
        "OPTIMIZING PERFORMANCE",
        "FINALIZING SYSTEM VERIFICATION"
    ]
    
    for step in steps:
        # Animation for each step
        for i in range(4):
            chars = "/-\|"
            sys.stdout.write(f"\r {C}[PROCESS] {step}... {Y}{chars[i]} ")
            sys.stdout.flush()
            time.sleep(0.1)
        
        # Done status
        sys.stdout.write(f"\r {C}[PROCESS] {step:<35} {G}[DONE] \n")
        time.sleep(0.2)
    
    print(f"\n{BK} [LOG] SYSTEM REBOOT REQUIRED...{RESET}")
    time.sleep(1)
    clear()


# --- HEADER ART ---
def print_uca_header():
    logo = f"""
{C}██╗   ██╗ ██████╗ ██████╗ 
{C}██║   ██║██╔════╝██╔══██╗   {Y}[ UCA TERMINAL PRO ]
{C}██║   ██║██║     ███████║
{C}██║   ██║██║     ██╔══██║   {R}OWNER : Mr.LEVIATHAN
{C}╚██████╔╝╚██████╗██║  ██║   {G}STATUS: ONLINE
{C} ╚═════╝  ╚═════╝╚═╝  ╚═╝
"""
    print(logo)
    print(f"{BK}========================================{RESET}")

# --- FONT DATABASE ---
font_db = [
    ("Bloody", "bloody"), ("Ansi Shadow", "ansi_shadow"), ("Graffiti", "graffiti"),
    ("Electronic", "electronic"), ("Sub-Zero", "sub-zero"), ("Calvin S", "calvin_s"),
    ("Slant", "slant"), ("Rectangles", "rectangles"), ("Larry 3D", "larry3d"),
    ("Delta Corps", "delta_corps_priest_1"), ("Standard", "standard"), ("Big", "big"),
    ("Script", "script"), ("Doom", "doom"), ("Speed", "speed"),
    ("Alligator", "alligator"), ("Cyber Large", "cyberlarge"), ("Digital", "digital"),
    ("Epic", "epic"), ("Fender", "fender"), ("Ghost", "ghost"),
    ("Isometric1", "isometric1"), ("Isometric2", "isometric2"), ("Hollywood", "hollywood"),
    ("Invita", "invita"), ("Kban", "kban"), ("Lean", "lean"),
    ("Letters", "letters"), ("Linux", "linux"), ("Lockergnome", "lockergnome"),
    ("Madrid", "madrid"), ("Marquee", "marquee"), ("Maxfour", "maxfour"),
    ("Mike", "mike"), ("Mini", "mini"), ("Mirror", "mirror"),
    ("NancyJ", "nancyj"), ("Nipples", "nipples"), ("Ogre", "ogre"),
    ("Pawp", "pawp"), ("Peaks", "peaks"), ("Poison", "poison"),
    ("Puffy", "puffy"), ("Pyramid", "pyramid"), ("Relief", "relief"),
    ("Roman", "roman"), ("Rot13", "rot13"), ("Rounded", "rounded"),
    ("Rowan Cap", "rowancap"), ("Serif Cap", "serifcap")
]

# --- REAL PREVIEW FUNCTION ---
def show_preview(name, font_file, font_name):
    clear()
    cols = get_cols()
    
    # 1. INFO PANEL (TOP)
    print(f"{C}╔{'═'*(cols-2)}╗")
    print(f"{C}║ {P}PREVIEW MODE  {R}●  {W}STYLE: {Y}{font_name.upper()} {C}".center(cols+18))
    print(f"{C}╠{'═'*(cols-2)}╣")
    
    # 2. BANNER GENERATION (MIDDLE)
    print(f"{C}╚{'═'*(cols-2)}╝{RESET}") 
    print("") 
    
    if system_os == "Windows":
        if pyfiglet:
            try:
                # Windows Preview Logic
                f_map = {
                    "bloody": "larry3d", "ansi_shadow": "doom", "electronic": "computer",
                    "sub-zero": "slant", "calvin_s": "block", "graffiti": "graffiti"
                }
                use_font = f_map.get(font_file, font_file)
                if use_font not in pyfiglet.FigletFont.getFonts():
                    use_font = "standard"
                
                art = pyfiglet.figlet_format(name, font=use_font, justify="center", width=cols)
                print(f"{C}{art}{RESET}")
            except Exception as e:
                print(f"{R}[!] Font render error: {e}{RESET}")
        else:
            print(f"{R}[!] INSTALL PYFIGLET TO SEE VISUAL PREVIEW (pip install pyfiglet){RESET}")

    else:
        # TERMUX PREVIEW LOGIC
        path = f"/data/data/com.termux/files/usr/share/figlet/{font_file}.flf"
        # Download if missing (Lazy Load)
        if not os.path.exists(path):
             print(f"{BK}Downloading font assets...{RESET}")
             os.system(f"wget -q http://www.figlet.org/fonts/{font_file}.flf -O {path}")
             if not os.path.exists(path) or os.path.getsize(path) < 100:
                  os.system(f"wget -q https://github.com/xero/figlet-fonts/raw/master/{font_file}.flf -O {path}")
                  if font_file == "ansi_shadow": os.system(f"wget -q https://github.com/xero/figlet-fonts/raw/master/ANSI%20Shadow.flf -O {path}")

        # Render Real Art
        os.system(f'figlet -f {font_file} -w {cols} -c "{name}" | lolcat')

    print("") # Spacer

    # 3. FOOTER PANEL
    print(f"{C}╔{'═'*(cols-2)}╗")
    print(f"{C}║{f'{Y}>>> Made By Mr.LEVIATHAN <<<'.center(cols+8)}{C}║")
    print(f"{C}╚{'═'*(cols-2)}╝{RESET}")

# --- MAIN ---
def main():
    # 1. INTRO ANIMATION
    intro_animation()

    print_uca_header()

    print(f"\n {C}┌──[ {P}IDENTITY {C}]")
    try:
        name = input(f" {C}└─➤ {Y}ENTER NAME :: {W}").strip()
    except: name = "LEVIATHAN"
    if not name: name = "LEVIATHAN"

    while True:
        clear()
        print_uca_header()
        print(f"{G} [✔] USER: {W}{name.upper()}{RESET}\n")
        
        # Menu
        rows = (len(font_db) // 3) + 1
        for i in range(rows):
            idx1, idx2, idx3 = i, i + rows, i + (rows * 2)
            s1 = f"{C}[{idx1+1:02}] {W}{font_db[idx1][0]:<14}" if idx1 < len(font_db) else ""
            s2 = f"{C}[{idx2+1:02}] {W}{font_db[idx2][0]:<14}" if idx2 < len(font_db) else ""
            s3 = f"{C}[{idx3+1:02}] {W}{font_db[idx3][0]:<14}" if idx3 < len(font_db) else ""
            print(f" {s1} {s2} {s3}")

        print(f"\n {C}┌──[ {P}CONFIG {C}]")
        try:
            choice = int(input(f" {C}└─➤ {Y}SELECT ID :: {W}"))
            if 1 <= choice <= len(font_db):
                sel_name, sel_file = font_db[choice-1]
            else:
                sel_name, sel_file = font_db[0]
        except:
            sel_name, sel_file = font_db[0]

        # SHOW THE REAL PREVIEW
        show_preview(name, sel_file, sel_name)
        
        print(f"\n {R}[?] {Y}ACTIVATE DASHBOARD? {R}(y/n)")
        confirm = input(f" {C}└─➤ {W}").strip().lower()
        
        if confirm == 'y':
            # 2. RUN INSTALL LOADERS IF CONFIRMED
            install_loaders()
            break

    # --- BASHRC INSTALL ---
    bashrc_content = f"""
# --- UCA SYSTEM ---
clear
PS1='\\[\\033[1;36m\\]┌──(\\[\\033[1;31m\\]UCA💀Termux\\[\\033[1;36m\\])-[\\[\\033[1;37m\\]\\w\\[\\033[1;36m\\]]\\n\\[\\033[1;36m\\]└─\\[\\033[1;33m\\]$\\[\\033[0m\\] '
COLS=$(tput cols)
C="\\033[1;36m"
R="\\033[1;31m"
W="\\033[1;37m"
Y="\\033[1;33m"
G="\\033[1;32m"
BK="\\033[1;30m"
RESET="\\033[0m"

# Top Bar
printf "$C╔"
for ((i=1; i<=COLS-2; i++)); do printf "═"; done
printf "╗\\n"
printf "$C║ $R● $W UCA TERMINAL $R● $C USER: $Y{name.upper()}"
printf "\\n"
printf "$C╠"
for ((i=1; i<=COLS-2; i++)); do printf "═"; done
printf "╣\\n"
DATE=$(date +"%d-%m")
printf "$C║ $BK[NET]: $G SECURE  $BK[IP]: $G HIDDEN  $BK[DATE]: $W $DATE"
printf "\\n"

# Banner
echo ""
echo -e "$C"
figlet -f {sel_file} -w $COLS -c "{name}"
echo -e "$RESET"

# Footer
echo -e "$Y"
MSG=">>> Made By Mr.LEVIATHAN <<<"
printf "%*s\\n" $(( (${{#COLS}} + ${{#MSG}}) / 2)) "$MSG"
echo -e "$RESET"
printf "$C╚"
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
        
        # 3. SUCCESS MESSAGE
        print(f"\n{R}╔══════════════════════════════════════════╗")
        print(f"{R}║ {G}  SETUP SUCCESSFUL! RESTART TERMUX NOW.   {R}║")
        print(f"{R}╚══════════════════════════════════════════╝{RESET}\n")

if __name__ == "__main__":
    main()
