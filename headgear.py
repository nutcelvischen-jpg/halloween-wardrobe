"""Hand-drawn Halloween accessories, shared portrait coordinates."""
HIDE={key:() for key in ['astronaut','chucky','vampire','mummy','wizard','pumpkin','pirate','frankenstein','skeleton','robot']}
for key in ['chucky','mummy','wizard','pumpkin','pirate','frankenstein','robot']:
    HIDE[key]=('hair',)
NAMES=dict(zip(HIDE,['太空頭盔','橘紅假髮與雀斑','尖牙','繃帶頭套','星月巫師帽','南瓜貝雷帽','海盜三角帽','平頂假髮與縫線','骷髏彩妝','天線頭盔']))
NECK_COLORS={}

def headgear(key):
    if key=='astronaut':
        return '''<path fill="#e9e5d7" fill-rule="evenodd" d="M200 21C99 21 69 91 77 218Q79 304 151 342Q200 362 249 342Q321 304 323 218C331 91 301 21 200 21Z M200 46C119 46 95 106 99 210Q101 288 159 316Q200 337 241 316Q299 288 301 210C305 106 281 46 200 46Z"/><path d="M119 101Q145 62 188 61M111 116L107 132" stroke="#fffefa" stroke-width="9" fill="none"/><path d="M281 272L270 289" stroke="#9ebbc3" stroke-width="5" fill="none"/><rect x="67" y="171" width="32" height="69" rx="12" fill="#8ea6ac"/><rect x="301" y="171" width="32" height="69" rx="12" fill="#8ea6ac"/><circle cx="83" cy="205" r="8" fill="#d8c08d"/><circle cx="317" cy="205" r="8" fill="#d8c08d"/>'''
    if key=='chucky':
        return '''<path fill="#b9693f" d="M112 209Q88 181 103 137L93 143L111 109L105 91L129 98L133 71L159 81Q202 42 247 74L277 68L273 92L301 98L290 123Q312 156 289 210L276 188L269 146Q232 141 202 110Q175 140 132 146L126 191Z"/><g fill="none" stroke="#80472e" stroke-width="3"><path d="M116 156Q130 110 176 94M126 123Q149 99 164 98M230 91Q274 112 283 165M244 111L271 134"/></g><g fill="#b57855" stroke="none"><circle cx="144" cy="254" r="2.5"/><circle cx="153" cy="259" r="2.5"/><circle cx="161" cy="251" r="2.5"/><circle cx="239" cy="251" r="2.5"/><circle cx="249" cy="258" r="2.5"/><circle cx="258" cy="251" r="2.5"/></g><path d="M255 273L240 298M249 277L258 283M244 286L252 291" stroke="#9f655b" fill="none" stroke-width="2"/>'''
    if key=='vampire':
        return '<path fill="#fffdf1" d="M177 283L184 299L190 285Z M213 281L220 295L226 278Z" stroke-width="2"/>'
    if key=='mummy':
        return '''<path fill="#e5d9bb" d="M105 193Q94 82 170 63Q264 40 294 131L292 187L271 173Q218 185 130 177L124 200Z"/><path fill="none" stroke="#a99b7d" d="M114 112Q192 151 285 117M133 80Q205 116 278 100M103 153Q192 122 293 153M174 64Q197 107 221 122"/><path fill="#f0e3c5" d="M117 250Q200 275 280 241L275 264Q206 298 123 273Z"/><path fill="#e5d9bb" d="M142 306Q201 333 255 302L235 327Q201 349 168 328Z"/><path d="M136 259Q180 269 225 264" stroke="#b5a586" fill="none" stroke-width="2"/>'''
    if key=='wizard':
        return '''<path fill="#6c6289" d="M120 142L175 26Q207 13 251 49L217 44L276 145Z"/><path fill="#c9ac6e" d="M133 113Q204 139 260 112L275 144H120Z"/><path fill="#6c6289" d="M78 154Q132 130 174 140Q249 153 307 140Q331 145 309 158Q201 196 88 171Q68 164 78 154Z"/><path fill="#e5d39b" stroke="none" d="M184 64Q177 91 204 91Q183 108 172 86Q167 72 184 64Z"/><path d="M216 83V99M208 91H224" stroke="#e5d39b" stroke-width="3"/>'''
    if key=='pumpkin':
        return '''<path fill="#d88a43" d="M110 160Q89 92 162 83Q199 57 239 82Q308 88 289 160Q200 137 110 160Z"/><path d="M165 85Q140 112 151 148M235 84Q260 112 249 148M200 78V145" stroke="#a7663a" fill="none"/><path fill="#73835c" d="M186 82L191 49L210 44L208 80Z"/><path fill="#8e9c6b" d="M210 76Q253 48 265 74Q237 91 210 76Z"/><path d="M210 76L251 70" fill="none" stroke="#566c49"/><path fill="#5e7050" d="M113 151Q200 135 287 151L283 170Q200 153 117 170Z"/>'''
    if key=='pirate':
        return '''<path fill="#a45c53" d="M111 155Q200 124 289 155L284 183Q201 155 116 183Z"/><path fill="#353239" d="M78 163L58 107Q100 120 129 96Q161 46 202 55Q242 46 273 96Q300 120 342 107L322 163Q200 124 78 163Z"/><path d="M75 122L88 148Q200 114 312 148L325 122M142 100Q200 38 260 100" stroke="#ceaf73" fill="none" stroke-width="4"/><g fill="#eee3cc" stroke-width="2"><path d="M184 93Q200 77 216 93L213 110H187Z"/><path d="M190 114L210 129M210 114L190 129" stroke="#eee3cc" stroke-width="4"/><circle cx="194" cy="99" r="3" fill="#353239"/><circle cx="206" cy="99" r="3" fill="#353239"/></g><circle cx="291" cy="252" r="11" fill="none" stroke="#c9a45c" stroke-width="5"/>'''
    if key=='frankenstein':
        return '''<path fill="#343a34" d="M109 206L111 87Q200 64 289 87L291 206L274 186L267 142L250 145L242 132L220 145L203 131L182 144L161 132L137 147L126 189Z"/><path d="M145 161L250 154M157 152L158 168M180 150L181 165M204 149L205 163M228 146L229 161" fill="none" stroke="#617653" stroke-width="3"/><path d="M265 270L248 290M257 272L265 280M250 281L257 288" fill="none" stroke="#617653" stroke-width="2.5"/>'''
    if key=='skeleton':
        return '''<path fill="#eee8db" stroke-width="2" d="M129 248Q148 233 170 247L163 264L139 272Z M271 246Q252 231 230 245L237 262L261 270Z"/><path fill="#3c4140" stroke="none" d="M193 251L200 239L207 251L200 255Z"/><path d="M166 292Q200 311 237 286M179 291L176 304M193 295V310M207 293L209 307M221 289L225 301" stroke="#656861" stroke-width="2.5" fill="none"/>'''
    if key=='robot':
        return '''<path d="M200 73V38" stroke="#677b7f" stroke-width="6"/><circle cx="200" cy="31" r="12" fill="#d49265"/><path fill="#a5b6b7" d="M105 183V104Q105 76 135 76H265Q295 76 295 104V183L275 174V150H125V174Z"/><path fill="#d1d5c5" d="M132 92H268V129H132Z"/><path d="M151 103V118M175 103V118M199 103V118M223 103V118M247 103V118" stroke="#6c8589"/><rect x="88" y="183" width="32" height="66" rx="8" fill="#a5b6b7"/><rect x="280" y="183" width="32" height="66" rx="8" fill="#a5b6b7"/><circle cx="104" cy="215" r="6" fill="#d9bd7f"/><circle cx="296" cy="215" r="6" fill="#d9bd7f"/>'''
    raise KeyError(key)
