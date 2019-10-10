import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
     name='folderclone',
     version='0.5.0',
     author='Spazzlo',
     description='A tool to copy large folders to Shared Drives.',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/Spazzlo/folderclone',
     packages=['folderclone'],
     install_requires=[
        'pyreadline',
        'google_auth_oauthlib',
        'urllib3',
        'httplib2shim',
        'protobuf',
        'google_api_python_client'
    ],
     classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
     ]
 )