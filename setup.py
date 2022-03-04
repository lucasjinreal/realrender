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
    version='0.0.3',
    author="Lucas Jin",
    author_email="11@qq.com",
    install_requires=REQUIREMENTS,
    description="RealRender: mesh3d render that most reliable.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jinfagang/realrender",
    packages=[
        'realrender',
        'realrender.sim3drender',
        'realrender.sim3drender.lib',
    ],
    # cmdclass={'build_ext': build_ext},
    ext_modules=cythonize([Extension("realrender.sim3drender.Sim3DR_Cython",
                           sources=["realrender/sim3drender/lib/rasterize.pyx",
                                    "realrender/sim3drender/lib/rasterize_kernel.cpp"],
                           language='c++',
                           include_dirs=[numpy.get_include()],
                           extra_compile_args=["-std=c++11"])]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2",
         "Programming Language :: Python :: 3",
         "License :: Other/Proprietary License",
         "Operating System :: OS Independent",
    ],


)
