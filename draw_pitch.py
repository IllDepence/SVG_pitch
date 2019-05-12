""" Draw pitch accent patterns in SVG

    Example:

        python3 draw_pitch.py はな 010 > 花.html
        firefox 花.html
"""

import sys

def circle(x, y, o=False):
    r = ('<circle r="5" cx="{}" cy="{}" style="opacity:1;fill:#000;" />'
        ).format(x, y)
    if o:
        r += ('<circle r="3.25" cx="{}" cy="{}" style="opacity:1;fill:#fff;"'
              '/>').format(x, y)
    return r

def text(x, text):
    # letter positioning tested with Noto Sans CJK JP
    return ('<text x="{}" y="67.5" style="font-size:20px;font-family:sans-seri'
            'f;fill:#000000;">{}</text>').format(x, text)

def path(x, y, typ):
    if typ == 's':  # straight
        delta = '29,0'
    elif typ == 'u':  # up
        delta = '29,-25'
    elif typ == 'd':  # down
        delta = '29,25'
    return ('<path d="m {},{} {}" style="fill:none;stroke:#000000;stroke-width'
            ':1.5;" />').format(x, y, delta)

if len(sys.argv) != 3:
    print('usage: python3 draw_pitch.py <word> <patt>')
    sys.exit()

word = sys.argv[1]
patt = sys.argv[2]

if len(patt) - len(word) not in [0, 1]:
    print('pattern should be length of word or length of word + 1')
    sys.exit()

svg_width = (len(word) * 29) + 19

svg = ('<svg class="pitch" width="{0}px" height="80px" viewBox="0 0 {0} 80">'
      ).format(svg_width)
circles = ''
paths = ''

for pos, accent in enumerate(patt):
    x_center = 9.5 + (pos * 29)
    if accent in ['H', 'h', '1', '2']:
        y_center = 5
    elif accent in ['L', 'l', '0']:
        y_center = 30
    if pos < len(word):
        char = word[pos]
        svg += text(x_center-11, char)
    circles += circle(x_center, y_center, pos==len(word))
    if pos > 0:
        if prev_center[1] == y_center:
            path_typ = 's'
        elif prev_center[1] < y_center:
            path_typ = 'd'
        elif prev_center[1] > y_center:
            path_typ = 'u'
        paths += path(prev_center[0], prev_center[1], path_typ)
    prev_center = (x_center, y_center)

svg += paths
svg += circles
svg += '</svg>'

print(svg)
