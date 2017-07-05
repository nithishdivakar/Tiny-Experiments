import math

colors=[ "244,149, 66", "244,217, 66", "170,244, 66", " 69,244, 66", " 66,244,143", " 66,244,223", " 66,176,244", " 66,119,244","244, 66, 66","244,110, 66", "244,149, 66", "244,217, 66", "170,244, 66", " 69,244, 66", " 66,244,143", " 66,244,223", " 66,176,244", " 66,119,244","244, 66, 66","244,110, 66"]

radius  = 50.0
centerx = 200
centery = 200

px = radius
py = 0.0
step_angle   = 36
stroke_color ="0,0,0"
stroke_alpha = 0.0
color_alpha  = 0.10

print('''<body> <svg height="400" width="400">''',end='')
#print(list(range(0,361,36)))
for angle,color in zip(range(0,361,step_angle),colors):
  xx     = px*math.cos(angle) - py*math.sin(angle)
  yy     = px*math.sin(angle) + py*math.cos(angle)
  color  = "255,0,255"
  string = '''<circle cx="{:4.2f}" cy="{:4.2f}" r="100" stroke="rgba({}, {})" stroke-width="1" fill="rgba({}, {})" angle="{}"/>'''.format(
    xx+centerx,
    yy+centery,
    stroke_color,
    stroke_alpha,
    color,
    color_alpha,
    angle
  )
  print(string, end='')
print("</svg>")
