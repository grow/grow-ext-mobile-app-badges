from setuptools import setup


setup(
    name='grow-ext-mobile-app-badges',
    version='1.0.0',
    license='MIT',
    author='Grow SDK Authors',
    author_email='hello@grow.io',
    package_data={
        'grow_mobile_app_badges': [
            '*.yaml',
            "images/*/*",
        ],
    },
    packages=[
        'grow_mobile_app_badges',
    ],
)
