from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing
from wand.color import Color
from wand.compat import nested


code = """ 
        const pluckDeep = key => obj => key.split('.').reduce((accum, key) => accum[key], obj)

const compose = (...fns) => res => fns.reduce((accum, next) => next(accum), res)

const unfold = (f, seed) => {
  const go = (f, seed, acc) => {
    const res = f(seed)
    return res ? go(f, res[1], acc.concat([res[0]])) : acc
  }
  return go(f, seed, [])
}
"""
with Drawing() as ctx:
    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.stroke_width = 2
        draw.fill_color = Color('black')

        EDITOR_WIDTH = 1000-80
        EDITOR_HEIGHT = 1000-80

        EDITOR_LEFT = 80
        EDITOR_TOP = 80
        draw.fill_color = Color('white')

        draw.rectangle(left=EDITOR_LEFT+10, top=EDITOR_TOP+10, right=None, bottom=None, width=EDITOR_WIDTH,
                       height=EDITOR_HEIGHT, radius=5, xradius=None, yradius=None)

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

        draw.fill_color = Color('white')
        draw.stroke_color = Color('transparent')
        draw.font=''
        draw.text(x=150,
                  y=175,
                  body=code)

        with nested(Image(width=1080, height=1080, background=Color("WHITE")),
                    Image(width=100, height=100, background=Color("transparent"))) as (img,
                                                                                       shadow):

            draw(img)
            img.sample(1080, 1080)
            img.save(filename="output.png")

