import setuptools

setuptools.setup(
    name="direct_redis",
    version="0.3.1",
    license='MIT',
    author="Yonghee Cheon",
    author_email="yonghee.cheon@gmail.com",
    description="Serialize any python datatypes and does redis actions using redis-py",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yonghee12/direct-redis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.4',
    install_requires=['redis==3.4.1'],
)
