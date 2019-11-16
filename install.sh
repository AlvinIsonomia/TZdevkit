rm *.so
rm -r bulid
swig -c++ -python polyiou.i
python setup.py build_ext --inplace
