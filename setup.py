from setuptools import setup




setup(
    name='Dans_Diffraction',
    packages=['pyXRD'],
    version='alpha1',
    description='some tools for crystallography',
    author='C.Prestipino',
    author_email='carmelo.prestipino@univ-rennes.fr',
    url='https://github.com/Prestipino/pyXRD',
    keywords=[
        'crystal', 'diffraction', 'crystallography'],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 3 - Alpha',
        ],
    install_requires=['numpy', 'matplotlib', 'Dans-Diffraction'],
    package_data={'': []}
    )
