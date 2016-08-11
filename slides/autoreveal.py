import sys
import re
import os
import shutil


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

def render_init(templates = './templates', build = './build', log=False):
    header = templates + '/header.content'
    footer = templates + '/footer.content'
    body   = templates +   '/body.content'

    if log:
        print('Copying templates to build/')
    # copy templates to build/
    util_copy_and_overwrite(templates,build)
    
    # open file index.html in build
    with open(build + '/index.html', 'w') as findex: # open in (over)write mode
        findex.write(get_content(header))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit()
    
    # get markdown filename
    filename = sys.argv[1]
    # get content
    content = get_content_as_list(filename)
    # split sections 
    tags = split_sections(content) 
    #print(tags)
    # get meta data
    meta = extract_content(content,tags['meta'])
    # get header information
    header  = extract_content(content,tags['header'])
    # heading
    heading = extract_content(content,tags['heading'])
    # body 
    body = extract_content(content,tags['body'])

    # render
    render_init()









