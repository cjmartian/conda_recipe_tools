#!/usr/bin/env python

from setuptools import setup

setup(
    name='conda_recipe_tools',
    version='0.1.0',
    description="Tools for maintaining and updating conda recipes",
    url='https://github.com/jjhelmus/conda_recipe_tools',
    author="Jonathan J. Helmus",
    author_email='jjhelmus@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=[
        'conda_recipe_tools',
    ],
    install_requires=[
        'beautifulsoup4',
        'feedparser',
        'jinja2',
        'pyyaml',
        'requests',
        ],
    entry_points={
        'console_scripts': [
            'channel_newest=conda_recipe_tools.cli.channel_newest:main',
            'create_clobber=conda_recipe_tools.cli.create_clobber:main',
            'create_diff_report=conda_recipe_tools.cli.create_diff_report:main',
            'extract_index_json=conda_recipe_tools.cli.extract_index_json:main',
            'find_changed_feedstocks=conda_recipe_tools.cli.find_changed_feedstocks:main',
            'find_latest=conda_recipe_tools.cli.find_latest:main',
            'find_outdated_packages_pypi=conda_recipe_tools.cli.find_outdated_packages_pypi:main',
            'gh=conda_recipe_tools.cli.gh:main',
            'prepare_batch_file=conda_recipe_tools.cli.prepare_batch_file:main',
            'push_feedstock_changes=conda_recipe_tools.cli.push_feedstock_changes:main',
            'pypi=conda_recipe_tools.cli.pypi:main',
            'replace_index_json=conda_recipe_tools.cli.replace_index_json:main',
            'rebuild_what=conda_recipe_tools.cli.rebuild_what:main',
            'reqs=conda_recipe_tools.cli.reqs:main',
            'run_grimlock=conda_recipe_tools.cli.run_grimlock:main',
            'show_git_messages=conda_recipe_tools.cli.show_git_messages:main',
            'sync_cf=conda_recipe_tools.cli.sync_cf:main',
            'update_recipe=conda_recipe_tools.cli.update_recipe:main',
            'upstream_newer=conda_recipe_tools.cli.upstream_newer:main',
            'upstream_stats=conda_recipe_tools.cli.upstream_stats:main',
            'what_needs=conda_recipe_tools.cli.what_needs:main',
        ]
    },
    license="BSD 3-clause",
)
