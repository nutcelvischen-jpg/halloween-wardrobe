"""Eight additional Halloween costumes, drawn with editable SVG geometry."""
COSTUMES=[
('blackcat','黑貓 Black Cat','#37363f',None,'聽到糖果袋的聲音，耳朵就豎起來。'),
('dinosaur','恐龍睡衣 Dinosaur','#829778',None,'躲在恐龍嘴巴裡，安心吃糖。'),
('mushroom','蘑菇精靈 Mushroom','#8b9272',None,'森林派對，帶一點小孢子。'),
('diver','復古潛水員 Diver','#9a927c',None,'今晚潛進糖果海。'),
('jiangshi','殭屍道長 Jiangshi','#43556d',None,'符紙一晃，跳進萬聖節。'),
('bee','蜜蜂 Bee','#d4b46b',None,'把糖果當花蜜，快樂採集。'),
('pumpkinlord','南瓜紳士 Pumpkin Lord','#514753',None,'南瓜頭罩一戴，晚宴正式開始。'),
('ghostchef','幽靈甜點師 Ghost Chef','#e8ddc5',None,'今天的特餐：小鬼奶油泡芙。'),
]
HIDE={key:('hair',) for key,*_ in COSTUMES}
HIDE['blackcat']=()
HIDE['bee']=()
HIDE['pumpkinlord']=('hair','ears','glasses','brows','eyes','nose','mouth')
NAMES=dict(zip(HIDE,['貓耳與鬍鬚','恐龍連帽頭套','紅白蘑菇帽','銅色潛水頭盔','清朝帽與符紙','蜜蜂觸角','南瓜頭罩','藏著小鬼的廚師帽']))

def outfit(key):
    back=''; detail=''
    if key=='blackcat':
        back='<path d="M311 475Q389 451 351 375Q333 347 341 330" stroke="#37363f" stroke-width="19" fill="none"/>'
        detail='<path fill="#d6c6b7" d="M168 374Q200 391 232 374L245 480Q200 505 155 480Z"/><path fill="#976b75" d="M165 368L200 382L235 368V395L200 387L165 395Z"/><circle cx="200" cy="387" r="10" fill="#d1b46a"/>'
    elif key=='dinosaur':
        back='<path fill="#d1bc78" d="M278 350L313 330L309 371L344 369L329 402L365 412L340 436L370 460L341 480Z"/>'
        detail='<path fill="#d9d7ab" d="M163 374Q200 390 237 374L250 492H150Z"/><path d="M200 386V492" fill="none" stroke="#74836a" stroke-width="2"/><g fill="#647e62" stroke="none"><circle cx="100" cy="417" r="10"/><circle cx="120" cy="454" r="7"/><circle cx="292" cy="426" r="11"/><circle cx="283" cy="466" r="7"/></g><circle cx="200" cy="409" r="5" fill="#b49e6e"/>'
    elif key=='mushroom':
        detail='<path fill="#e5d4af" d="M153 352Q200 376 247 352L228 500H172Z"/><path fill="#737e60" d="M117 365L151 354L182 492L124 475Z M283 365L249 354L218 492L276 475Z"/><path d="M147 414Q200 441 254 409" stroke="#70533e" stroke-width="12" fill="none"/><path fill="#b79766" d="M219 437Q240 428 261 439L257 477H222Z"/><circle cx="199" cy="392" r="6" fill="#937849"/>'
    elif key=='diver':
        detail='<path fill="#ba8b59" d="M142 351Q200 373 258 351L284 389Q200 426 116 389Z"/><path d="M140 366Q200 404 260 366" stroke="#e2c38a" stroke-width="8" fill="none"/><path d="M121 399L111 490M279 399L289 490" stroke="#594e44" stroke-width="17"/><rect x="158" y="424" width="84" height="53" rx="8" fill="#b28d5f"/><circle cx="200" cy="450" r="17" fill="#e0d0a5"/><path d="M200 450L207 439" fill="none"/><path d="M306 388Q361 369 334 330" stroke="#b89c68" stroke-width="12" fill="none"/>'
    elif key=='jiangshi':
        detail='<path fill="#e2d1a8" d="M155 351L200 380L245 351L252 363L204 398L148 365Z"/><path d="M204 393V495" stroke="#bb9966" stroke-width="5"/><g stroke="#dac49b" stroke-width="4"><path d="M186 413H222M186 439H222M186 465H222"/></g><circle cx="204" cy="412" r="5" fill="#c9a868"/><circle cx="204" cy="438" r="5" fill="#c9a868"/><circle cx="204" cy="464" r="5" fill="#c9a868"/><path d="M69 452L115 462M331 452L285 462" stroke="#b99b6c" stroke-width="12"/>'
    elif key=='bee':
        back='<g class="bee-wings" fill="#e1ece3" fill-opacity=".9"><ellipse cx="91" cy="359" rx="42" ry="67" transform="rotate(-35 91 359)"/><ellipse cx="309" cy="359" rx="42" ry="67" transform="rotate(35 309 359)"/><path d="M69 319L117 406M331 319L283 406" stroke="#a8bbb1" fill="none"/></g>'
        detail='<path d="M49 401H351M49 451H351M49 497H351" stroke="#3f3a37" stroke-width="24"/><path fill="#e8d39b" d="M157 351L200 375L243 351L228 386H172Z"/><path fill="#9b6a5b" d="M176 378L200 387L224 378V402L200 393L176 402Z"/>'
    elif key=='pumpkinlord':
        detail='<path fill="#e8deca" d="M155 351Q200 375 245 351L227 493H173Z"/><path fill="#39343d" d="M127 364L156 352L187 492L137 438L155 414L126 405Z M273 364L244 352L213 492L263 438L245 414L274 405Z"/><path fill="#ba8052" d="M174 375L200 386L226 375V401L200 391L174 401Z"/><circle cx="200" cy="421" r="4" fill="#665046"/><circle cx="200" cy="444" r="4" fill="#665046"/><path d="M269 438Q258 469 229 465" stroke="#c6a46a" fill="none"/><path d="M268 404L276 392L284 405Z" fill="#c6a46a"/>'
    elif key=='ghostchef':
        detail='<path fill="#fff6df" d="M153 351L201 382L245 351L255 365L218 401H159Z"/><path fill="#b1bcb0" d="M131 370L151 364L162 419H238L249 364L269 370L256 503H144Z"/><path fill="#ccd2bb" d="M173 440H227V472Q200 485 173 472Z"/><path d="M178 448H222" stroke="#fff6df" stroke-dasharray="3 5"/><path d="M285 401L295 462" stroke="#a68458" stroke-width="8"/><ellipse cx="283" cy="389" rx="12" ry="20" fill="#c5a371"/>'
    return back,detail

def gear(key):
    if key=='blackcat':
        return '''<g class="cat-ears"><path fill="#37363f" d="M117 130L100 47Q147 62 160 104Z M240 104Q253 62 300 47L283 130Z"/><path fill="#bc9195" stroke="none" d="M119 107L113 68L145 99Z M255 99L287 68L281 107Z"/></g><g fill="none" stroke="#685357" stroke-width="2.5"><path d="M137 263L89 252M139 273L90 277M263 263L311 252M261 273L310 277"/></g><path fill="#9f777d" d="M191 256Q200 251 209 256L200 264Z" stroke-width="2"/>'''
    if key=='dinosaur':
        return '''<path fill="#839a79" d="M110 259Q78 210 99 141Q93 88 139 67Q201 34 260 68Q309 91 301 143Q322 210 290 259L276 246L279 158Q200 183 121 158L124 246Z"/><path fill="#9daf86" d="M106 133Q200 108 294 133L280 166Q201 182 120 166Z"/><g fill="#f2e7c8" stroke-width="2"><path d="M130 166L139 183L149 168M171 172L180 188L189 174M212 174L221 188L230 172M251 168L261 184L270 166"/></g><ellipse cx="142" cy="102" rx="15" ry="18" fill="#f1e4ba"/><ellipse cx="258" cy="102" rx="15" ry="18" fill="#f1e4ba"/><circle cx="145" cy="103" r="5"/><circle cx="255" cy="103" r="5"/><path fill="#c6b774" d="M181 65L200 30L219 65Z"/>'''
    if key=='mushroom':
        return '''<g class="mushroom-cap"><path fill="#b66153" d="M65 154Q86 58 185 47Q284 39 335 154Q200 190 65 154Z"/><ellipse cx="200" cy="155" rx="135" ry="24" fill="#ebd9b6"/><path d="M100 157L156 165M139 149L177 165M200 145V168M261 149L223 165M300 157L244 165" stroke="#b99e82" stroke-width="2"/><g fill="#f0e4ca" stroke="none"><ellipse cx="125" cy="112" rx="22" ry="15" transform="rotate(-25 125 112)"/><ellipse cx="205" cy="78" rx="26" ry="17"/><ellipse cx="283" cy="118" rx="21" ry="16"/></g></g><g class="magic-dust" fill="#d6bc7a" stroke="none"><circle cx="75" cy="193" r="5"/><circle cx="320" cy="207" r="4"/><circle cx="304" cy="186" r="3"/></g>'''
    if key=='diver':
        return '''<path fill="#ba8b59" fill-rule="evenodd" d="M200 47Q306 46 312 161L307 255Q294 322 241 344H159Q106 322 93 255L88 161Q94 46 200 47Z M200 100Q125 100 121 185L126 254Q140 308 200 314Q260 308 274 254L279 185Q275 100 200 100Z"/><path d="M200 62V89M111 161L100 155M289 161L300 155M126 294L116 304M274 294L284 304" stroke="#f0ce95" stroke-width="7"/><rect x="73" y="169" width="37" height="71" rx="11" fill="#876545"/><rect x="290" y="169" width="37" height="71" rx="11" fill="#876545"/><path d="M81 185H101M81 199H101M81 213H101M299 185H319M299 199H319M299 213H319" stroke="#c9a774" stroke-width="3"/><path d="M140 145Q157 121 179 120" stroke="#fdf1d3" stroke-width="6" fill="none"/><g class="diver-bubbles" fill="#e3ece5" fill-opacity=".6" stroke="#849b9d" stroke-width="2"><circle cx="330" cy="128" r="10"/><circle cx="345" cy="92" r="7"/><circle cx="327" cy="64" r="4"/></g>'''
    if key=='jiangshi':
        return '''<path fill="#3c4e68" d="M108 157L112 119Q119 66 200 66Q281 66 288 119L292 157Z"/><path d="M200 76V139M143 91L136 138M257 91L264 138" stroke="#6e7b8e" fill="none"/><ellipse cx="200" cy="66" rx="13" ry="10" fill="#984f4b"/><path fill="#242e43" d="M100 144Q200 126 300 144V171Q200 152 100 171Z"/><circle cx="200" cy="149" r="12" fill="#c4ab71"/><g class="talisman"><path fill="#e4c77f" d="M184 158H216L219 251L201 246L183 254Z"/><path d="M192 172H209M200 165V192M190 183H211M192 195L209 203L192 213L209 221M200 219V237M191 230H210" stroke="#a35143" stroke-width="3" fill="none"/></g>'''
    if key=='bee':
        return '''<path d="M132 123Q200 100 268 123" stroke="#d7b770" stroke-width="12" fill="none"/><g class="bee-antennae"><path d="M145 113Q112 78 126 53M255 113Q288 78 274 53" stroke="#3f3a37" stroke-width="5" fill="none"/><circle cx="127" cy="48" r="13" fill="#d7b770"/><circle cx="273" cy="48" r="13" fill="#d7b770"/></g><ellipse cx="143" cy="259" rx="13" ry="6" fill="#d9a383" stroke="none"/><ellipse cx="257" cy="257" rx="13" ry="6" fill="#d9a383" stroke="none"/>'''
    if key=='pumpkinlord':
        return '''<path fill="#c98347" d="M200 76Q161 58 133 80Q74 100 89 207Q82 309 150 328Q200 350 250 328Q318 309 311 207Q326 100 267 80Q239 58 200 76Z"/><path d="M156 86Q119 200 155 317M244 86Q281 200 245 317M200 86V320" stroke="#a5663d" fill="none"/><path fill="#748158" d="M188 77L192 47L212 39L208 78Z"/><g class="lantern-light" fill="#f1d78b"><path d="M123 196L173 177L181 216Z M277 196L227 177L219 216Z M187 242L200 221L213 242Z M131 262L155 272L170 259L185 282H215L230 259L245 272L269 262Q251 312 200 311Q149 312 131 262Z"/></g>'''
    if key=='ghostchef':
        return '''<g class="chef-peek"><path fill="#fff8e7" d="M229 94V61Q225 35 245 34Q267 36 261 62L266 83L254 78L250 91L239 82Z"/><circle cx="240" cy="53" r="3"/><circle cx="252" cy="53" r="3"/><path d="M240 64Q246 70 252 63" fill="none" stroke-width="2"/></g><path fill="#fff8e7" d="M116 132Q80 109 100 79Q113 63 136 72Q145 36 178 53Q207 25 231 57Q268 41 281 77Q319 83 291 125L277 144H124Z"/><path fill="#e9ddc4" d="M119 129Q200 145 281 129L277 174Q200 157 123 174Z"/><path d="M149 88L152 130M200 76V136M251 91L249 131" fill="none" stroke="#c7b99f" stroke-width="3"/>'''
    raise KeyError(key)
