from distutils.core import setup
from setuptools import find_packages

setup(
    name='autokeras',
    packages=find_packages(exclude=('tests',)),
    install_requires=['scipy==1.1.0',
                      'torch==1.0.0',
                      'torchvision==0.2.1',
                      'numpy==1.15.4',
                      'keras==2.2.4',
                      'scikit-learn==0.20.1',
                      'scikit-image==0.14.1',
                      'tqdm==4.29.0',
                      'tensorflow==1.12.0',
                      'imageio==2.4.1',
                      'requests==2.20.1',
                      'lightgbm==2.2.2',
                      'pandas==0.23.4',
                      'librosa==0.6.2',
                      'numba',
                      'inflect',
                      'unidecode',
                      'nltk==3.3',
                      'lws==1.2',
                      'opencv-python==4.0.0.21'],
    version='0.3.6',
    description='AutoML for deep learning',
    author='DATA Lab at Texas A&M University',
    author_email='jhfjhfj1@gmail.com',
    url='http://autokeras.com',
    download_url='https://github.com/jhfjhfj1/autokeras/archive/0.3.6.tar.gz',
    keywords=['AutoML', 'keras'],
    classifiers=[]
)
