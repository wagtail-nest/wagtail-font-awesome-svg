import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wagtail-font-awesome-svg",
    version="1.1",
    author="Coen van der Kamp",
    author_email="coen@fourdigits.nl",
    description="Font Awesome icons as SVG for Wagtail",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wagtail-nest/wagtail-font-awesome-svg",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        # 'CC BY 4.0 License'  # TODO Find trove classifier.
        'License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 5',
        'Framework :: Wagtail :: 6',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    python_requires='>=3.8',
    include_package_data=True,
)
