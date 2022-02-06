import setuptools
from distutils.core import setup, Extension
try:
    from Cython.Build import cythonize
    from Cython.Distutils import build_ext
except Exception:
    print('Cython should be installed.')
import numpy

with open("readme.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = ["numpy", "opencv-python", "alfred-py", "cython"]


setuptools.setup(
    name='realrender',
    version='0.0.1',
    author="Lucas Jin",
    author_email="11@qq.com",
    install_requires=REQUIREMENTS,
    description="RealRender: mesh3d render that most reliable.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jinfagang/realrender",
    packages=setuptools.find_packages(),
    # cmdclass={'build_ext': build_ext},
    ext_modules=cythonize([Extension("realrender.Sim3DR.Sim3DR_Cython",
                           sources=["realrender/Sim3DR/lib/rasterize.pyx",
                                    "realrender/Sim3DR/lib/rasterize_kernel.cpp"],
                           language='c++',
                           include_dirs=[numpy.get_include()],
                           extra_compile_args=["-std=c++11"])]),
    classifiers=[
        "Programming Language :: Python :: 2",
         "Programming Language :: Python :: 3",
         "License :: Other/Proprietary License",
         "Operating System :: OS Independent",
    ],


)
