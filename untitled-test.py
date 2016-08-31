import re

i = 'https://s-passets-cache-ak0.pinimg.com/webapp/style/app/common/images/pin_grid-1x-9bd0bc61.jpg'

pattern = r'src\=|.{0,10}(h.{0,25}\/{2}.{1,50}:*\/{0,50}.{0,150}jpg*) *'



pattern1 = '\/\/.+'


purified = re.search(pattern, i).group(0)
purified1 = re.search(pattern1, i).group(0)

if re.search(pattern, i):
    print(purified)


elif re.search(pattern1  , i):
    print(purified1)

