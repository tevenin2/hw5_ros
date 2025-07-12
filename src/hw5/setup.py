from setuptools import setup

package_name = 'hw5'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/hw5.launch.py']),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pjhllove',
    maintainer_email='your@email.com',
    description='Homework for ROS2 node communication',
    license='MIT',
    tests_require=['pytest'],
entry_points={
    'console_scripts': [
        'node1 = hw5.node1:main',
        'node2 = hw5.node2:main', 
        'node3 = hw5.node3:main', 
    ],
},
)
