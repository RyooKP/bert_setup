from seyuptools import setup

setup(
    name='bert_setup',
    version='0.0.1',
    description='bert setup for project',
    url='https://github.com/RyooKP/bert_setup.git',
    # download_url     = 'https://githur.com/rampart81/pyquibase/archive/1.0.tar.gz',
    author='kp.ryoo',
    author_email='kp.ryoo@yonsei.ac.kr',
    license='MIT',
    pakages=['bert_setup'],
    zip_safe=False,
    install_requires=[]
)


# from setuptools import setup, find_packages

# setup(
#     name             = 'pyquibase',
#     version          = '1.0',
#     description      = 'Python wrapper for liquibase',
#     author           = 'Eun Woo Song',
#     author_email     = 'songew@gmail.com',
#     url              = 'https://github.com/rampart81/pyquibase',
#     download_url     = 'https://githur.com/rampart81/pyquibase/archive/1.0.tar.gz',
#     install_requires = [ ],
#     packages         = find_packages(exclude = ['docs', 'tests*']),
#     keywords         = ['liquibase', 'db migration'],
#     python_requires  = '>=3',
#     package_data     =  {
#         'pyquibase' : [
#             'db-connectors/sqlite-jdbc-3.18.0.jar',
#             'db-connectors/mysql-connector-java-5.1.42-bin.jar',
#             'liquibase/liquibase.jar'
#     ]},
#     zip_safe=False,
#     classifiers      = [
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.2',
#         'Programming Language :: Python :: 3.3',
#         'Programming Language :: Python :: 3.4',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.6'
#     ]
# )
