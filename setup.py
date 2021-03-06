import setuptools
version = '1.15.0'

setuptools.setup(
    name='electrumX',
    version=version,
    scripts=['electrumx_server', 'electrumx_rpc', 'electrumx_compact_history'],
    python_requires='>=3.7',
    install_requires=['aiorpcX[ws]>=0.18.3,<0.19', 'attrs',
                      'plyvel', 'pylru', 'aiohttp>=3.3'],
    extras_require={
        'rocksdb': ['python-rocksdb>=0.6.9'],
        'uvloop': ['uvloop>=0.14'],
    },
    packages=setuptools.find_packages(include=('electrumx*',)),
    description='ElectrumX Server',
    author='Neil Booth',
    author_email='kyuupichan@gmail.com',
    license='MIT Licence',
    url='https://github.com/kyuupichan/electrumx',
    long_description='Server implementation for the Electrum protocol',
    download_url=('https://github.com/kyuupichan/electrumX/archive/'
                  f'{version}.tar.gz'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
        'Topic :: Internet',
    ],
)
