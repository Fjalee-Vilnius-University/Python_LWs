#include <Python.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>

static PyObject *moduleError;


static int get_fibonacci_nth_nm(int n){
    if(n <= 0)
        return -1;
    else if(n == 1)
        return 0;
    else if(n == 2)
        return 1;
    else
        return get_fibonacci_nth_nm(n-1) + get_fibonacci_nth_nm(n-2);
}

static PyObject * fibonacci_nth_nm(PyObject *self, PyObject *args)
{
  int n = 0;
  int result = 0;

  if (!PyArg_ParseTuple(args, "i", &n))
  {
    PyErr_Format(moduleError, "Can't parse input");
    return NULL;
  }

  if(n <= 0)
  {
    PyErr_Format(moduleError, "Can't handle negative numbers or 0");
    return NULL;
  }

  result = get_fibonacci_nth_nm(n);

  return PyLong_FromLong(result);
}

static PyMethodDef fibonacciModuleMethods[] = {
  {"fibonacci_nth_nm", fibonacci_nth_nm, METH_VARARGS, "module for finding fibonacci nth number"},
  {NULL, NULL, 0, NULL}
};


static struct PyModuleDef fibonacciNthNmModule = {
  PyModuleDef_HEAD_INIT,
  "getFibonacciNthNm",
  "function for finding fibonacci nth number",
  -1,
  fibonacciModuleMethods
};

PyMODINIT_FUNC PyInit_checkPalindrome(void)
{
  return PyModule_Create(&fibonacciNthNmModule);
}

PyMODINIT_FUNC PyInit_empty(void)
{
  PyObject * module = PyModule_Create(&fibonacciNthNmModule);
  moduleError = PyErr_NewException("module.error", NULL, NULL);
  Py_INCREF(moduleError);
  PyModule_AddObject(module, "error", moduleError);
}
