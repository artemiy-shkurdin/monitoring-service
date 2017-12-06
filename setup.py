from setuptools import setup, find_packages
setup(
    name="monitor",
    version="0.1.2",
    packages=find_packages(),
    scripts=['monitor/rest.py','monitor/checker.py'],
    zip_safe=True,
    entry_points = {
        'console_scripts': [
        	'monitor-rest=monitor.rest:RunRest',        # сервис с REST интерфейсом
        	'monitor-checker=monitor.checker:RunChecker'   # сервис который осуществляет проверки
        ],
    }
)