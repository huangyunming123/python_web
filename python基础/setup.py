from distutils.core import setup

setup(
    name='my_package',#需要打包的名字
    version='0.1',
    py_modules=['my_package.Student','my_package.importTest'],#需要打包模块
)

