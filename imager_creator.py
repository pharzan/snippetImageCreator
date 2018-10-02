from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing
from wand.color import Color
from wand.compat import nested

import subprocess
code = """ 
const pluckDeep = key => obj => key.split('.').reduce((accum, key) => accum[key], obj)const compose = (...fns) => res => fns.reduce((accum, next) => next(accum), res)const unfold = (f, seed) => {const go = (f, seed, acc) => {const res = f(seed)return res ? go(f, res[1], acc.concat([res[0]])) : acc}return go(f, seed, [])}
"""

with open("code.txt", "w") as text_file:
    text_file.write("{0}".format(code))

shell_cmd = """ vim -c "argdo setf javascript | execute 'normal! gg=G' | execute 'call JsBeautify()' | execute 'wq!' | update" code.txt """
p = subprocess.call(shell_cmd, shell=True, stdout=subprocess.PIPE)
with open('code.txt', 'r') as myfile:
    code = myfile.read()


def get_words(para):
    words = para.split(" ")
    lines = []
    with Image(height=1080, width=1080) as img:
        line = words.pop(0)
        for word in words:
            line_width = draw.get_font_metrics(img, line + " " + word).text_width
            if line_width < 370:
                line = line + " " + word
            else:
                lines.append(line)
                line = word
        if line != "":
            lines.append(line)
    return lines

with Drawing() as ctx:
        with Image(width=1080, height=1080, background=Color("WHITE")) as img:
            with Drawing() as draw:
                draw.stroke_color = Color('black')
                draw.stroke_width = 2
                draw.fill_color = Color('black')

                EDITOR_WIDTH = 1000-80
                EDITOR_HEIGHT = 1000-80

                EDITOR_LEFT = 80
                EDITOR_TOP = 80
                draw.fill_color = Color('white')

                draw.rectangle(left=EDITOR_LEFT+10, top=EDITOR_TOP+10, right=None, bottom=None, width=EDITOR_WIDTH, height=EDITOR_HEIGHT, radius=5, xradius=None, yradius=None)

                draw.fill_color = Color('black')

                draw.rectangle(left=EDITOR_LEFT, top=EDITOR_TOP, right=None, bottom=None, width=EDITOR_WIDTH,
                            height=EDITOR_HEIGHT, radius=5, xradius=None, yradius=None)

                draw.fill_color = Color('red')
                draw.circle((100, 100),  # Center point
                            (105, 105))  # Perimeter point

                draw.fill_color = Color('yellow')
                draw.circle((120, 100),  # Center point
                            (125, 105))  # Perimeter point

                draw.fill_color = Color('green')
                draw.circle((140, 100),  # Center point
                            (145, 105))  # Perimeter point
                a = get_words(code)
                # print(a)
                draw.fill_color = Color('white')
                draw.stroke_color = Color('transparent')
                draw.font_family = './Raleway-Thin.ttf'
                draw.font_size = 24
                draw.text_interline_spacing = 15
                # img.caption(left=150, top=200,
                #             font='./Raleway-Regular.ttf', text="hello")

                # print(''.join([str(x) for x in a]))
                txt = '\n'.join([str(x) for x in a])
                draw.text(x=175, y=120,body=txt)
                metrics = draw.get_font_metrics(img, txt, multiline=True)
                print(metrics)
                # for i,line in enumerate(a):
                #     metrics = draw.get_font_metrics(img, line, multiline=True)
                #     draw.text(x=150, y=120+(i*35)+int(metrics.text_height), body=line)
                    # print( line, '\n')
                draw(img)
                img.sample(1080, 1080)
                img.save(filename="output.png")

