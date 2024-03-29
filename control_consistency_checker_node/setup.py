from setuptools import find_packages, setup

package_name = 'control'

setup(
    name='control',
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'ament_index_python', 'PyYAML'],
    zip_safe=True,
    maintainer='shen',
    maintainer_email='lucidshenzhe@gmail.com',
    description='A ROS 2 package for consistency checking.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'consistency_checker = control.consistency_checker:main',
        ],
    },
)
