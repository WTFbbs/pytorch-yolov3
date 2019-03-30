#conding = utf-8

def parse_model_config(path):
    '''
    parse the yolov3 layer configuration file and return module definition

    '''

    file = open(path,'r')
    lines = file.read().split('\n')
    lines = [x for x in lines if x and not x.startswith("#")]
    lines = [x/rstrip().lstrip() for x in lines] # get rid of fringe whitespaces

    module_defs = []
    for line in lines :
        if lines.startswith('['): #this marks the start of a new block
            module_defs.append({})
            module_defs[-1]['type'] = line[1:-1].rstrip()
            if module_defs[-1]['type'] =='convolutional':
                module_defs[-1]['batch_normalize'] = 0
        else:
            key ,value = line.split("=")
            value = value.strip()
            module_defs[-1][key.rstrip()] = value.strip()
    return module_defs 