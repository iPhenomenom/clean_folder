from setuptools import setup

setup(name='clean_folder',
      version='0.0.1',
      description='Very useful code',
      url='https://github.com/iPhenomenom/clean_folder',
      author='Dmitriy',
      author_email='mytoreh@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean_folder=clean_folder.clean:main']}
      )