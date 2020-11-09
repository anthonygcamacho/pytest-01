from setuptools import setup, find_packages


setup(name='ssqaapitest',
      version='1.0',
      description="Practice API testing",
      author='Admas Kinfu',
      author_email='admas@supersqa.com',
      url='https://supersqa.com',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==6.1.2",
          "pytest-html==2.1.1",
          "requests==2.24.0",
          "requests-oauthlib==1.3.0",
          "PyMySQL==0.10.1",
          "WooCommerce==2.1.1",
      ]
      )
