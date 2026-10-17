"""Rebuild the standalone gallery and individual SVGs. Python standard library only."""
from pathlib import Path
import json
from extras import COSTUMES, outfit as extra_outfit
from headgear import headgear, HIDE, NAMES, NECK_COLORS
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'avatar-source.svg'
(ROOT / 'svg').mkdir(exist_ok=True)
(ROOT / 'svg' / 'headgear').mkdir(exist_ok=True)
INK = '#22211f'
SKIN = '#f4eee2'
SKINS = {'frankenstein':'#b6c493'}
HEROES = [
('astronaut','太空人 Astronaut','#ece9dc',None,'今晚的任務：在月球找糖果。'),
('chucky','恰吉 Chucky','#b65a40',None,'條紋上衣、吊帶褲，還有一點壞壞的笑。'),
('vampire','吸血鬼 Vampire','#37313c','#704254','晚安，今晚喝蔓越莓汁。'),
('mummy','木乃伊 Mummy','#e4d8bc',None,'包得很緊，糖果還是裝得下。'),
('wizard','巫師 Wizard','#6c6289','#504c70','施一個讓週一消失的魔法。'),
('pumpkin','南瓜 Pumpkin','#d88a43',None,'小心，我的口袋全是糖。'),
('pirate','海盜 Pirate','#6d4351',None,'藏寶圖指向下一家糖果店。'),
('frankenstein','科學怪人 Frankenstein','#68765c',None,'充完電，就可以出門搗蛋。'),
('skeleton','骷髏 Skeleton','#35383b',None,'骨感穿搭，甜食照吃。'),
('robot','機器人 Robot','#9aaeb1',None,'偵測到糖果。快樂值加一。'),
] + COSTUMES

def outfit(key,suit,cape,equipped=False):
    back=''
    if cape:
        back=f'<path class="cape" fill="{cape}" d="M148 344Q81 330 57 407L27 493Q200 511 373 493L343 407Q319 330 252 344Z"/>'
    if key=='astronaut':
        back='<rect x="77" y="332" width="246" height="149" rx="26" fill="#a3b5b6"/><path d="M82 367H318" fill="none"/>'
    if key=='vampire':
        back+='<path fill="#704254" d="M172 365L96 284L106 373L144 402M228 365L304 284L294 373L256 402"/>'
    neck_d = 'M174 314 Q170 337 155 359 Q200 387 245 359 Q230 337 226 314 Z'
    skin = SKINS.get(key,SKIN)
    neck_fill = NECK_COLORS.get(key,skin) if equipped else skin
    neck = f'''<defs><clipPath id="{key}-neck-clip"><path class="neck-clip" d="{neck_d}"/></clipPath></defs>
<path class="neck-skin" fill="{neck_fill}" d="{neck_d}"/>
<g clip-path="url(#{key}-neck-clip)"><path class="neck-shadow" fill="#272724" fill-opacity=".12" stroke="none" d="M174 327 Q200 342 226 327 L231 346 Q200 360 169 346 Z"/></g>'''
    torso = f'<path fill="{suit}" d="M155 351 Q137 356 105 367 Q64 380 57 425 L49 487 Q200 506 351 487 L343 425 Q336 380 295 367 Q263 356 245 351 Q200 376 155 351 Z"/>'
    detail=''
    if key=='astronaut':
        detail='<path fill="#a3b5b6" d="M151 351Q200 377 249 351L261 370Q200 406 139 370Z"/><rect x="156" y="410" width="88" height="56" rx="8" fill="#728c98"/><rect x="167" y="420" width="40" height="21" rx="3" fill="#d3e8db"/><circle cx="226" cy="426" r="5" fill="#d5884e"/><circle cx="226" cy="448" r="5" fill="#eed395"/><path d="M167 453H204M83 425L111 430M79 439L107 444M317 425L289 430M321 439L293 444" fill="none"/><path d="M128 410Q113 448 141 478" fill="none" stroke="#d5b470" stroke-width="10"/><circle cx="285" cy="396" r="13" fill="#d5884e"/><path d="M281 387L279 398H289L284 406" fill="none" stroke="#fff7dc"/>'
    elif key=='chucky':
        detail='<g fill="none" stroke-width="7">'
        for y,col in [(374,'#d4b762'),(387,'#718a89'),(400,'#ead6b8'),(413,'#7b6a88'),(426,'#d4b762'),(439,'#718a89'),(452,'#ead6b8'),(465,'#7b6a88')]:
            detail+=f'<path d="M48 {y}H352" stroke="{col}"/>'
        detail+='</g><path fill="#527e98" d="M125 360L150 354L160 410H240L250 354L275 360L263 438V504H137V438Z"/><circle cx="153" cy="415" r="7" fill="#cc7147"/><circle cx="247" cy="415" r="7" fill="#cc7147"/><path fill="#658fa5" d="M171 438H229V466Q200 482 171 466Z"/><path d="M180 447H220" stroke="#e2c9a0" stroke-dasharray="3 5"/><path d="M146 455L154 463M244 483L252 475M222 490L216 483" stroke="#ddaa61"/>'
    elif key=='vampire':
        detail='<path fill="#eee4cf" d="M155 351Q200 378 245 351L230 451H170Z"/><path fill="#985d68" d="M169 393L200 404L231 393L231 420L200 410L169 420Z"/><circle cx="200" cy="406" r="6" fill="#d1a25a"/><path fill="#242631" d="M122 362L164 376L184 482L139 432L155 414L128 405Z M278 362L236 376L216 482L261 432L245 414L272 405Z"/><path d="M200 430V490" fill="none"/><circle cx="200" cy="443" r="3" fill="#cba75e"/><circle cx="200" cy="463" r="3" fill="#cba75e"/>'
    elif key=='mummy':
        detail='<g fill="none" stroke="#9f957f" stroke-width="3">'
        for y in range(370,510,24):
            detail+=f'<path d="M40 {y}Q200 {y+35}360 {y-3}"/>'
        detail+='</g><path fill="#f1e6cb" d="M101 364L123 359L277 488L250 496Z"/><path fill="#eee1bf" d="M288 365L306 379L110 499L79 490Z"/><path d="M152 406L144 414M215 456L207 463" stroke="#b3a789"/>'
    elif key=='wizard':
        detail='<path fill="#dac38b" d="M152 351L200 414L248 351L254 364L207 432V500H193V432L146 364Z"/><circle cx="200" cy="415" r="10" fill="#92b1a6"/>'
        for x,y in [(104,406),(275,444),(144,475)]:
            detail+=f'<path fill="#d9c795" d="M{x} {y-12}L{x+4} {y-4}L{x+13} {y}L{x+4} {y+4}L{x} {y+12}L{x-4} {y+4}L{x-13} {y}L{x-4} {y-4}Z" stroke-width="2"/>'
        back+='<path d="M330 490L307 341" stroke="#876544" stroke-width="9"/><circle cx="307" cy="341" r="18" fill="#cab476"/><path d="M307 329V353M295 341H319" stroke="#fff0be"/>'
    elif key=='pumpkin':
        torso='<path fill="#d88a43" d="M153 350Q200 375 247 350Q349 360 355 438Q365 509 200 505Q35 509 45 438Q51 360 153 350Z"/>'
        detail='<g fill="none" stroke="#aa6037"><path d="M134 370Q98 440 135 499M266 370Q302 440 265 499M200 380V502"/></g><path fill="#728059" d="M147 350L168 370L183 361L199 385L217 361L234 370L253 350Q200 381 147 350Z"/><path fill="#3b3530" d="M134 414L164 396L174 425Z M266 414L236 396L226 425Z M189 441L200 426L211 441Z M130 453L158 466L166 455L183 473H215L232 455L241 466L270 453Q252 490 200 489Q148 490 130 453Z"/>'
    elif key=='pirate':
        detail='<path fill="#f0e3c9" d="M155 351Q200 375 245 351L230 501H170Z"/><path fill="#8b5b62" d="M127 362L156 355L180 500H117Z M273 362L244 355L220 500H283Z"/><path d="M160 370L176 402L155 424M240 370L224 402L245 424" fill="none" stroke="#d8b46a" stroke-width="5"/><path d="M116 370L283 485" stroke="#3c3333" stroke-width="18"/><rect x="185" y="420" width="28" height="24" rx="3" fill="#d6b474" transform="rotate(35 200 432)"/><path fill="#d3b171" d="M54 474Q200 489 346 474L350 490Q200 510 50 490Z"/>'
    elif key=='frankenstein':
        detail='<path fill="#3c4140" d="M155 351Q200 377 245 351L240 500H160Z"/><path fill="#879170" d="M130 359L158 353L183 479L133 429L153 409L120 399Z M270 359L242 353L217 479L267 429L247 409L280 399Z"/><g fill="none" stroke="#ded9bc"><path d="M76 442L111 459M78 449L83 438M89 455L94 444M100 461L105 450M281 393L317 406M287 388L283 400M299 393L295 405M311 398L307 410"/></g>'
        back+='<g fill="#a5b0ae"><rect x="139" y="332" width="31" height="15" rx="3"/><rect x="230" y="332" width="31" height="15" rx="3"/></g>'
    elif key=='skeleton':
        detail='<g stroke="#e9e3d4" stroke-width="9" fill="none"><path d="M200 377V486M179 388Q141 384 127 401Q145 418 183 408M221 388Q259 384 273 401Q255 418 217 408M181 423Q147 416 133 430Q153 448 185 442M219 423Q253 416 267 430Q247 448 215 442M183 456Q159 448 145 460Q163 475 186 474M217 456Q241 448 255 460Q237 475 214 474M94 410L81 467M306 410L319 467"/></g><circle cx="80" cy="475" r="8" fill="#e9e3d4"/><circle cx="320" cy="475" r="8" fill="#e9e3d4"/>'
    elif key=='robot':
        detail='<path fill="#697f85" d="M155 351Q200 375 245 351L249 378H151Z"/><rect x="125" y="397" width="150" height="85" rx="13" fill="#c9cebc"/><rect x="140" y="410" width="75" height="37" rx="4" fill="#536e70"/><path d="M148 435L159 435L167 420L178 440L188 425L204 425" stroke="#cbe0ae" fill="none"/><circle cx="242" cy="420" r="8" fill="#c7855c"/><circle cx="242" cy="445" r="8" fill="#cfb877"/><path d="M145 463H211M79 416L108 423M76 433L105 440M321 416L292 423M324 433L295 440" stroke="#556f75" fill="none" stroke-width="5"/>'
    if key in {item[0] for item in COSTUMES}:
        extra_back,detail=extra_outfit(key)
        back+=extra_back
    body_path=re.search(r'd="([^"]+)"',torso)[1]
    clip=f'<defs><clipPath id="{key}-body-clip"><path d="{body_path}"/></clipPath></defs>'
    return back+neck+torso+clip+f'<g clip-path="url(#{key}-body-clip)">{detail}</g>'

def portrait(key,name,suit,cape,equipped=False):
    src = SOURCE.read_text()
    group = src[src.index('  <g stroke='):src.rindex('</svg>')]
    # The original avatar remains the shared drawing source.
    group = re.sub(r'    <!-- Neck -->.*?<!-- Ears -->', '    <!-- Ears -->', group, flags=re.S)
    skin = SKINS.get(key,SKIN)
    group = group.replace('fill="white"', f'fill="{skin}"')
    group = re.sub(r'id="([^"]+)"', lambda m:f'id="{key}-{m[1]}" class="{m[1]}"',group)
    if equipped:
        for feature in HIDE[key]:
            group = group.replace(f'class="{feature}"',f'class="{feature}" opacity="0"')
    gear = f'<g class="headgear" data-hide="{" ".join(HIDE[key])}" opacity="{1 if equipped else 0}" stroke-width="3.5">{headgear(key)}</g>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 520" width="400" height="520" role="img" aria-labelledby="{key}-title">
<title id="{key}-title">Your portrait in the {name} outfit</title>
<g class="character" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
<g class="outfit">{outfit(key,suit,cape,equipped)}</g>
<g class="head">{group}{gear}</g>
</g></svg>'''

items=[]
for key,name,suit,cape,line in HEROES:
    svg=portrait(key,name,suit,cape)
    ET.fromstring(svg)
    (ROOT/'svg'/f'{key}.svg').write_text(svg)
    equipped = portrait(key,name,suit,cape,True)
    ET.fromstring(equipped)
    (ROOT/'svg'/'headgear'/f'{key}.svg').write_text(equipped)
    items.append(dict(key=key,name=name,line=line,svg=svg,helmetSvg=equipped,headgearName=NAMES[key],neckColor=NECK_COLORS.get(key,SKINS.get(key,SKIN)),skinColor=SKINS.get(key,SKIN)))
template=(ROOT/'template.html').read_text().replace('{{HERO_COUNT}}',str(len(HEROES)))
(ROOT/'index.html').write_text(template.replace('/* PORTRAITS_DATA */',json.dumps(items).replace('<', '\\u003c')))
print(f'Built {len(items)} SVG portraits and {ROOT / "index.html"}')
