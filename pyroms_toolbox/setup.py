from setuptools import setup, find_packages

setup(
    name="pyroms_toolbox",
    version="0.1.0",
    packages=[
        'pyroms_toolbox',
        'pyroms_toolbox.BGrid_GFDL',
        'pyroms_toolbox.BGrid_POP',
        'pyroms_toolbox.BGrid_SODA',
        'pyroms_toolbox.CGrid_GLORYS',
        'pyroms_toolbox.Grid_GLORYS',
        'pyroms_toolbox.Grid_HYCOM',
        'pyroms_toolbox.seawater',
    ],
)
