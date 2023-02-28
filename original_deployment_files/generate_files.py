import os
from shutil import copyfile


def generate(stage_port, prod_port, project, stage_domain, prod_domain):
    config_dir = '../config/'
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)

    def read_write(name, dst, env='', domain_name='', port=''):
        with open(f'{name}.txt', encoding='utf-8') as f:
            original_text = f.read()
        text = original_text.format(port=port, project=project, domain_name=domain_name, env=env,
                                    stage_domain=stage_domain, prod_domain=prod_domain)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(text.lstrip())

    # nginx
    read_write('nginx', os.path.join(config_dir, f'{project}_stage.conf'), 'stage',
               domain_name=stage_domain, port=stage_port)
    read_write('nginx', os.path.join(config_dir, f'{project}_prod.conf'), 'prod',
               domain_name=prod_domain, port=prod_port)
    # uwsgi
    read_write('uwsgi', os.path.join(config_dir, f'uwsgi.stage.ini'), 'stage', port=stage_port)
    read_write('uwsgi', os.path.join(config_dir, f'uwsgi.prod.ini'), 'prod', port=prod_port)

    # deploy.sh
    read_write('deploy', '../deploy.sh')
    # Dockerfile
    read_write('dockerfile', '../Dockerfile')
    # start.sh
    copyfile('start.txt', '../start.sh')


if __name__ == '__main__':
    generate(8081, 8091, 'go_tube', 'test.gotube.app', 'api.gotube.app')
