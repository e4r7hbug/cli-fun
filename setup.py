from setuptools import find_packages, setup

setup(name='CLIFun',
      version='0.0',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['Click',
                        'Fabric', ],
      entry_points="""
        [console_scripts]
        f=cli_fun.__main__:cli
    """, )
