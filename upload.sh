rm -r build dist direct_redis.egg-info
python setup.py sdist bdist_wheel \
&& twine upload dist/*
rm -r build dist direct_redis.egg-info