from bokeh.plotting import figure, show
import random

limit_xy = int(input('Type the limit for x coordenate -> '))

x = [i for i in range(limit_xy)]
y = [random.randint(0,100) for i in range(limit_xy)]

print(f'''
{x}

{y}

''')

p = figure(title='My first plop in Bokeh', x_axis_label = 'x', y_axis_label = 'y')

# p.line(x, y, legend_label="Temp.", color="blue", line_width=2)
# p.circle(x, y, legend_label="Points.", color="yellow", line_width=2)
p.vbar(x=x, top=y, legend_label="Rate", width=0.5, bottom=0, color="red")

show(p)