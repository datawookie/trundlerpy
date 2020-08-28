import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.1'
PACKAGE_NAME = 'trundlerpy'
AUTHOR = 'Laura Calcagni, Andrew B. Collier'
AUTHOR_EMAIL = 'l.calcagni@gmail.com, andrew@exegetic.biz'
URL = 'https://github.com/datawookie/trundlerpy'

LICENSE = ''
DESCRIPTION = 'Trundler Python Package'
LONG_DESCRIPTION = (HERE/"README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
"numpy==1.18.5",
"pandas== 1.0.5",
"requests==2.24.0"
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
