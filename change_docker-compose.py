import yaml

image_names = []
try:
    with open('docker-compose.yml') as file:
        for line in file.readlines():
            line = ''.join(line.split())
            if line.startswith("#image"):
                image_names.append(line[7:])

    with open('docker-compose.yml', 'r') as stream:
        file = yaml.safe_load(stream)
        
        num = 0
        for serv_name, serv in file['services'].items():
            serv.pop('build', None)
            serv['image'] = image_names[num]
            num += 1

        with open('docker-compose1.yml', 'w') as new_file:
            yaml.dump(file, new_file)
            print(True)

except:
    print(False)