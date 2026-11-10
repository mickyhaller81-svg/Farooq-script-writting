import os
OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 900
SKIN = "#e0ac7e"; SKIN2 = "#d39b6a"

def face(cx, cy, r, mood, female=False):
    s = []
    # eyes
    ex = r*0.38; ey = cy - r*0.05
    if mood == "tired":
        for d in (-1, 1):
            s.append(f'<path d="M{cx+d*ex-r*0.16},{ey} q{r*0.16},{r*0.1} {r*0.32},0" stroke="#222" stroke-width="{r*0.07}" fill="none"/>')
            s.append(f'<path d="M{cx+d*ex-r*0.15},{ey+r*0.15} q{r*0.15},{r*0.08} {r*0.3},0" stroke="#8a6a8a" stroke-width="{r*0.05}" fill="none" opacity=".7"/>')
    else:
        for d in (-1, 1):
            s.append(f'<circle cx="{cx+d*ex}" cy="{ey}" r="{r*0.09}" fill="#222"/>')
    # brows
    if mood == "angry":
        for d in (-1, 1):
            s.append(f'<line x1="{cx+d*ex*1.5}" y1="{ey-r*0.32}" x2="{cx+d*ex*0.4}" y2="{ey-r*0.18}" stroke="#222" stroke-width="{r*0.09}" stroke-linecap="round"/>')
    elif mood in ("sad", "tired"):
        for d in (-1, 1):
            s.append(f'<line x1="{cx+d*ex*1.4}" y1="{ey-r*0.2}" x2="{cx+d*ex*0.5}" y2="{ey-r*0.32}" stroke="#222" stroke-width="{r*0.07}" stroke-linecap="round"/>')
    elif mood == "smug":
        s.append(f'<line x1="{cx-ex*1.4}" y1="{ey-r*0.28}" x2="{cx-ex*0.5}" y2="{ey-r*0.3}" stroke="#222" stroke-width="{r*0.07}" stroke-linecap="round"/>')
        s.append(f'<line x1="{cx+ex*1.4}" y1="{ey-r*0.4}" x2="{cx+ex*0.5}" y2="{ey-r*0.3}" stroke="#222" stroke-width="{r*0.07}" stroke-linecap="round"/>')
    # mouth
    my = cy + r*0.42
    if mood == "happy":
        s.append(f'<path d="M{cx-r*0.3},{my-r*0.08} q{r*0.3},{r*0.3} {r*0.6},0" stroke="#7a2a2a" stroke-width="{r*0.08}" fill="#b9474b"/>')
    elif mood == "angry":
        s.append(f'<ellipse cx="{cx}" cy="{my}" rx="{r*0.2}" ry="{r*0.14}" fill="#7a1f24"/>')
    elif mood == "smug":
        s.append(f'<path d="M{cx-r*0.25},{my} q{r*0.3},{r*0.1} {r*0.5},{-r*0.12}" stroke="#7a2a2a" stroke-width="{r*0.08}" fill="none" stroke-linecap="round"/>')
    else:
        s.append(f'<path d="M{cx-r*0.25},{my+r*0.06} q{r*0.25},{-r*0.18} {r*0.5},0" stroke="#5a2a2a" stroke-width="{r*0.08}" fill="none" stroke-linecap="round"/>')
    if female:
        s.append(f'<circle cx="{cx-r*0.55}" cy="{cy+r*0.2}" r="{r*0.12}" fill="#e88" opacity=".5"/><circle cx="{cx+r*0.55}" cy="{cy+r*0.2}" r="{r*0.12}" fill="#e88" opacity=".5"/>')
    return "".join(s)

def man(x, y, k=1.0, mood="tired", shirt="#dfe8f2", tie="#2b4a7a", pants="#3a3f4a", slump=True, arm="down"):
    """x,y = feet center. ~ 300px tall at k=1"""
    g = [f'<g transform="translate({x},{y}) scale({k})">']
    sh = 12 if slump else 0
    g.append(f'<rect x="-30" y="-140" width="24" height="140" rx="8" fill="{pants}"/><rect x="6" y="-140" width="24" height="140" rx="8" fill="{pants}"/>')
    g.append('<ellipse cx="-18" cy="-2" rx="20" ry="8" fill="#222"/><ellipse cx="18" cy="-2" rx="20" ry="8" fill="#222"/>')
    g.append(f'<path d="M-42,-130 L-46,{-240+sh} Q0,{-262+sh} 46,{-240+sh} L42,-130 Z" fill="{shirt}" stroke="#9aa8b8" stroke-width="2"/>')
    g.append(f'<path d="M0,{-248+sh} l-7,12 l7,70 l7,-70 z" fill="{tie}"/>')
    if arm == "down":
        g.append(f'<path d="M-44,{-232+sh} q-22,50 -16,110" stroke="{shirt}" stroke-width="20" fill="none" stroke-linecap="round"/><circle cx="-60" cy="-118" r="10" fill="{SKIN}"/>')
        g.append(f'<path d="M44,{-232+sh} q22,50 16,110" stroke="{shirt}" stroke-width="20" fill="none" stroke-linecap="round"/><circle cx="60" cy="-118" r="10" fill="{SKIN}"/>')
    elif arm == "hold":  # both hands forward (holding kids' hands)
        g.append(f'<path d="M-44,{-232+sh} q-30,40 -50,90" stroke="{shirt}" stroke-width="20" fill="none" stroke-linecap="round"/><circle cx="-96" cy="-148" r="10" fill="{SKIN}"/>')
        g.append(f'<path d="M44,{-232+sh} q30,40 50,90" stroke="{shirt}" stroke-width="20" fill="none" stroke-linecap="round"/><circle cx="96" cy="-148" r="10" fill="{SKIN}"/>')
    elif arm == "head":  # hand on forehead
        g.append(f'<path d="M-44,{-232+sh} q-22,50 -16,110" stroke="{shirt}" stroke-width="20" fill="none" stroke-linecap="round"/><circle cx="-60" cy="-118" r="10" fill="{SKIN}"/>')
        g.append(f'<path d="M44,{-232+sh} q30,-20 -6,-68" stroke="{shirt}" stroke-width="20" fill="none" stroke-linecap="round"/><circle cx="34" cy="{-305+sh}" r="11" fill="{SKIN}"/>')
    hy = -290 + sh
    g.append(f'<rect x="-9" y="{hy+30}" width="18" height="18" fill="{SKIN2}"/>')
    g.append(f'<circle cx="0" cy="{hy}" r="40" fill="{SKIN}"/>')
    g.append(f'<path d="M-40,{hy-4} Q-42,{hy-48} 0,{hy-46} Q42,{hy-48} 40,{hy-4} Q30,{hy-28} 0,{hy-30} Q-30,{hy-28} -40,{hy-4}Z" fill="#1d1a18"/>')
    # moustache
    g.append(f'<path d="M-14,{hy+12} q14,-6 28,0 q-14,6 -28,0" fill="#1d1a18"/>')
    g.append(face(0, hy+2, 40, mood))
    if arm == "head":
        g.append(f'<circle cx="34" cy="{hy-15}" r="11" fill="{SKIN}"/>')
    g.append('</g>')
    return "".join(g)

def woman(x, y, k=1.0, mood="angry", kameez="#c2185b", dupatta="#f8bbd0", pose="point", sit=False):
    g = [f'<g transform="translate({x},{y}) scale({k})">']
    if not sit:
        g.append('<rect x="-26" y="-80" width="22" height="80" rx="6" fill="#f3e5f5"/><rect x="4" y="-80" width="22" height="80" rx="6" fill="#f3e5f5"/>')
        g.append('<ellipse cx="-16" cy="-2" rx="16" ry="6" fill="#b8860b"/><ellipse cx="16" cy="-2" rx="16" ry="6" fill="#b8860b"/>')
        g.append(f'<path d="M-36,-232 Q0,-250 36,-232 L54,-70 Q0,-58 -54,-70 Z" fill="{kameez}"/>')
        g.append('<path d="M-30,-110 q30,10 60,0" stroke="#ffd54f" stroke-width="4" fill="none"/>')
    else:
        g.append(f'<path d="M-36,-162 Q0,-180 36,-162 L46,-60 L-46,-60 Z" fill="{kameez}"/>')
        g.append('<rect x="-46" y="-72" width="110" height="30" rx="12" fill="#f3e5f5"/><rect x="40" y="-72" width="24" height="72" rx="8" fill="#f3e5f5"/>')
    top = -232 if not sit else -162
    g.append(f'<path d="M-38,{top+4} q-10,90 -4,170" stroke="{dupatta}" stroke-width="16" fill="none" opacity=".9"/>')
    if pose == "point":
        g.append(f'<path d="M36,{top+10} q50,10 80,-10" stroke="{kameez}" stroke-width="18" fill="none" stroke-linecap="round"/><circle cx="120" cy="{top-2}" r="9" fill="{SKIN}"/><line x1="124" y1="{top-6}" x2="140" y2="{top-14}" stroke="{SKIN}" stroke-width="6" stroke-linecap="round"/>')
        g.append(f'<path d="M-36,{top+10} q-20,40 -8,80" stroke="{kameez}" stroke-width="18" fill="none" stroke-linecap="round"/><circle cx="-42" cy="{top+92}" r="9" fill="{SKIN}"/>')
    elif pose == "phone":
        g.append(f'<path d="M36,{top+10} q30,40 -6,60" stroke="{kameez}" stroke-width="18" fill="none" stroke-linecap="round"/><circle cx="26" cy="{top+70}" r="9" fill="{SKIN}"/>')
        g.append(f'<rect x="10" y="{top+36}" width="26" height="42" rx="5" fill="#222"/><rect x="13" y="{top+40}" width="20" height="32" fill="#7fd3ff"/>')
        g.append(f'<path d="M-36,{top+10} q-20,40 -8,80" stroke="{kameez}" stroke-width="18" fill="none" stroke-linecap="round"/><circle cx="-42" cy="{top+92}" r="9" fill="{SKIN}"/>')
    elif pose == "bags":
        g.append(f'<path d="M36,{top+10} q24,50 26,100" stroke="{kameez}" stroke-width="18" fill="none" stroke-linecap="round"/><circle cx="62" cy="{top+112}" r="9" fill="{SKIN}"/>')
        g.append(f'<path d="M-36,{top+10} q-24,50 -26,100" stroke="{kameez}" stroke-width="18" fill="none" stroke-linecap="round"/><circle cx="-62" cy="{top+112}" r="9" fill="{SKIN}"/>')
        for bx, col, lab in ((62, "#ff7043", "SALE"), (110, "#ab47bc", "LUXE"), (-62, "#26a69a", "BRAND"), (-110, "#ffca28", "GOLD")):
            g.append(f'<path d="M{bx-12},{top+112} q12,-24 24,0" stroke="#333" stroke-width="3" fill="none"/>')
            g.append(f'<rect x="{bx-22}" y="{top+112}" width="44" height="54" rx="4" fill="{col}" stroke="#333" stroke-width="2"/>')
            g.append(f'<text x="{bx}" y="{top+145}" font-size="11" font-weight="700" text-anchor="middle" fill="#fff" font-family="Arial">{lab}</text>')
    hy = top - 46
    g.append(f'<rect x="-8" y="{hy+28}" width="16" height="20" fill="{SKIN2}"/>')
    g.append(f'<path d="M-44,{hy-6} Q-46,{hy+60} -30,{hy+80} L30,{hy+80} Q46,{hy+60} 44,{hy-6} Z" fill="#1d1a18"/>')
    g.append(f'<circle cx="0" cy="{hy}" r="38" fill="{SKIN}"/>')
    g.append(f'<path d="M-40,{hy} Q-40,{hy-46} 0,{hy-44} Q40,{hy-46} 40,{hy} Q20,{hy-30} -2,{hy-26} Q-24,{hy-32} -40,{hy}Z" fill="#1d1a18"/>')
    g.append(f'<path d="M-46,{hy+6} Q-50,{hy-60} 0,{hy-58} Q50,{hy-60} 46,{hy+6}" stroke="{dupatta}" stroke-width="10" fill="none" opacity=".9"/>')
    g.append(f'<circle cx="-38" cy="{hy+14}" r="5" fill="#ffd54f"/><circle cx="38" cy="{hy+14}" r="5" fill="#ffd54f"/>')
    g.append(face(0, hy+2, 38, mood, female=True))
    g.append('</g>')
    return "".join(g)

def kid(x, y, k=1.0, shirt="#ff9800", girl=False, mood="happy", arm=None):
    g = [f'<g transform="translate({x},{y}) scale({k})">']
    g.append('<rect x="-16" y="-60" width="13" height="60" rx="5" fill="#455a64"/><rect x="3" y="-60" width="13" height="60" rx="5" fill="#455a64"/>')
    if girl:
        g.append(f'<path d="M-24,-120 L24,-120 L34,-50 L-34,-50 Z" fill="{shirt}"/>')
    else:
        g.append(f'<rect x="-24" y="-122" width="48" height="66" rx="10" fill="{shirt}"/>')
    if arm == "up-left":
        g.append(f'<path d="M-22,-112 q-20,0 -32,-16" stroke="{shirt}" stroke-width="12" fill="none" stroke-linecap="round"/>')
    elif arm == "up-right":
        g.append(f'<path d="M22,-112 q20,0 32,-16" stroke="{shirt}" stroke-width="12" fill="none" stroke-linecap="round"/>')
    g.append('<circle cx="0" cy="-150" r="28" fill="#e0ac7e"/>')
    if girl:
        g.append('<path d="M-29,-150 Q-30,-184 0,-182 Q30,-184 29,-150 Q22,-170 0,-168 Q-22,-170 -29,-150Z" fill="#1d1a18"/><circle cx="-30" cy="-160" r="9" fill="#1d1a18"/><circle cx="30" cy="-160" r="9" fill="#1d1a18"/>')
    else:
        g.append('<path d="M-28,-152 Q-28,-182 0,-180 Q28,-182 28,-152 Q16,-166 0,-164 Q-16,-166 -28,-152Z" fill="#1d1a18"/>')
    g.append(face(0, -150, 28, mood))
    g.append('</g>')
    return "".join(g)

def maid(x, y, k=1.0, tool="broom"):
    g = [f'<g transform="translate({x},{y}) scale({k})">']
    g.append('<rect x="-22" y="-70" width="18" height="70" rx="6" fill="#8d6e63"/><rect x="4" y="-70" width="18" height="70" rx="6" fill="#8d6e63"/>')
    g.append('<path d="M-32,-210 Q0,-224 32,-210 L44,-64 L-44,-64 Z" fill="#5c6bc0"/>')
    g.append('<rect x="-26" y="-150" width="52" height="70" rx="6" fill="#fff" opacity=".85"/>')
    if tool == "broom":
        g.append('<line x1="40" y1="-190" x2="70" y2="10" stroke="#8d5524" stroke-width="7"/><path d="M52,0 L90,0 L84,30 L58,30Z" fill="#c8a165"/>')
        g.append('<path d="M30,-200 q24,20 26,50" stroke="#5c6bc0" stroke-width="16" fill="none" stroke-linecap="round"/><circle cx="56" cy="-148" r="8" fill="#c68b59"/>')
    else:  # tray of tea
        g.append('<path d="M30,-200 q30,20 30,60" stroke="#5c6bc0" stroke-width="16" fill="none" stroke-linecap="round"/><path d="M-30,-200 q-30,20 -30,60" stroke="#5c6bc0" stroke-width="16" fill="none" stroke-linecap="round"/>')
        g.append('<rect x="-75" y="-146" width="150" height="10" rx="4" fill="#bdbdbd"/><rect x="-50" y="-172" width="22" height="26" rx="4" fill="#fff" stroke="#999"/><rect x="20" y="-172" width="22" height="26" rx="4" fill="#fff" stroke="#999"/>')
    g.append('<circle cx="0" cy="-246" r="32" fill="#c68b59"/>')
    g.append('<path d="M-40,-240 Q-40,-292 0,-290 Q40,-292 40,-240 Q40,-200 30,-190 L-30,-190 Q-40,-200 -40,-240" fill="none" stroke="#9fa8da" stroke-width="10"/>')
    g.append(face(0, -244, 32, "tired"))
    g.append('</g>')
    return "".join(g)

def bubble(x, y, w, h, text_lines, tail=(0, 0), color="#fff", border="#222", fs=26, think=False, tc="#111"):
    s = []
    tx, ty = tail
    if think:
        s.append(f'<circle cx="{tx}" cy="{ty}" r="7" fill="{color}" stroke="{border}" stroke-width="3"/>')
        s.append(f'<circle cx="{(tx+x+w/2)/2}" cy="{(ty+y+h)/2}" r="12" fill="{color}" stroke="{border}" stroke-width="3"/>')
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{color}" stroke="{border}" stroke-width="3" stroke-dasharray="2 0"/>')
    else:
        bx = x + w*0.3 if tx < x + w/2 else x + w*0.6
        s.append(f'<path d="M{bx},{y+h-4} L{tx},{ty} L{bx+36},{y+h-4} Z" fill="{color}" stroke="{border}" stroke-width="3" stroke-linejoin="round"/>')
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{color}" stroke="{border}" stroke-width="3"/>')
        s.append(f'<rect x="{bx+3}" y="{y+h-8}" width="31" height="10" fill="{color}"/>')
    n = len(text_lines)
    for i, t in enumerate(text_lines):
        ly = y + h/2 + (i - (n-1)/2) * fs*1.2 + fs*0.35
        s.append(f'<text x="{x+w/2}" y="{ly}" font-size="{fs}" text-anchor="middle" font-family="Comic Sans MS, Chalkboard, Arial" font-weight="700" fill="{tc}">{t}</text>')
    return "".join(s)

def frame(n, title, caption, body, bg_top, bg_bot):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs><linearGradient id="bg{n}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{bg_top}"/><stop offset="1" stop-color="{bg_bot}"/></linearGradient></defs>
<rect width="{W}" height="{H}" fill="url(#bg{n})"/>
{body}
<rect x="0" y="0" width="{W}" height="78" fill="#111"/>
<circle cx="52" cy="39" r="26" fill="#ffca28"/><text x="52" y="49" font-size="30" font-weight="900" text-anchor="middle" font-family="Arial" fill="#111">{n}</text>
<text x="96" y="51" font-size="34" font-weight="800" font-family="Arial" fill="#fff">{title}</text>
<rect x="0" y="{H-110}" width="{W}" height="110" fill="#fffdf5"/><rect x="0" y="{H-110}" width="{W}" height="5" fill="#ffca28"/>
{"".join(f'<text x="{W/2}" y="{H-70+i*36}" font-size="27" text-anchor="middle" font-family="Georgia, serif" font-style="italic" fill="#222">{c}</text>' for i, c in enumerate(caption))}
<rect x="4" y="4" width="{W-8}" height="{H-8}" fill="none" stroke="#111" stroke-width="8"/>
</svg>'''

# ---------- Panel 1: Office ----------
b = []
b.append('<rect x="0" y="560" width="1200" height="230" fill="#9e9e9e"/>')
b.append('<rect x="760" y="120" width="380" height="300" fill="#0d1b3a" stroke="#555" stroke-width="10"/>')
for i in range(9):
    bx = 780 + i*40; bh = 80 + (i*53) % 140
    b.append(f'<rect x="{bx}" y="{420-bh}" width="32" height="{bh}" fill="#263859"/>')
    for wy in range(420-bh+10, 410, 22):
        b.append(f'<rect x="{bx+8}" y="{wy}" width="6" height="8" fill="#ffe082"/>')
b.append('<circle cx="1080" cy="170" r="22" fill="#fff8e1"/>')
b.append('<circle cx="620" cy="190" r="56" fill="#fff" stroke="#333" stroke-width="6"/><line x1="620" y1="190" x2="620" y2="150" stroke="#333" stroke-width="5"/><line x1="620" y1="190" x2="650" y2="200" stroke="#c62828" stroke-width="5"/><text x="620" y="268" text-anchor="middle" font-size="22" font-family="Arial" font-weight="700" fill="#333">9:40 PM</text>')
b.append(man(380, 700, 1.0, mood="tired", arm="head"))
b.append('<rect x="120" y="520" width="700" height="34" fill="#6d4c41"/><rect x="140" y="554" width="660" height="200" fill="#795548"/><rect x="170" y="590" width="200" height="60" rx="6" fill="#8d6e63"/><rect x="570" y="590" width="200" height="60" rx="6" fill="#8d6e63"/><circle cx="270" cy="620" r="6" fill="#4e342e"/><circle cx="670" cy="620" r="6" fill="#4e342e"/>')
b.append('<rect x="0" y="0" width="0" height="0"/><rect x="150" y="554" width="22" height="200" fill="#5d4037"/><rect x="770" y="554" width="22" height="200" fill="#5d4037"/>')
b.append('<rect x="440" y="420" width="180" height="104" rx="6" fill="#37474f"/><rect x="452" y="430" width="156" height="84" fill="#90caf9"/><rect x="420" y="520" width="220" height="10" rx="3" fill="#263238"/>')
b.append('<text x="530" y="470" text-anchor="middle" font-size="16" font-family="Arial" fill="#0d47a1" font-weight="700">REPORT DUE</text><text x="530" y="492" text-anchor="middle" font-size="14" font-family="Arial" fill="#0d47a1">Q4 Targets</text>')
for i in range(6):
    b.append(f'<rect x="{170+i*3}" y="{506-i*18}" width="140" height="16" fill="{["#fff","#fff3e0","#e3f2fd"][i%3]}" stroke="#999"/>')
b.append('<rect x="660" y="488" width="44" height="32" rx="4" fill="#fff" stroke="#999"/><path d="M704,496 q14,0 14,10 q0,10 -14,10" stroke="#999" stroke-width="4" fill="none"/>')
# phone with messages
b.append('<g transform="translate(860,450) rotate(-6)"><rect x="0" y="0" width="190" height="260" rx="20" fill="#212121"/><rect x="10" y="22" width="170" height="220" fill="#ece5dd"/>')
b.append('<text x="95" y="16" font-size="12" text-anchor="middle" fill="#fff" font-family="Arial">Begum 💢 (14)</text>')
for i, m in enumerate(["Kahan ho??", "Bachon ki fees!", "Mujhe naya sofa", "chahiye 😤", "Tum kuch nahi", "karte!!"]):
    b.append(f'<rect x="18" y="{30+i*34}" width="{len(m)*8+20}" height="26" rx="8" fill="#fff"/><text x="28" y="{48+i*34}" font-size="14" font-family="Arial" fill="#111">{m}</text>')
b.append('</g>')
b.append('<text x="1060" y="450" font-size="38" font-family="Arial" fill="#c62828" font-weight="900">!</text><path d="M1040,470 l10,-10 M1060,480 l14,-4" stroke="#c62828" stroke-width="4"/>')
b.append(bubble(40, 110, 360, 110, ["Bas ek ghanta aur...", "phir ghar."], tail=(330, 330), think=True, fs=26))
s1 = frame(1, "12 Hours at the Office", ["He works late every night so his family can live better", "than most people in the country ever will."], "".join(b), "#cfd8dc", "#b0bec5")

# ---------- Panel 2: Weekend with kids, wife at home on phone ----------
b = []
b.append('<rect x="0" y="0" width="640" height="790" fill="#bde3ff"/><circle cx="540" cy="160" r="50" fill="#ffeb3b"/>')
b.append('<rect x="0" y="560" width="640" height="230" fill="#7cb342"/>')
for tx in (90, 330):
    b.append(f'<rect x="{tx-10}" y="360" width="20" height="210" fill="#6d4c41"/><circle cx="{tx}" cy="330" r="80" fill="#43a047"/><circle cx="{tx-50}" cy="370" r="50" fill="#388e3c"/>')
b.append('<path d="M480,560 L520,400 L560,560" stroke="#e53935" stroke-width="10" fill="none"/><line x1="520" y1="400" x2="600" y2="400" stroke="#e53935" stroke-width="10"/><line x1="600" y1="400" x2="600" y2="560" stroke="#e53935" stroke-width="10"/><line x1="560" y1="400" x2="560" y2="500" stroke="#555" stroke-width="3"/><rect x="545" y="500" width="30" height="8" fill="#555"/>')
b.append(man(300, 730, 0.95, mood="tired", arm="hold", shirt="#fff59d", tie="#fff59d", pants="#5d4037"))
b.append(kid(185, 735, 1.0, shirt="#ff7043", arm="up-right", mood="happy"))
b.append(kid(420, 735, 0.92, shirt="#ec407a", girl=True, arm="up-left", mood="happy"))
b.append('<g transform="translate(150,555)"><path d="M0,0 L10,-30 L20,0Z" fill="#d7a35c"/><circle cx="10" cy="-36" r="12" fill="#f48fb1"/></g>')
b.append(bubble(150, 100, 340, 90, ["Abbu! Ek aur jhoola!"], tail=(200, 520), fs=26))
b.append('<text x="40" y="770" font-size="22" font-family="Arial" font-weight="700" fill="#1b5e20">Sunday, his only day off</text>')
# divider
b.append('<rect x="636" y="78" width="10" height="712" fill="#111"/>')
# home side
b.append('<rect x="646" y="78" width="554" height="712" fill="#f3e5d0"/><rect x="646" y="600" width="554" height="190" fill="#bcaaa4"/>')
b.append('<rect x="700" y="250" width="160" height="120" fill="#90caf9" stroke="#8d6e63" stroke-width="8"/><line x1="780" y1="250" x2="780" y2="370" stroke="#8d6e63" stroke-width="6"/>')
b.append('<rect x="960" y="250" width="180" height="120" fill="#d7ccc8" stroke="#8d6e63" stroke-width="4"/><text x="1050" y="316" text-anchor="middle" font-size="18" font-family="Arial" fill="#5d4037">Family photo</text>')
b.append('<rect x="700" y="480" width="460" height="120" rx="30" fill="#7b1fa2"/><rect x="690" y="440" width="60" height="160" rx="24" fill="#6a1b9a"/><rect x="1110" y="440" width="60" height="160" rx="24" fill="#6a1b9a"/>')
b.append(woman(900, 600, 0.95, mood="smug", pose="phone", sit=True))
b.append('<rect x="1000" y="560" width="120" height="40" rx="6" fill="#fff"/><text x="1060" y="586" text-anchor="middle" font-size="16" font-family="Arial">AC: 18°C ❄</text>')
b.append(bubble(690, 96, 480, 110, ["“Tum hamein kabhi", "bahar nahi le jaate!”"], tail=(880, 360), fs=27, color="#ffebee", border="#c62828", tc="#b71c1c"))
s2 = frame(2, "His Only Day Off", ["He spends Sunday with the kids at the park while she rests at home in the AC —", "and then tells her friends he “never takes the family anywhere.”"], "".join(b), "#fff", "#fff")

# ---------- Panel 3: shopping, maids, social media ----------
b = []
b.append('<rect x="0" y="78" width="1200" height="712" fill="#fff3e0"/><rect x="0" y="620" width="1200" height="170" fill="#d7ccc8"/>')

b.append(maid(170, 700, 0.95, tool="broom"))
b.append(maid(1040, 700, 0.95, tool="tray"))
b.append(woman(560, 700, 1.1, mood="angry", pose="bags", kameez="#ad1457", dupatta="#ffd54f"))
# husband in doorway with bill
b.append('<rect x="760" y="250" width="140" height="370" fill="#6d4c41"/><rect x="772" y="262" width="116" height="358" fill="#3e2723"/>')
b.append(man(830, 640, 0.75, mood="sad", arm="down"))
b.append('<g transform="translate(860,470) rotate(8)"><rect x="0" y="0" width="90" height="120" fill="#fff" stroke="#333" stroke-width="2"/><text x="45" y="22" text-anchor="middle" font-size="14" font-weight="700" font-family="Arial">CARD BILL</text>')
for i, t in enumerate(["Mall  85,000", "Salon 22,000", "Maids 50,000", "Dining 30,000"]):
    b.append(f'<text x="6" y="{44+i*18}" font-size="10" font-family="monospace">{t}</text>')
b.append('<text x="45" y="116" text-anchor="middle" font-size="12" font-weight="900" fill="#c62828" font-family="Arial">PAID ✔</text></g>')
# social post
b.append('<g transform="translate(40,110)"><rect x="0" y="0" width="330" height="200" rx="16" fill="#fff" stroke="#1877f2" stroke-width="4"/><circle cx="34" cy="34" r="18" fill="#f48fb1"/><text x="62" y="32" font-size="15" font-weight="700" font-family="Arial">Begum Sahiba</text><text x="62" y="50" font-size="12" fill="#777" font-family="Arial">Just now · 🌐</text>')
for i, t in enumerate(["Some husbands are just useless 🙄", "Never any time, never any love.", "Mera naseeb hi kharab hai 💔", "#ToxicHusband #SadLife"]):
    b.append(f'<text x="16" y="{88+i*24}" font-size="15" font-family="Arial" fill="{"#1877f2" if i==3 else "#111"}">{t}</text>')
b.append('<text x="16" y="186" font-size="13" fill="#555" font-family="Arial">😂 214   💬 87 comments</text></g>')
b.append(bubble(560, 120, 200, 120, ["Phir bhi", "kuch nahi", "milta!"], tail=(580, 330), color="#ffebee", border="#c62828", fs=24, tc="#b71c1c"))
b.append('<g transform="translate(830,110)"><rect x="0" y="0" width="330" height="110" rx="14" fill="#111"/><text x="165" y="40" text-anchor="middle" fill="#ffca28" font-size="22" font-weight="900" font-family="Arial">Maids · Driver · Mall</text><text x="165" y="76" text-anchor="middle" fill="#fff" font-size="18" font-family="Arial">A life fewer than 1% of</text><text x="165" y="98" text-anchor="middle" fill="#fff" font-size="18" font-family="Arial">Pakistani women ever get</text></g>')
s3 = frame(3, "Everything Paid For. Still Not Enough.", ["Two maids, full shopping bags, every bill paid —", "yet online she calls him a useless husband for everyone to see."], "".join(b), "#fff", "#fff")

# ---------- Panel 4: alone at night ----------
b = []
b.append('<rect x="0" y="78" width="1200" height="712" fill="#0d1b2a"/>')
import random
random.seed(4)
for _ in range(70):
    b.append(f'<circle cx="{random.randint(10,1190)}" cy="{random.randint(90,420)}" r="{random.choice([1,1.5,2])}" fill="#fff" opacity="{random.choice([.5,.8,1])}"/>')
b.append('<circle cx="1040" cy="190" r="56" fill="#fffde7"/><circle cx="1064" cy="176" r="50" fill="#0d1b2a"/>')
for i in range(10):
    bx = i*125; bh = 120 + (i*71) % 160
    b.append(f'<rect x="{bx}" y="{560-bh}" width="110" height="{bh}" fill="#1b263b"/>')
    for wy in range(560-bh+16, 550, 30):
        for wx in (bx+16, bx+60):
            if (wx + wy) % 3: b.append(f'<rect x="{wx}" y="{wy}" width="16" height="12" fill="#ffe082" opacity=".6"/>')
# balcony
b.append('<rect x="0" y="560" width="1200" height="230" fill="#263238"/>')
b.append('<rect x="0" y="540" width="1200" height="14" fill="#90a4ae"/>')
for i in range(0, 1200, 50):
    b.append(f'<rect x="{i}" y="554" width="8" height="120" fill="#78909c"/>')
b.append('<rect x="0" y="670" width="1200" height="12" fill="#90a4ae"/>')
# lit window behind with wife silhouette
b.append('<rect x="60" y="250" width="300" height="300" fill="#ffcc80"/><rect x="60" y="250" width="300" height="300" fill="none" stroke="#5d4037" stroke-width="10"/>')
b.append('<g opacity=".85">' + woman(210, 560, 0.85, mood="angry", pose="point", kameez="#4e342e", dupatta="#4e342e") + '</g>')
b.append(bubble(40, 110, 360, 100, ["Aur paise chahiye!", "Tum kisi kaam ke nahi!"], tail=(200, 290), color="#ffebee", border="#c62828", fs=23, tc="#b71c1c"))
# husband sitting on chair, back slumped
b.append('<rect x="640" y="600" width="140" height="16" fill="#795548"/><rect x="650" y="616" width="12" height="70" fill="#5d4037"/><rect x="760" y="616" width="12" height="70" fill="#5d4037"/><rect x="760" y="470" width="14" height="146" fill="#5d4037"/>')
b.append(man(710, 690, 0.95, mood="sad", arm="down", shirt="#cfd8dc", tie="#455a64"))
b.append('<rect x="560" y="610" width="40" height="50" rx="6" fill="#fff"/><path d="M570,605 q5,-14 0,-24 M585,605 q5,-14 0,-24" stroke="#ccc" stroke-width="3" fill="none"/>')
# phone: empty contacts / memes
b.append('<g transform="translate(860,330)"><rect x="0" y="0" width="200" height="290" rx="22" fill="#212121"/><rect x="10" y="24" width="180" height="246" fill="#eceff1"/>')
b.append('<text x="100" y="48" text-anchor="middle" font-size="15" font-weight="700" font-family="Arial">Messages</text>')
b.append('<rect x="20" y="62" width="160" height="56" rx="8" fill="#fff"/><text x="30" y="82" font-size="12" font-weight="700" font-family="Arial">Begum</text><text x="30" y="102" font-size="11" font-family="Arial">sent a meme: “Husband =</text><text x="30" y="114" font-size="11" font-family="Arial">ATM” 😂🤡</text>')
b.append('<rect x="20" y="126" width="160" height="40" rx="8" fill="#fff"/><text x="30" y="150" font-size="11" font-family="Arial">Begum: “Idiot 🙄”</text>')
b.append('<rect x="20" y="174" width="160" height="40" rx="8" fill="#fff"/><text x="30" y="198" font-size="11" font-family="Arial">Friends: no new messages</text>')
b.append('<text x="100" y="250" text-anchor="middle" font-size="12" fill="#777" font-family="Arial">No one asked “how are you?”</text></g>')
b.append(bubble(470, 140, 400, 150, ["Main bhi insaan hoon.", "Kabhi koi poochta hai", "main kaisa hoon?"], tail=(650, 380), think=True, color="#e3f2fd", border="#90caf9", fs=26, tc="#0d47a1"))
s4 = frame(4, "Who Asks How He Is?", ["No friends left, no rest, no thank you — only memes calling him an idiot.", "Behind the paycheck there is a person. His mental health matters too."], "".join(b), "#0d1b2a", "#0d1b2a")

for i, s in enumerate([s1, s2, s3, s4], 1):
    with open(os.path.join(OUT, f"panel-{i}.svg"), "w") as f:
        f.write(s)
print("ok")
