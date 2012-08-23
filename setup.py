from setuptools import setup, find_packages #your system should use distribute which is successor to setuptools 
                                            # and distutils, http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-and-setuptools

package = __import__('simplemenu')
setup(name='django-simplemenu',
    install_requires=['distribute'], # let's use the enhanced setuptools
    version=package.get_version(),
    url='http://github.com/danielsokolowski/django-simplemenu',
    license='BSD',
    description=package.__doc__.strip(),
    author='Alex Vasi , Justin Steward , Daniel Sokolowski ',
    author_email='unemelpmis-ognajd@danols.com',
    include_package_data=True, # this will use MANIFEST.in during install where we specify all of our additional files
    packages=find_packages(),
    # Below is not needed as we are utilizing MANIFEST.in 
    #package_data={'simplemenu': ['locale/en/LC_MESSAGES/*', 
    #                             'locale/ru/LC_MESSAGES/*']
    #              },
    scripts=[],
    requires=[],
    )
