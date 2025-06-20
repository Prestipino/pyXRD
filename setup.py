from setuptools import setup




setup(
    name='pyXRD',
    version='1.1.2',
    description='some tools for crystallography',
    author='C. Prestipino',
    author_email='carmelo.prestipino@ensicaen.fr',
    url='https://github.com/Prestipino/pyXRD',
    keywords=[
        'crystal', 'diffraction', 'crystallography'],
    packages=['pyXRD', 'pyXRD.IO', 'pyXRD.GII', 'pyXRD.Crystal'],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 3 - Alpha',
        ],
    install_requires=['numpy', 'matplotlib', 'scipy','lmfit', 'xraydb', 'Dans-Diffraction' ],
    package_data={'': []}
    )
