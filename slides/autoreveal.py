import sys
import re
import os
import shutil

global meta 
meta = None

def util_copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

def filter_content(content):
    lines = content.split('\n')
    return [ line for line in lines if not line.strip().startswith('#') ]

def get_content_as_list(filename):
    with open(filename,'r') as f:
        content = f.read()
    return filter_content(content)

def get_content(filename):
    with open(filename,'r') as f:
        content = f.read()
    return content


def split_sections(content):
    # split into ( meta, header, heading, body, footer )
    tags, indices = [], []
    for i in range(len(content)):
        if re.match('\[.+\]',content[i]):
            indices.append(i)
            tags.append(content[i].replace('[','').replace(']',''))
    endices = indices[1:] + [ len(content) ]
    # create a dictionary
    return dict(zip(tags, zip(indices,endices)))

def extract_content(content, index):
    roi = content[index[0]+1 : index[1]]

    def extract_unique():
        kvals = {}
        for line in roi:
            k,v = line.split('=')
            kvals[k.strip()] = v.strip()
        return kvals

    def extract():
        sec_type, sec_val = [],[]
        for line in roi:
            k,v = line.split('=')
            sec_type.append(k.strip())
            sec_val.append(v.strip())
        return tuple(zip(sec_type,sec_val))

    if content[index[0]] == '[body]':
        return extract()
    
    return extract_unique()

def render_init(meta, header_val, heading, body, templates = './templates', build = './build', log=False):
    header = templates + '/header.content'
    footer = templates + '/footer.content'

    if log:
        print('Copying templates to build/')
    # copy templates to build/
    util_copy_and_overwrite(templates,build)
    util_copy_and_overwrite(meta['res'],'build/res')
    
    # open file index.html in build
    with open(build + '/index.html', 'w') as findex: # open in (over)write mode
        # get content
        header_content = fill_header(get_content(header),header_val)
        heading_content = fill_heading(heading)
        body_content = fill_body(body)
        findex.write(header_content)
        findex.write(heading_content)
        findex.write(body_content)
        with open(footer,'r') as f:
            foot_content = f.read()
        findex.write(foot_content)

def fill_header(template, header):
    lines = template.split('\n')
    for i in range(len(lines)):
        if lines[i].startswith('x---'):
            break
    lines[i] = '\t\t<link rel="stylesheet" href="css/theme/{}.css" id="theme">'.format(header['theme'])
    body_open = '\n<body>\n<div class="reveal">\n<div class="slides">\n'
                                        
    return '\n'.join(lines) + body_open

def fill_heading(heading):
    title = '<h1>{}</h1>'.format(heading['title'])
    author = '<a href = "{0}">{1}</a>'.format(heading['web'],heading['author'])
    return '\n<section>\n{0}\n{1}\n</section>'.format(title,author)

def get_section(sec_type, sec_val):
    sec_content = get_content(meta['md'] + '/' + sec_val)
    md_template = '<section data-markdown>\n<script type="text/template">\n'\
            '{}\n</script></section>'.format(sec_content)
    return md_template


def fill_body(body):
    content = '' 
    for sect,secv in body:
        content += '\n' + get_section(sect,secv)
    return content + '\n'
    
def expand_md(md_files):
    for sect, secv in md_files:
        if 'md' in sect:
            # convert content to list
            lines = get_content(meta['md'] + '/' + secv).split('\n')
            # check for code &name.py&
            for i in range(len(lines)):
                if re.match('&.+&',lines[i]):
                    # use index to replace line with code
                    code_file = meta['code'] + '/' + lines[i].replace('&','').replace(' ','')
                    code_content = get_content(code_file).split('\n')
                    # replace ith element
                    lines[i] = '```'
                    code_content.append('```')
                    # add code to list
                    mod_content = '\n'.join(lines[:i+1] + code_content + lines[i+1:])
                    # (over)write to file
                    with open(meta['md'] + '/' + secv, 'w') as f:
                        f.write(mod_content)
                    # break now
                    break

            

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('>> Usage : python3 autoreveal.py config.ini')
        sys.exit()
    
    # get markdown filename
    filename = sys.argv[1]
    # get content
    content = get_content_as_list(filename)
    # split sections 
    tags = split_sections(content) 
    # get meta data
    meta = extract_content(content,tags['meta'])
    # get header information
    header  = extract_content(content,tags['header'])
    # heading
    heading = extract_content(content,tags['heading'])
    # body 
    body = extract_content(content,tags['body'])

    expand_md(body)

    # render
    render_init(meta,header,heading,body)
