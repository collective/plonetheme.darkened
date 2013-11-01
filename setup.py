from setuptools import setup, find_packages
import os

version = '1.1'

setup(
        name='plonetheme.darkened',
        description='An installable Diazo theme for Plone 4.1',
        long_description=open('README.rst', 'rb').read()+'\n'+
                         open(os.path.join("docs", "INSTALL.txt")).read()+'\n'+
                         open(os.path.join("docs", "HISTORY.txt")).read(),
        version='1.1',
        author='Giacomo Spettoli',
        author_email='giacomo.spettoli@gmail.com',
        url='https://github.com/collective/plonetheme.darkened',
        packages=find_packages(),
        include_package_data=True,
        namespace_packages=[
            'plonetheme'
            ],
        install_requires=[
            'setuptools',
            'plone.app.theming',
            ],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Web Environment',
            'Framework :: Plone',
            'Framework :: Plone :: 4.1',
            'Framework :: Plone :: 4.2',
            'Framework :: Plone :: 4.3',
            'Framework :: Zope2',
            'Framework :: Zope3',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        keywords='web zope plone theme diazo darkened',
        entry_points={
            'z3c.autoinclude.plugin': 'target = plone',
            }
        )


