import sys


def to_html(content):
    if content != None:
        with open("myCV.html","w") as f:
            f.write(content)
        f.close()

def parse_files():
    config_file = "settings.py"
    try:
        data = {}
        with open(config_file) as handle:
            for line in handle:
                data['{' + line.split('=')[0].strip() + '}'] = line.split('=')[1].strip().strip('\"')
        handle.close()
    except:
        exit(1)
    if len(sys.argv) == 2:
        cv = sys.argv[1]
        if cv[-9:] == '.template':
            with open(cv, 'r') as handle:
                new_template = ''
                for line in handle:
                    
                    line = line.replace('{name}', data['{name}'])
                    line = line.replace('{surname}', data['{surname}'])
                    line = line.replace('{career}', data['{career}'])
                    new_template += line
                    new_template += '\n'
                    # i += 1
            handle.close()
            return new_template

def render():
    content = parse_files()
    to_html(content)

if __name__ == '__main__':
    render()

