from setuptools import find_packages, setup

setup(name='FunCLI',
      version='0.0',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['Click',
                        'Fabric', ],
      entry_points="""
        [console_scripts]
        f=cli:cli
    """, )
