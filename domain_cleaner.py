from ruamel.yaml import YAML

yaml = YAML()

with open('./domain/domain.yml') as fp:
    data = yaml.load(fp)
    for x in data['templates']:
        print('  - '+x)