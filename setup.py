# from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
# with codecs_open('README.rst', encoding='utf-8') as f:
#     long_description = f.read()


setup(name='mica',
      version='0.0.1',
      description=u"Matplotlib Improved Color Abbreviations",
      #long_description=long_description,
      classifiers=[],
      keywords='Matplotlib',
      author=u"Julian Irwin",
      author_email='julian.irwin@gmail.com',
      url='https://github.com/julianirwin/mica',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      setup_requires=['nose>=1.0'],
      extras_require={
          'test': ['nose'],
      },
      test_suite = 'nose.collector',
      entry_points="""
      [console_scripts]
      pyskel=pyskel.scripts.cli:cli
      """
      )
