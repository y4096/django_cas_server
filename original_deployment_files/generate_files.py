import os
from shutil import copyfile


def generate(port, project, domain_name, env):
    config_dir = '../config/'
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)

    def read_write(name, dst):
        with open(f'{name}.txt', encoding='utf-8') as f:
            original_text = f.read()
        text = original_text.format(port=port, project=project, domain_name=domain_name, env=env)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(text.lstrip())

    # nginx
    read_write('nginx', os.path.join(config_dir, f'{project}_{env}.conf'))
    # uwsgi
    read_write('uwsgi', os.path.join(config_dir, f'uwsgi.{env}.ini'))

    # deploy.sh
    read_write('deploy', '../deploy.sh')
    # Dockerfile
    read_write('dockerfile', '../Dockerfile')
    # start.sh
    copyfile('start.txt', '../start.sh')


if __name__ == '__main__':
    generate(8081, 'django_cas_server', 'localhost', 'stage')
