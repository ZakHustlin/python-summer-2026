import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if i.startswith('#') and len(i.split(' ')[0]) <= 6:
            n = len(i.split(' ')[0])
            nstr = str(n)
            i = ('<h' + nstr + '>') + i[n+1:] + ('</h' + nstr + '>')
            
        m = re.match(r'\* (.*)', i)
        
        if m:
            curr = m.group(1)
            if not in_list:
                in_list = True
                i = '<ul><li>' + curr + '</li>'
            else:
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                res += '</ul>'
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        i = re.sub('__(.*)__', r'<strong>\1</strong>', i)
        i = re.sub('_(.*)_', r'<em>\1</em>', i)
        res += i
    if in_list:
        res += '</ul>'
    return res
