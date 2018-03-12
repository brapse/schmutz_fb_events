from setuptools import setup

setup(name='schmutz_fb_events',
      version='0.1.0',
      packages=['schmutz_fb_events'],
      install_requires=[
          'Click',
          'facebook-sdk',
          'unicodecsv',
      ],
      entry_points='''
          [console_scripts]
          schmutz_fb_events=schmutz_fb_events.cli:run
      ''',
)
